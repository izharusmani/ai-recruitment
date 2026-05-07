from typing import TypedDict, Optional, List

class RecruitState(TypedDict):
    resume_text: str
    skills: List[str]
    job_description: str
    score: float
    decision: str
    candidate_id: Optional[int]