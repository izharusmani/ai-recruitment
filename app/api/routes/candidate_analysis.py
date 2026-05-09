from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.candidate_analysis import CandidateAnalysis
from app.schemas.candidate_analysis import CandidateAnalysisSchema
from app.api.deps import get_db

router = APIRouter(prefix="/candidate-analysis", tags=["Candidate Analysis"])

@router.get("/", response_model=list[CandidateAnalysisSchema])
def get_candidate_analyses(db: Session = Depends(get_db)):
    return db.query(CandidateAnalysis).all()

@router.post("/", response_model=CandidateAnalysisSchema)
def create_candidate_analysis(
    analysis: CandidateAnalysisSchema,
    db: Session = Depends(get_db)
):
    db_analysis = CandidateAnalysis(**analysis.dict())

    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)

    return db_analysis