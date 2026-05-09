from typing import TypedDict, Optional


class RecruitmentState(TypedDict):

    candidate_id: int

    resume_text: str

    parsed_data: dict

    job_description: str

    match_score: str

    decision: str