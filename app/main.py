import os
from fastapi import FastAPI

app = FastAPI()
VERSION = os.getenv("APP_VERSION", "v1")
COLOR = os.getenv("APP_COLOR", "blue")

@app.get("/")
def root():
    return {"version": VERSION, "color": COLOR, "message": "hello from rollout demo,v1.0"}

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"ready": True}