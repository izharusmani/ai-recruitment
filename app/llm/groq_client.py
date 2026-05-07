from langchain_groq import ChatGroq
from app.core.config import settings

def get_llm():
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama3-70b-8192"
    )