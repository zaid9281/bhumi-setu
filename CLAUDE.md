# Instructions for AI Coding Assistants

This file applies to any AI working on this repository — Claude, ChatGPT,
Cursor, Copilot, Gemini, or anything else. Read it before making any
non-trivial change.

## Before you do anything

1. Read `docs/HANDOFF.md` first — it tells you exactly where the project
   left off and what the next task is.
2. Read `docs/PROGRESS.md` and `docs/ARCHITECTURE.md` to understand what's
   actually built vs. what's still planned.
3. **Inspect the real code before assuming anything.** Docs can drift out
   of date. If a doc and the code disagree, the code is correct — flag the
   mismatch and fix the doc.
4. **Do not change the existing architecture** (tech stack, folder
   structure, service boundaries) without an explicit reason and without
   saying so clearly before doing it. See `docs/DECISIONS.md` for why things
   are the way they are.
5. **Do not invent features, endpoints, or fields that aren't asked for.**
   If something seems missing, say so — don't silently add it.
6. **Do not introduce new technologies or dependencies** outside what
   `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` already establish, unless
   explicitly asked.
7. **Follow the phase order** in `docs/TODO.md`. Later phases assume earlier
   ones exist — don't jump ahead.
8. **Test what you change.** For this project that means: does
   `docker compose up` still start cleanly, does `/health` still return
   `"ok"`, do the relevant endpoints in `/docs` (FastAPI Swagger UI) still
   work as expected.

## After meaningful work

Update, in the same session:
- `docs/PROGRESS.md` — mark what's actually done (tested, not just written)
- `docs/API.md` — add/update any endpoint you touched
- `docs/HANDOFF.md` — rewrite it to reflect the new current state, so the
  *next* session (any AI, any tool) picks up correctly
- `docs/DECISIONS.md` — if you made or changed an architectural call

**Do not mark something as done unless it has actually been implemented
and run/tested** — not just written. Distinguish clearly between
IMPLEMENTED, PARTIALLY IMPLEMENTED, and PLANNED wherever you write status.

## Source of truth

The codebase is the source of truth, not this documentation and not any
chat history. If they conflict, trust the code, then fix the docs.
