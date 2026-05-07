from app.utils.file_handler import save_uploaded_file
from app.utils.text_extractor import extract_text_from_pdf
from app.services.parsing_service import parse_resume
from app.agents.recruitment_agent import analyze_candidate, match_candidate


def process_resume_workflow(file, job_description=None):
    
    # 1. Save file
    file_path = save_uploaded_file(file)

    # 2. Extract text
    resume_text = extract_text_from_pdf(file_path)

    # 3. Structured parsing (JSON)
    parsed_data = parse_resume(resume_text)

    # 4. AI analysis
    analysis = analyze_candidate(resume_text)

    result = {
        "file_path": file_path,
        "resume_text": resume_text,
        "parsed_data": parsed_data,
        "analysis": analysis
    }

    # 5. Optional job matching
    if job_description:
        result["match"] = match_candidate(resume_text, job_description)

    return result