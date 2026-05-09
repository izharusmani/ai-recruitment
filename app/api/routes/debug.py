from fastapi import APIRouter
from app.utils.gemini_debug import list_gemini_models

router = APIRouter(prefix="/debug", tags=["Debug"])

@router.get("/gemini-models")
def get_gemini_models():
    return list_gemini_models()