from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Recruitment API"
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    GROQ_API_KEY: str
    GEMINI_API_KEY: str
    # Future use
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    MODEL_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()