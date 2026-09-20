from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.land_record import LandRecord
from app.models.audit_log import AuditLog
from app.schemas.land_record import LandRecordCreate, LandRecordUpdate, LandRecordOut

router = APIRouter(prefix="/land-records", tags=["land-records"])


@router.post("", response_model=LandRecordOut, status_code=201)
def create_land_record(payload: LandRecordCreate, db: Session = Depends(get_db)):
    record = LandRecord(**payload.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)

    db.add(AuditLog(
        entity_type="LandRecord",
        entity_id=record.id,
        action="created",
        data_snapshot=payload.model_dump(),
    ))
    db.commit()

    return record


@router.get("", response_model=list[LandRecordOut])
def list_land_records(db: Session = Depends(get_db)):
    return db.query(LandRecord).all()


@router.get("/{record_id}", response_model=LandRecordOut)
def get_land_record(record_id: int, db: Session = Depends(get_db)):
    record = db.get(LandRecord, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Land record not found")
    return record


@router.patch("/{record_id}", response_model=LandRecordOut)
def update_land_record(record_id: int, payload: LandRecordUpdate, db: Session = Depends(get_db)):
    record = db.get(LandRecord, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Land record not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(record, field, value)

    db.commit()
    db.refresh(record)

    db.add(AuditLog(
        entity_type="LandRecord",
        entity_id=record.id,
        action="updated",
        data_snapshot=payload.model_dump(exclude_unset=True),
    ))
    db.commit()

    return record
