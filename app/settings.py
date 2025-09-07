from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENV: str = "dev"
    API_KEY: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()
