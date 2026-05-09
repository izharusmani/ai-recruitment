from app.services.parsing_service import parse_resume
from app.services.matching_service import calculate_match


# =========================
# PARSE RESUME NODE
# =========================
def parse_resume_node(state):

    parsed = parse_resume(state["resume_text"])

    state["parsed_data"] = parsed

    return state

# =========================
# MATCHING NODE
# =========================
def matching_node(state):

    score = calculate_match(
        state["resume_text"],
        state["job_description"]
    )

    state["match_score"] = score

    return state


# =========================
# DECISION NODE
# =========================
def decision_node(state):

    score_text = state["match_score"]

    # Simple logic
    if "80" in score_text or "90" in score_text:
        decision = "Shortlisted"
    else:
        decision = "Rejected"

    state["decision"] = decision

    return state