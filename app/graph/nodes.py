from app.llm.groq_client import get_llm
from app.services.parsing_service import parse_resume
from app.services.matching_service import calculate_match
from app.services.resume_service import process_resume

llm = get_llm()

def extract_skills_node(state):
    prompt = f"""
    Extract technical skills from this resume:

    {state['resume_text']}

    Return comma separated skills only.
    """

    response = llm.invoke(prompt)

    return {
        "skills": [s.strip() for s in response.content.split(",")]
    }

def scoring_node(state):
    skills = state["skills"]
    jd = state["job_description"]

    result = calculate_match(skills, jd)  # your existing service

    return {
        "score": result["score"]
    }


def decision_node(state):
    score = state["score"]

    if score >= 75:
        decision = "shortlist"
    elif score >= 50:
        decision = "review"
    else:
        decision = "reject"

    return {"decision": decision} 