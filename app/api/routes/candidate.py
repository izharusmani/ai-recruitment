from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.candidate import CandidateCreate, CandidateResponse
from app.models.candidate import Candidate
from app.api.deps import get_db

router = APIRouter(prefix="/candidates", tags=["Candidates"])


# Create Candidate
@router.post("/", response_model=CandidateResponse)
def create_candidate(data: CandidateCreate, db: Session = Depends(get_db)):
    candidate = Candidate(**data.dict())
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    return candidate


# Get All Candidates
@router.get("/", response_model=list[CandidateResponse])
def get_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()