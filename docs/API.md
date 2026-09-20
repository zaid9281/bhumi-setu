# BHUMI-SETU — API Reference (as implemented)

**Base URL (local dev):** `http://localhost:8000`
**Authentication:** none implemented on any endpoint yet — Keycloak
integration is Phase 7. Every route below is currently open.

---

## Health

### `GET /health`
Checks real database and Redis connectivity.
**Response 200:**
```json
{"status": "ok", "environment": "development", "database": "ok", "redis": "ok"}
```
`status` is `"degraded"` if either dependency fails, with the specific
error under `database` or `redis`.

### `GET /`
Returns basic project/phase info. No parameters.

---

## Users

### `POST /users`
Create a user.
**Request body:**
```json
{"username": "string", "email": "user@example.com", "full_name": "string",
 "role": "clerk | verifier | district_officer | admin", "district": "string | null"}
```
`role` defaults to `"clerk"` if omitted. Returns **409** if username or
email already exists.
**Response 201:** the created user object (includes `id`).

### `GET /users`
Lists all users. No pagination implemented yet.

### `GET /users/{user_id}`
Returns one user by id. **404** if not found.

---

## Documents

### `POST /documents/upload`
Multipart form upload.
**Form fields:** `file` (the file), `uploaded_by` (int, must be an
existing user id), `district` (optional string).
Uploads the raw file to object storage, creates a `Document` row with
`status: "uploaded"`, and logs an `AuditLog` entry with `action: "uploaded"`.
**Response 201:** the created document object.
**404** if `uploaded_by` doesn't match an existing user.

### `GET /documents`
Lists all documents.

### `GET /documents/{document_id}`
Returns one document by id. **404** if not found.

### `GET /documents/{document_id}/download-url`
Returns a temporary (1 hour) presigned URL to the stored file:
```json
{"url": "https://..."}
```

---

## Land Records

### `POST /land-records`
Create a land record.
**Request body (all fields except relations are optional):**
```json
{
  "document_id": 1,
  "landowner_name": "string",
  "survey_number": "string",
  "khasra_number": "string",
  "khata_number": "string",
  "village": "string",
  "tehsil": "string",
  "district": "string",
  "plot_area": 0.0,
  "plot_area_unit": "acres | hectares",
  "land_classification": "string",
  "mutation_records": []
}
```
Logs an `AuditLog` entry with `action: "created"`.
**Response 201:** the created record, including `id`, `field_confidence`
(null until Phase 3 populates it), `created_at`, `updated_at`.

### `GET /land-records`
Lists all land records.

### `GET /land-records/{record_id}`
Returns one record by id. **404** if not found.

### `PATCH /land-records/{record_id}`
Partial update — send only the fields you want to change. Logs an
`AuditLog` entry with `action: "updated"` containing only the changed
fields. **Note:** this does NOT yet write to the `corrections` table
(that wiring is Phase 5) — it's a direct edit, not a tracked correction.

---

## Corrections

### `POST /corrections`
Manually log a correction record.
**Request body:**
```json
{"land_record_id": 1, "field_name": "string", "old_value": "string | null",
 "new_value": "string | null", "corrected_by": 1}
```
**404** if `land_record_id` or `corrected_by` don't exist.
**Note:** nothing in the system calls this automatically yet — no review
UI or diffing logic exists. This endpoint exists so the table/contract is
ready for Phase 5.

### `GET /corrections`
Lists all corrections.

---

## Audit Logs

### `GET /audit-logs`
Lists all audit log entries, most recent first. Each entry:
```json
{"id": 1, "entity_type": "string", "entity_id": 1, "action": "string",
 "performed_by": 1, "data_snapshot": {}, "created_at": "..."}
```
`prev_hash`/`entry_hash` exist on the underlying table but are not
returned or populated yet — hash-chaining is Phase 8.

---

## Not yet implemented (do not assume these exist)

- No DELETE endpoint on any resource
- No pagination or filtering on any list endpoint
- No authentication/authorization on any route
- No OCR/extraction endpoints (Phase 2)
- No status-transition endpoint for documents (`pending → processing → ...`)
  — Phase 4
