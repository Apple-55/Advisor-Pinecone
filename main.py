from fastapi import FastAPI
from app.settings import settings

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/config")
def config():
    return {"env": settings.ENV, "api_key_set": settings.API_KEY is not None}

@app.get("/settings")
def get_settings():
    masked = None
    if settings.API_KEY:
        masked = f"{settings.API_KEY[:4]}***{len(settings.API_KEY)}"
    return {
        "env": settings.ENV,
        "api_key_present": settings.API_KEY is not None,
        "api_key_masked": masked,
    }
