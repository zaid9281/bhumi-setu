"""
BHUMI-SETU backend entrypoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import health, users, documents, land_records, corrections, audit_logs
from app import models  # noqa: F401 — registers all models on Base.metadata

app = FastAPI(
    title="BHUMI-SETU API",
    description="Intelligent Land Record Digitization & Validation System",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["health"])
app.include_router(users.router)
app.include_router(documents.router)
app.include_router(land_records.router)
app.include_router(corrections.router)
app.include_router(audit_logs.router)


@app.get("/")
def root():
    return {
        "project": "BHUMI-SETU",
        "phase": "1 — backend core",
        "docs": "/docs",
    }
