# BHUMI-SETU — Architectural Decisions

Each entry: decision, reason, date (if known), alternatives considered
(if known). Where the reason wasn't explicitly stated, it's marked
inferred or unknown rather than invented.

---

### Full Python backend (FastAPI), not hybrid Node/Python
- **Reason:** keep the whole ML/OCR ecosystem native and consistent —
  no cross-language bridging needed between the API layer and
  HuggingFace/PyTorch/OpenCV
- **Alternatives considered:** hybrid Node/Express + Python microservice —
  explicitly considered and rejected
- **Date:** original project planning, before Phase 0 build began

### React (Vite) for frontend
- **Reason:** standard web app choice; users (clerks, verifiers, district
  officers) work at desks with scanners, need real screen space — a
  browser-based web app fits better than mobile/native
- **Alternatives considered:** none recorded
- **Date:** original project planning

### PostgreSQL + PostGIS as the database
- **Reason:** relational integrity for ownership/mutation chains, plus
  native geo support for cadastral data (used starting Phase 8)
- **Alternatives considered:** none recorded
- **Date:** original project planning

### Redis + Celery for the task queue
- **Reason:** decouples slow OCR/ML work from the request-response cycle;
  queue-based rather than request-blocking
- **Alternatives considered:** none recorded
- **Date:** original project planning

### Keycloak for auth/RBAC
- **Reason:** real role-based access control (Clerk/Verifier/District
  Officer/Admin), per-district data scoping, audit-friendly, SSO-ready
- **Alternatives considered:** none recorded
- **Date:** original project planning
- **Status:** container is in the stack; integration is Phase 7, not done

### Object storage: switched from `minio/minio` to `pgsty/silo`
- **Reason:** the official `minio/minio` Docker Hub image was archived
  (April 2026) and pull attempts returned "repository does not exist."
  `pgsty/silo` is the actively maintained successor fork, a drop-in
  replacement using the same `MINIO_ROOT_USER`/`MINIO_ROOT_PASSWORD` env
  vars and the same S3 API
- **Alternatives considered:** `bitnami/minio` was identified as another
  option but not used
- **Date:** during Phase 0 build, when the original image failed to pull

### `docker-compose.yml` — removed the `version:` key
- **Reason:** Docker Compose reported it as obsolete; harmless but
  unnecessary in current Compose versions
- **Date:** during Phase 0 build

### Vercel serverless — rejected
- **Reason:** doesn't fit ML/OCR workloads, which need sustained compute
  and no execution time limits
- **Date:** original project planning

### OCR provider abstraction layer (interface, not hardcoded)
- **Reason:** Google Document AI used for development (best accuracy,
  fastest to build against), but the interface is designed so a
  self-hosted engine (PaddleOCR or fine-tuned TrOCR/LayoutLMv3) can be
  swapped in for real government deployment with zero application-code
  changes — directly answers a real data-sovereignty deployment blocker
  for citizen-PII systems
- **Alternatives considered:** hardcoding directly to Document AI —
  rejected for the sovereignty reason above
- **Date:** original project planning
- **Status:** planned for Phase 2, not yet implemented in code

### Hash-chained audit log (custom), not a blockchain platform
- **Reason:** tamper-evidence for verified land records without the
  overhead of a full blockchain
- **Date:** original project planning
- **Status:** table columns (`prev_hash`, `entry_hash`) exist since Phase
  1; actual chaining logic is Phase 8, not yet implemented

### Free hosting target: Oracle Cloud Always Free VM (for later deployment)
- **Reason:** as of the research done during this project, Render's free
  tier doesn't support background workers and its free Postgres expires
  after 30 days; Railway's free credit lapses after ~30 days; Fly.io
  dropped free tier for new signups. Oracle Cloud's Always Free Arm VM
  was identified as the only option that runs the *entire* docker-compose
  stack (including Celery worker and Keycloak) continuously at no cost
- **Alternatives considered:** split free tiers (Neon for Postgres,
  Upstash for Redis, Render free for the API) — viable for the web-facing
  pieces only, not the background worker or Keycloak
- **Date:** researched during Phase 0 discussion; not yet acted on —
  deployment itself is Phase 10
