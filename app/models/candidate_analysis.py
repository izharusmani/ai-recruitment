from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base

class CandidateAnalysis(Base):
    __tablename__ = "candidate_analysis"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)
    job_id = Column(Integer, ForeignKey("job_descriptions.id"), nullable=False)
    score = Column(Integer, nullable=True)
    recommendation = Column(String, nullable=True)
    strengths = Column(String, nullable=True)
    weaknesses = Column(String, nullable=True)
    matched_skills = Column(String, nullable=True)
    missing_skills = Column(String, nullable=True)
    analysis_result = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    candidate = relationship("Candidate", backref="analyses")
    job_description = relationship("JobDescription", backref="analyses")