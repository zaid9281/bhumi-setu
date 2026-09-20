from datetime import datetime
from pydantic import BaseModel


class CorrectionCreate(BaseModel):
    land_record_id: int
    field_name: str
    old_value: str | None = None
    new_value: str | None = None
    corrected_by: int


class CorrectionOut(CorrectionCreate):
    id: int
    corrected_at: datetime

    class Config:
        from_attributes = True
