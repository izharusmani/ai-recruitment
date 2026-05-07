from fastapi import APIRouter, UploadFile, File, Form
from app.agents.workflows import process_resume_workflow

router = APIRouter(prefix="/workflow", tags=["Workflow"])


@router.post("/resume")
def run_resume_workflow(
    file: UploadFile = File(...),
    job_description: str = Form(None)
):
    result = process_resume_workflow(file, job_description)
    return result