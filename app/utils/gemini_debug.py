from google import genai
from app.core.config import settings
import logging

logger = logging.getLogger("gemini_models")

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def list_gemini_models():
    try:
        models = client.models.list()

        logger.info("Available Gemini Models:")

        for m in models:
            logger.info(m.name)

        return [m.name for m in models]

    except Exception as e:
        logger.error(f"Failed to list models: {e}")
        return []