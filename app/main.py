from fastapi import FastAPI

from app.core.database import Base, engine
from app.models import candidate, job_description, resume

# Import routers
from app.api.routes import candidate as candidate_router
from app.api.routes import job as job_router
from app.api.routes import resume as resume_router
from app.api.routes import agent as agent_router
from app.api.routes.test_upload import router as test_router
from app.api.routes import debug
from app.api.routes import candidate_analysis as candidate_analysis_router

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="AI Recruitment API")

# Include routes
app.include_router(candidate_router.router)
app.include_router(job_router.router)
app.include_router(resume_router.router)
app.include_router(agent_router.router)
app.include_router(test_router)
app.include_router(debug.router)
app.include_router(candidate_analysis_router.router)

# Root endpoint (optional)
@app.get("/")
def root():
    return {"message": "AI Recruitment API is running 🚀"} 