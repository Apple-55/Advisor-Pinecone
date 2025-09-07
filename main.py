from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv(override=True)  # force-read .env
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/config")
def config():
    return {
        "env": os.getenv("ENV", "dev"),
        "api_key_set": bool(os.getenv("API_KEY")),
    }
