from fastapi import FastAPI
import os

app = FastAPI()

VERSION = os.getenv("APP_VERSION", "0.2.0")

@app.get("/")
def root():
    return {"message": "Hello from K8s Interview App! v4 🚀", "version": VERSION}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/version")
def version():
    return {"version": VERSION, "env": "dev"}