# BHUMI-SETU — Roadmap

Checkboxes reflect actual implemented-and-tested status, not just written
code. See `docs/PROGRESS.md` for narrative detail.

## Completed

### Phase 0 — Environment & Fundamentals
- [x] Docker + docker-compose skeleton (all 7 services)
- [x] Health check endpoint (real DB/Redis checks)
- [x] Frontend smoke-test page
- [x] Basic CI (GitHub Actions)

### Phase 1 — Backend Core
- [x] Data models: User, Document, LandRecord, Correction, AuditLog
- [x] Alembic migrations set up and applied
- [x] CRUD endpoints for all 5 models (create/list/get; update on
      LandRecord)
- [x] File upload to object storage

## Currently working on

- [ ] Repo-level documentation (`CLAUDE.md` + `docs/`) for cross-AI/session
      continuity

## Next (Phase 2 — OCR Pipeline)

- [ ] Define the OCR provider abstraction interface
- [ ] Implement Google Document AI as the dev-time provider behind it
- [ ] OpenCV preprocessing: deskew, denoise, contrast adjustment
- [ ] Wire upload → preprocess → OCR → store raw text/key-value pairs on
      `Document`
- [ ] Test against real sample documents

## Future phases (planned, not started)

### Phase 3 — Field Extraction & NLP
- [ ] HuggingFace Transformers setup
- [ ] LayoutLMv3 fine-tuning (label 50–100 sample records)
- [ ] IndicNER integration
- [ ] Field-extraction service: OCR output + image → structured JSON with
      per-field confidence

### Phase 4 — Async Processing
- [ ] Move OCR + extraction onto Celery/Redis (currently just a stub task)
- [ ] Status endpoint: pending → processing → needs_review → verified

### Phase 5 — Validation, Confidence Scoring, Review Workflow
- [ ] Confidence-threshold routing
- [ ] Rule-based validation
- [ ] Fuzzy duplicate detection (rapidfuzz)
- [ ] Wire the existing `corrections` table into an actual review flow

### Phase 6 — Frontend
- [ ] Real dashboard
- [ ] Upload UI
- [ ] Review/correction queue UI
- [ ] Leaflet GIS map view

### Phase 7 — Auth & Security
- [ ] Keycloak realms/clients/roles
- [ ] OIDC into FastAPI + React
- [ ] Role-based access enforcement (Clerk/Verifier/District Officer/Admin)
- [ ] Audit-log attribution tied to real authenticated users

### Phase 8 — Hash-Chained Audit Trail, GIS, Integration Stubs
- [ ] Implement actual hash-chaining on `audit_logs.prev_hash`/`entry_hash`
      (columns already exist, unused)
- [ ] PostGIS geometry fields on `LandRecord`
- [ ] Mock LRMS/DILRMP/GIS integration endpoints

### Phase 9 — Correction-Driven Retraining
- [ ] Scheduled job fine-tuning the extraction model on accumulated
      `corrections` data

### Phase 10 — Deployment
- [ ] Move beyond local Docker Compose to a real host (see
      `docs/DECISIONS.md` for hosting research already done)
- [ ] Separate dev/staging/prod configs

### Phase 11 — Testing, Real Accuracy Numbers, Polish
- [ ] Run full sample document set through the pipeline
- [ ] Record real accuracy metrics
- [ ] Fix edge cases, finish documentation, demo video, PPT
