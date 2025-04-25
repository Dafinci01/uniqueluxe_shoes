from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Uniqluxe Shoes"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    DATABASE_URL: str 
    SECRET_KEY: str 

    class Config:
        env_file = ".env"

settings = Settings()