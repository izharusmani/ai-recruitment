from fastapi import APIRouter
from app.graph.workflow import app

router = APIRouter()

@router.post("/analyze-resume")
def analyze_resume(payload: dict):

    result = app.invoke({
        "resume_text": payload["resume_text"],
        "job_description": payload["job_description"]
    })

    return result