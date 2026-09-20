"""
Central app configuration. Everything reads from env vars via .env.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    environment: str = "development"
    debug: bool = True
    secret_key: str = "change-me-to-a-long-random-string"

    database_url: str = "postgresql+psycopg://bhusetu:change-me@db:5432/bhusetu"
    redis_url: str = "redis://redis:6379/0"

    minio_endpoint: str = "minio:9000"
    minio_access_key: str = "change-me"
    minio_secret_key: str = "change-me"
    minio_bucket: str = "bhusetu-documents"
    minio_secure: bool = False

    ocr_provider: str = "document_ai"

    keycloak_url: str = ""
    keycloak_realm: str = "bhusetu"
    keycloak_client_id: str = ""


settings = Settings()
