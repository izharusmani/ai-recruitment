from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Create Candidate (Request)
class CandidateCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None


# Response Model
class CandidateResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True   # for SQLAlchemy (important)


# Optional Update Schema
class CandidateUpdate(BaseModel):
    full_name: Optional[str]
    phone: Optional[str]