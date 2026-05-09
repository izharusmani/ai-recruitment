import logging
import os
from typing import List

from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.resume import Resume
from app.models.candidate import Candidate
from app.models.job_description import JobDescription
from app.models.candidate_analysis import CandidateAnalysis

from app.services.resume_service import process_resume
from app.graph.workflow import app_graph
from app.utils.clean_ai_result import clean_ai_result

# =========================
# LOGGING
# =========================
logger = logging.getLogger("resume_upload")
logging.basicConfig(level=logging.INFO)

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"]
)


@router.post("/upload")
def upload_resume(
    job_id: int = Form(...),
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db)
):

    # =========================
    # GET JOB
    # =========================
    job = db.query(JobDescription).filter(
        JobDescription.id == job_id
    ).first()

    if not job:
        return {"status": False, "message": "Job not found"}

    uploaded_resumes = []

    # =========================
    # LOOP FILES
    # =========================
    for file in files:

        try:
            logger.info(f"Processing file: {file.filename}")

            # =========================
            # PROCESS RESUME
            # =========================
            result = process_resume(file)
            logger.info(f"Extracted text length: {len(result['parsed_data'])} characters")
            parsed = result["parsed_data"]

            # =========================
            # FIND / CREATE CANDIDATE
            # =========================
            existing_candidate = db.query(Candidate).filter(
                Candidate.email == parsed["email"]
            ).first()

            if existing_candidate:

                existing_candidate.full_name = parsed.get("full_name")
                existing_candidate.phone = parsed.get("phone")

                db.commit()
                db.refresh(existing_candidate)

                candidate = existing_candidate

            else:

                candidate = Candidate(
                    full_name=parsed.get("full_name"),
                    email=parsed.get("email"),
                    phone=parsed.get("phone")
                )

                db.add(candidate)
                db.commit()
                db.refresh(candidate)

            # =========================
            # RESUME HANDLING
            # =========================
            existing_resume = db.query(Resume).filter(
                Resume.candidate_id == candidate.id
            ).first()

            if existing_resume:

                if existing_resume.file_path and os.path.exists(existing_resume.file_path):
                    os.remove(existing_resume.file_path)

                existing_resume.file_path = result["file_path"]
                existing_resume.extracted_text = result["extracted_text"]
                existing_resume.parsed_data = result["parsed_data"]

                db.commit()
                db.refresh(existing_resume)

                resume_status = "Resume Updated"

            else:

                resume = Resume(
                    candidate_id=candidate.id,
                    file_path=result["file_path"],
                    extracted_text=result["extracted_text"],
                    parsed_data=result["parsed_data"]
                )

                db.add(resume)
                db.commit()
                db.refresh(resume)

                resume_status = "Resume Uploaded"

            # =========================
            # AI INPUT
            # =========================
            ai_input = {
                "candidate_id": candidate.id,
                "resume_text": result["extracted_text"],
                "job_description": job.description
            }

            # =========================
            # RUN AI AGENT
            # =========================
            ai_raw_result = app_graph.invoke(ai_input)

            logger.info("==== RAW AI RESULT ====")
            logger.info(ai_raw_result)

            # =========================
            # CLEAN AI RESULT
            # =========================
            ai_clean_result = clean_ai_result(ai_raw_result)

            # logger.info("==== CLEAN AI RESULT ====")
            # logger.info(ai_clean_result)

            # =========================
            # SAVE ANALYSIS
            # =========================
            analysis_exists = db.query(CandidateAnalysis).filter(
                CandidateAnalysis.candidate_id == candidate.id,
                CandidateAnalysis.job_id == job.id
            ).first()

            if analysis_exists:

                # =========================
                # UPDATE EXISTING
                # =========================
                analysis_exists.score = (
                    ai_clean_result.get("score")
                    or ai_clean_result.get("match_percentage")
                    or 0
                )

                analysis_exists.recommendation = ai_clean_result.get("recommendation")
                analysis_exists.strengths = ai_clean_result.get("strengths", [])
                analysis_exists.weaknesses = ai_clean_result.get("weaknesses", [])
                analysis_exists.matched_skills = ai_clean_result.get("matched_skills", [])
                analysis_exists.missing_skills = (
                    ai_clean_result.get("missing_skills")
                    or ai_clean_result.get("skill_gaps", [])
                )

                db.commit()
                db.refresh(analysis_exists)

                analysis = analysis_exists

            else:

                # =========================
                # CREATE NEW
                # =========================
                analysis = CandidateAnalysis(
                    candidate_id=candidate.id,
                    job_id=job.id,

                    score=(
                        ai_clean_result.get("score")
                        or ai_clean_result.get("match_percentage")
                        or 0
                    ),

                    recommendation=ai_clean_result.get("recommendation"),

                    strengths=ai_clean_result.get("strengths", []),
                    weaknesses=ai_clean_result.get("weaknesses", []),

                    matched_skills=ai_clean_result.get("matched_skills", []),

                    missing_skills=(
                        ai_clean_result.get("missing_skills")
                        or ai_clean_result.get("skill_gaps", [])
                    )
                )

                db.add(analysis)
                db.commit()
                db.refresh(analysis)

            # =========================
            # RESPONSE
            # =========================
            uploaded_resumes.append({
                "candidate_id": candidate.id,
                "candidate_name": candidate.full_name,
                "email": candidate.email,
                "resume_status": resume_status,

                "ai_score": (
                    ai_clean_result.get("score")
                    or ai_clean_result.get("match_percentage")
                    or 0
                ),

                "recommendation": ai_clean_result.get("recommendation")
            })

        except Exception as e:

            logger.exception(f"Failed processing file: {file.filename}")

            uploaded_resumes.append({
                "file": file.filename,
                "status": "Failed",
                "error": str(e)
            })

    # =========================
    # FINAL RESPONSE
    # =========================
    return {
        "status": True,
        "message": "Bulk upload and AI analysis completed",
        "job_id": job.id,
        "job_title": job.title,
        "total_files": len(files),
        "results": uploaded_resumes
    }