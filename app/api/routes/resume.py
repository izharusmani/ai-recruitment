from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.api.deps import get_db
from app.services.resume_service import process_resume

router = APIRouter(prefix="/resumes", tags=["Resumes"])


@router.post("/upload")
def upload_resume(
    candidate_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    result = process_resume(file)

    resume = Resume(
        candidate_id=candidate_id,
        file_path=result["file_path"],
        extracted_text=result["extracted_text"],
        parsed_data=result["parsed_data"]
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume 