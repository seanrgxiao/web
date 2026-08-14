from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

import os

app = FastAPI()

# 自动采集 http_requests_total、http_request_duration_seconds 等指标
# 并暴露在 /metrics 端点
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

VERSION = os.getenv("APP_VERSION", "21.1.3")

@app.get("/")
def root():
    return {"message": "Hello from K8s Interview App! v21.1.3 🚀", "version": VERSION}
@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/version")
def version():
    return {"version": VERSION, "env": "dev"}