from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.job_description import JobDescription
from app.api.deps import get_db
from app.schemas.job import JobCreate

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/")
def create_job(data: JobCreate, db: Session = Depends(get_db)):
    job = JobDescription(**data.dict())
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@router.get("/")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(JobDescription).all()