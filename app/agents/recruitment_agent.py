from app.services.llm_service import ask_llm
from app.constants.prompts import HR_SYSTEM_PROMPT


def analyze_candidate(resume_text: str):
    prompt = f"""
    Analyze this resume:

    {resume_text}

    Return:
    - Skills
    - Experience level
    - Strengths
    - Weaknesses
    - Suitability score (0-100)
    """

    return ask_llm(
        user_prompt=prompt,
        system_prompt=HR_SYSTEM_PROMPT
    )


def match_candidate(resume_text: str, job_description: str):
    prompt = f"""
    Compare resume with job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return:
    - Match percentage
    - Skill gaps
    - Recommendation (Hire / Reject / Shortlist)
    """

    return ask_llm(
        user_prompt=prompt,
        system_prompt=HR_SYSTEM_PROMPT
    ) 