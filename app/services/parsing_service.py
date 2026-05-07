import json
from app.services.llm_service import ask_llm
from app.constants.prompts import RESUME_PARSING_PROMPT


def parse_resume(text: str):

    user_prompt = f"""
    Extract structured resume data from this text:

    {text}
    """

    result =  ask_llm(
        user_prompt=user_prompt,
        system_prompt=RESUME_PARSING_PROMPT
    )

    try:
        return json.loads(result)
    except:
        return {"error": "Invalid JSON from LLM", "raw": result} 