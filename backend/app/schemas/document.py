from datetime import datetime
from pydantic import BaseModel
from app.models.document import DocumentStatus


class DocumentOut(BaseModel):
    id: int
    original_filename: str
    storage_path: str
    mime_type: str
    status: DocumentStatus
    district: str | None
    uploaded_by: int
    uploaded_at: datetime

    class Config:
        from_attributes = True
