from app.services.llm_service import ask_llm
from app.constants.prompts import JOB_MATCH_PROMPT

def calculate_match(resume_text, jd_text):

    user_prompt = f"""
    Compare resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Give matching score.
    """

    return ask_llm(user_prompt=user_prompt, system_prompt=JOB_MATCH_PROMPT)