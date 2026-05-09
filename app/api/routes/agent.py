from fastapi import APIRouter

from app.graph.workflow import app_graph

router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"]
)


@router.post("/analyze")
def analyze_candidate(payload: dict):

    result = app_graph.invoke({

        "candidate_id": payload["candidate_id"],

        "resume_text": payload["resume_text"],

        "job_description": payload["job_description"]
    })

    return result