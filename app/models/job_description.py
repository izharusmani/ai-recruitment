from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=True)
    description = Column(Text, nullable=False)
    required_skills = Column(Text, nullable=True)
    preferred_skills = Column(Text, nullable=True)
    experience = Column(String, nullable=True)
    experience_years = Column(Integer, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())