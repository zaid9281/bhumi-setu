# BHUMI-SETU — Session Handoff

**Update this file at the end of every real work session**, so the next
session (any AI, any tool) can pick up correctly without re-reading full
chat history.

---

## What we were doing

Building BHUMI-SETU for SIH26018 step-by-step, phase by phase, with the
project owner implementing each step by hand from provided instructions
(not via AI-generated file drops) and pushing to GitHub themselves.

## Completed in the latest session

- Phase 0 (Docker skeleton) — built and confirmed working
- Phase 1 (backend core: models, CRUD, migrations, file upload) — built
  and confirmed working, exactly as instructed
- Fixed a real-world break: `minio/minio` Docker image was archived
  upstream; swapped to `pgsty/silo` (see `docs/DECISIONS.md`)
- Project renamed from `bhu-setu` to `bhumi-setu`
- Set up this documentation set (`CLAUDE.md` + `docs/`) so the project
  doesn't depend on any single AI chat's memory

## Currently being worked on

Nothing mid-flight — Phase 1 is a clean stopping point. Documentation was
just completed.

## Current blockers / errors

None open. (Historical note: the `minio/minio` pull failure above was
resolved, not an open issue.)

## Exact next step

**Start Phase 2 — OCR Pipeline:**
1. Design the OCR provider abstraction interface (a small Python
   interface/base class that any OCR provider implements)
2. Implement Google Document AI as the first (dev) provider behind it
3. Add OpenCV preprocessing (deskew, denoise, contrast) before OCR runs
4. Wire it into the existing `Document` flow: after upload, run
   preprocess → OCR → store raw text + key-value pairs against the
   `Document` record (new fields/table needed — not designed yet)
5. Test against real sample documents

Before starting, whoever picks this up (AI or human) should read
`docs/ARCHITECTURE.md`'s "OCR layer" section and `docs/DECISIONS.md`'s
OCR abstraction entry — the interface design is a non-negotiable
requirement from the original project scoping, not optional.
