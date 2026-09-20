from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime, JSON, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class AuditLog(Base):
    """
    One row per meaningful action on any entity. prev_hash/entry_hash exist
    now so Phase 8 can add real hash-chaining without a schema migration —
    they stay null until then.
    """
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    entity_type: Mapped[str] = mapped_column(String(50))   # "LandRecord", "Document", ...
    entity_id: Mapped[int] = mapped_column(Integer)
    action: Mapped[str] = mapped_column(String(50))        # "created", "updated", "verified", ...
    performed_by: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    data_snapshot: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    prev_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)   # Phase 8
    entry_hash: Mapped[str | None] = mapped_column(String(64), nullable=True)  # Phase 8

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    performed_by_user: Mapped["User"] = relationship()
