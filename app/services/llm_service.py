from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_llm(user_prompt: str, system_prompt: str):
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=f"""
                SYSTEM: {system_prompt}
                USER: {user_prompt}
                Return ONLY valid JSON. No explanation.
                """
            )

        return response.text

    except Exception as e:
        print("LLM Error:", e)
        return None