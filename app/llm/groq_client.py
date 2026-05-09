# from langchain_groq import ChatGroq
# from app.core.config import settings

# def get_llm():
#     return ChatGroq(
#         api_key=settings.GROQ_API_KEY,
#         model="llama3-70b-8192"
#     )

from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_llm():
    return ChatGoogleGenerativeAI(
        google_api_key=settings.GEMINI_API_KEY,
        model="gemini-1.5-flash",
        temperature=0
    )