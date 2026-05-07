from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Resume Upload (Request)
class ResumeCreate(BaseModel):
    candidate_id: int


# Resume Response
class ResumeResponse(BaseModel):
    id: int
    candidate_id: int
    file_path: str
    extracted_text: Optional[str]
    skills: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True