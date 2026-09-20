from fastapi import APIRouter
from sqlalchemy import text
import redis

from app.core.config import settings
from app.db.session import engine

router = APIRouter()


@router.get("/health")
def health_check():
    status = {"status": "ok", "environment": settings.environment}

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        status["database"] = "ok"
    except Exception as exc:
        status["status"] = "degraded"
        status["database"] = f"error: {exc}"

    try:
        r = redis.Redis.from_url(settings.redis_url)
        r.ping()
        status["redis"] = "ok"
    except Exception as exc:
        status["status"] = "degraded"
        status["redis"] = f"error: {exc}"

    return status
