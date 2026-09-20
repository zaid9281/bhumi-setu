from datetime import datetime

from sqlalchemy import String, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class Correction(Base):
    """
    Every human edit to a LandRecord field. This table exists from Phase 1
    even though no review UI uses it yet — Phase 9's retraining job needs
    this data to exist from day one, not bolted on later.
    """
    __tablename__ = "corrections"

    id: Mapped[int] = mapped_column(primary_key=True)
    land_record_id: Mapped[int] = mapped_column(ForeignKey("land_records.id"))
    field_name: Mapped[str] = mapped_column(String(100))
    old_value: Mapped[str | None] = mapped_column(Text, nullable=True)
    new_value: Mapped[str | None] = mapped_column(Text, nullable=True)
    corrected_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    corrected_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    land_record: Mapped["LandRecord"] = relationship(back_populates="corrections")
    corrected_by_user: Mapped["User"] = relationship(back_populates="corrections")
