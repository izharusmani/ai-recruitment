from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CandidateAnalysisSchema(BaseModel):
    id: Optional[int]
    candidate_id: int
    job_id: int
    score: Optional[int] = None
    recommendation: Optional[str] = None
    strengths: Optional[str] = None
    weaknesses: Optional[str] = None
    matched_skills: Optional[str] = None
    missing_skills: Optional[str] = None
    analysis_result: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True