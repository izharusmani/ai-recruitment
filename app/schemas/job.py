from pydantic import BaseModel
from typing import Optional, Dict, Any

class JobCreate(BaseModel):
    title: str
    description: str
    required_skills: list[str] | None = None
    preferred_skills: list[str] | None = None
    experience: Optional[str] = None
    experience_years: int | None = None
    metadata: Optional[Dict[str, Any]] = None  # optional flexible field