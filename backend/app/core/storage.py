"""
MinIO (S3-compatible) client wrapper. Document files are stored here,
separate from structured data in Postgres, per Section 5 of the README.
"""

import io
from datetime import timedelta

from minio import Minio

from app.core.config import settings

_client = Minio(
    settings.minio_endpoint,
    access_key=settings.minio_access_key,
    secret_key=settings.minio_secret_key,
    secure=settings.minio_secure,
)


def ensure_bucket_exists() -> None:
    if not _client.bucket_exists(settings.minio_bucket):
        _client.make_bucket(settings.minio_bucket)


def upload_file(object_name: str, data: bytes, content_type: str) -> str:
    """Uploads bytes under object_name. Returns object_name (the storage_path)."""
    ensure_bucket_exists()
    _client.put_object(
        settings.minio_bucket,
        object_name,
        data=io.BytesIO(data),
        length=len(data),
        content_type=content_type,
    )
    return object_name


def get_file_url(object_name: str, expires_seconds: int = 3600) -> str:
    """Temporary presigned URL to view/download the file."""
    return _client.presigned_get_object(
        settings.minio_bucket, object_name, expires=timedelta(seconds=expires_seconds)
    )
