import uuid

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.storage import upload_file, get_file_url
from app.models.document import Document, DocumentStatus
from app.models.user import User
from app.models.audit_log import AuditLog
from app.schemas.document import DocumentOut

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("/upload", response_model=DocumentOut, status_code=201)
async def upload_document(
    file: UploadFile = File(...),
    uploaded_by: int = Form(...),
    district: str | None = Form(None),
    db: Session = Depends(get_db),
):
    user = db.get(User, uploaded_by)
    if not user:
        raise HTTPException(status_code=404, detail="uploaded_by user not found")

    contents = await file.read()
    object_key = f"documents/{uuid.uuid4()}_{file.filename}"
    upload_file(object_key, contents, file.content_type or "application/octet-stream")

    document = Document(
        original_filename=file.filename,
        storage_path=object_key,
        mime_type=file.content_type or "application/octet-stream",
        status=DocumentStatus.UPLOADED,
        district=district,
        uploaded_by=uploaded_by,
    )
    db.add(document)
    db.commit()
    db.refresh(document)

    db.add(AuditLog(
        entity_type="Document",
        entity_id=document.id,
        action="uploaded",
        performed_by=uploaded_by,
        data_snapshot={"filename": file.filename, "status": document.status.value},
    ))
    db.commit()

    return document


@router.get("", response_model=list[DocumentOut])
def list_documents(db: Session = Depends(get_db)):
    return db.query(Document).all()


@router.get("/{document_id}", response_model=DocumentOut)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.get("/{document_id}/download-url")
def get_document_download_url(document_id: int, db: Session = Depends(get_db)):
    document = db.get(Document, document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"url": get_file_url(document.storage_path)}
