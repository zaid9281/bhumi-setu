from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.correction import Correction
from app.models.land_record import LandRecord
from app.models.user import User
from app.schemas.correction import CorrectionCreate, CorrectionOut

router = APIRouter(prefix="/corrections", tags=["corrections"])


@router.post("", response_model=CorrectionOut, status_code=201)
def log_correction(payload: CorrectionCreate, db: Session = Depends(get_db)):
    if not db.get(LandRecord, payload.land_record_id):
        raise HTTPException(status_code=404, detail="Land record not found")
    if not db.get(User, payload.corrected_by):
        raise HTTPException(status_code=404, detail="User not found")

    correction = Correction(**payload.model_dump())
    db.add(correction)
    db.commit()
    db.refresh(correction)
    return correction


@router.get("", response_model=list[CorrectionOut])
def list_corrections(db: Session = Depends(get_db)):
    return db.query(Correction).all()
