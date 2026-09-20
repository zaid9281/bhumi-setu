# BHUMI-SETU — Progress Tracker

**Last updated:** end of Phase 1 build session
**Current phase:** Between Phase 1 and Phase 2

## Completed (implemented AND verified working)

### Phase 0 — Environment & Fundamentals
- [x] Docker Compose skeleton: FastAPI backend, React/Vite frontend,
      PostgreSQL+PostGIS, Redis, object storage (pgsty/silo), Keycloak
      (dev mode), Celery worker — all start via `docker compose up --build`
- [x] `GET /health` checks real DB and Redis connectivity, confirmed
      returning `"status": "ok"`
- [x] Frontend fetches `/health` on load and displays it, confirmed working
- [x] Basic GitHub Actions CI (backend import check + compose validation)
- **Verified by user:** yes — ran locally, confirmed both `/health` and
  the frontend page showed green status

### Phase 1 — Backend Core
- [x] SQLAlchemy models: `User`, `Document`, `LandRecord`, `Correction`,
      `AuditLog`
- [x] Pydantic schemas for all 5 models
- [x] Alembic configured; initial migration generated and applied
      (`alembic upgrade head` run successfully)
- [x] CRUD endpoints for users, documents, land records, corrections
      (create/list only), audit logs (list only) — see `docs/API.md`
- [x] File upload to object storage via `POST /documents/upload`
- **Verified by user:** yes — user confirmed they completed every step
  exactly as instructed

## Currently being worked on

- Setting up repo-level cross-AI documentation (this file and its
  siblings) so the project isn't dependent on any single AI chat's memory

## Next immediate task

**Phase 2 — OCR Pipeline.** Build the OCR provider abstraction interface,
integrate Google Document AI behind it (dev provider), add OpenCV
preprocessing (deskew/denoise/contrast), and wire up:
upload → preprocess → OCR → raw text + key-value pairs stored against the
`Document` record. Test against real sample documents.

## Not started

Phases 3–11 in full — field extraction/NLP, async processing via Celery,
validation/confidence scoring/review workflow, frontend beyond the health
page, Keycloak integration, hash-chained audit trail, correction-driven
retraining, deployment beyond local Docker, and final testing/polish.
See `docs/TODO.md` for the full breakdown.
