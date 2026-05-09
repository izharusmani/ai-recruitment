from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.dialects.postgresql import JSONB


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
        unique=True
    )

    file_path = Column(String, nullable=False)

    extracted_text = Column(Text, nullable=True)

    parsed_data = Column(JSONB, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    candidate = relationship("Candidate", backref="resume")