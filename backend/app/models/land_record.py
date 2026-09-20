from datetime import datetime

from sqlalchemy import String, Float, ForeignKey, DateTime, JSON, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class LandRecord(Base):
    __tablename__ = "land_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int | None] = mapped_column(ForeignKey("documents.id"), nullable=True)

    landowner_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    survey_number: Mapped[str | None] = mapped_column(String(100), nullable=True)
    khasra_number: Mapped[str | None] = mapped_column(String(100), nullable=True)
    khata_number: Mapped[str | None] = mapped_column(String(100), nullable=True)
    village: Mapped[str | None] = mapped_column(String(150), nullable=True)
    tehsil: Mapped[str | None] = mapped_column(String(150), nullable=True)
    district: Mapped[str | None] = mapped_column(String(150), nullable=True)
    plot_area: Mapped[float | None] = mapped_column(Float, nullable=True)
    plot_area_unit: Mapped[str | None] = mapped_column(String(20), nullable=True)  # "acres" / "hectares"
    land_classification: Mapped[str | None] = mapped_column(String(100), nullable=True)

    mutation_records: Mapped[list | None] = mapped_column(JSON, nullable=True)
    field_confidence: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # Phase 3 populates this

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    document: Mapped["Document"] = relationship(back_populates="land_records")
    corrections: Mapped[list["Correction"]] = relationship(back_populates="land_record")
