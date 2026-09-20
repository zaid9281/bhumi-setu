from datetime import datetime
from pydantic import BaseModel


class AuditLogOut(BaseModel):
    id: int
    entity_type: str
    entity_id: int
    action: str
    performed_by: int | None
    data_snapshot: dict | None
    created_at: datetime

    class Config:
        from_attributes = True
