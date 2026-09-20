from datetime import datetime
from pydantic import BaseModel


class LandRecordCreate(BaseModel):
    document_id: int | None = None
    landowner_name: str | None = None
    survey_number: str | None = None
    khasra_number: str | None = None
    khata_number: str | None = None
    village: str | None = None
    tehsil: str | None = None
    district: str | None = None
    plot_area: float | None = None
    plot_area_unit: str | None = None
    land_classification: str | None = None
    mutation_records: list | None = None


class LandRecordUpdate(LandRecordCreate):
    pass


class LandRecordOut(LandRecordCreate):
    id: int
    field_confidence: dict | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
