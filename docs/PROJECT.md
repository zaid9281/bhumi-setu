# BHUMI-SETU — Project Overview

## What it is

BHUMI-SETU (भू-सेतु — "Land Bridge") is an AI-powered system for digitizing
and validating legacy land records — ownership records, survey/khasra/khata
numbers, plot area, mutation history — that currently exist only as
handwritten registers, faded scans, legacy PDFs, or cadastral maps.

Built for **SIH26018** (Smart India Hackathon 2026), under the Ministry of
Rural Development. Official theme listed in the catalogue: MedTech /
BioTech / HealthTech (a catalogue quirk, not a data error — used as-is).

## The problem

- Manual digitization of land records is slow, expensive, and error-prone —
  a mistyped survey number can cause a real ownership dispute later
- No unified system validates extracted data, scores its own confidence, or
  keeps a tamper-proof history of changes
- Foreign-hosted AI APIs raise real data-sovereignty concerns for sensitive
  citizen ownership data — a genuine government deployment blocker
- The problem statement itself acknowledges 100% automation isn't
  realistic — it asks for confidence scoring and human-assisted
  verification, not perfect handwriting recognition

## Goals

Take a scanned/legacy land document in, produce verified structured
audit-safe data out, with humans only reviewing the parts the system is
genuinely unsure about.

## Intended users / roles

- **Clerk** — uploads documents
- **Verifier** — reviews low-confidence extracted fields
- **District Officer** — oversees district-level records/progress
- **Admin** — full system access

(Role-based access via Keycloak is **planned**, not yet implemented — see
`docs/ARCHITECTURE.md`.)

## Major features (confirmed scope)

1. Document upload → preprocessing → OCR → structured field extraction
2. Per-field confidence scoring
3. Automatic validation + duplicate detection
4. Human review queue for low-confidence fields only
5. Full audit trail, tamper-evident via hash chaining
6. Dashboard: documents processed, accuracy, pending review, district
   progress
7. Integration-ready (mocked) APIs for LRMS/DILRMP/GIS

**Status:** items 1 (partially — upload only so far) and the data layer
underneath all of them are implemented. Items 2–7 are **planned**, not yet
built. See `docs/PROGRESS.md` for exact current state.

## Technology stack (finalized, confirmed)

| Layer | Choice |
|---|---|
| Backend | Python + FastAPI |
| Frontend | React (Vite) |
| Database | PostgreSQL + PostGIS |
| Task queue | Celery + Redis |
| Object storage | MinIO-compatible (`pgsty/silo` image — see `docs/DECISIONS.md`) |
| Auth / RBAC | Keycloak (running in the stack, **not yet wired into the app**) |
| Audit trail | Custom hash-chained log table (**schema exists, chaining logic not yet implemented**) |
| Deployment | Docker + docker-compose (Kubernetes-ready planned) |
| CI/CD | GitHub Actions |

Full reasoning for each choice is in `docs/DECISIONS.md`.

## OCR strategy

Built behind a **provider abstraction layer** (not yet implemented in
code — planned for Phase 2): Google Document AI for development (best
accuracy, fastest to build against), with the architecture designed to
swap in a self-hosted engine (PaddleOCR or fine-tuned TrOCR/LayoutLMv3) for
real government deployment, with zero application-code changes elsewhere.
This directly addresses the data-sovereignty concern above.

## AI/ML strategy

- **Field extraction:** LayoutLMv3 (fine-tuned) + IndicNER/IndicBERT for
  layout-aware, Indian-language-aware structured extraction — **planned**,
  Phase 3
- **Correction-driven retraining:** every human correction in the review
  queue gets logged (the `corrections` table already exists — see
  `docs/API.md`); a scheduled job will periodically retrain the extraction
  model on this data — **planned**, Phase 9
- **Scoping decision:** not claiming to solve messy/handwritten OCR
  perfectly. The system aims to be excellent at typed/printed legacy
  documents, honest about handwriting uncertainty, and smart about
  *which* records need a human look.

## Current project scope

As of this document: **Phase 0 and Phase 1 of an 11-phase roadmap are
complete.** The system currently has a working Docker environment and a
functioning backend data layer (models, CRUD, file upload) with no OCR, no
ML, no auth enforcement, and no frontend beyond a health-check page yet.
See `docs/PROGRESS.md` for the authoritative current state.
