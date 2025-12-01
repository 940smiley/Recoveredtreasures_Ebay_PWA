# eBay Seller Dashboard (Local, PWA)

Local-only dashboard to manage inventory, drafts, and listings with future AI-assisted features. Accessible from your iPhone over LAN.

## Run
- Backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`
- Frontend: `cd frontend && python -m http.server 5173`
- Open: `http://<PC_IP>:5173` (frontend) which calls `http://<PC_IP>:8000` via same host (served by http.server). If cross-origin blocks, open `http://localhost:5173` on PC.

## Configure
- Copy `backend/.env.example` to `backend/.env` and fill when ready (AnythingLLM, eBay IDs).

## Notes
- Zero-cost: SQLite planned for persistence; current scaffold keeps in-memory runs.
- Next steps: file upload API, SQLite models, jobs (hotness), real eBay OAuth.

---

## Dependency Map (auto-generated)
- **Backend (FastAPI + SQLModel):** fastapi, uvicorn[standard], sqlmodel, pydantic, python-multipart, apscheduler, httpx, python-dotenv
- **Frontend (static HTML/JS):** vanilla HTML/CSS/JS served via `python -m http.server` with service worker manifest
- **Tooling:** none required beyond Python 3.11+, git, and a modern browser

## Feature Overview & Component Summary
- **AI model router (`backend/app/routes/ai.py`):** exposes `/api/ai/models` and `/api/ai/generate` with configurable parameters for each model option.
- **AI service core (`backend/app/services/ai.py`):** registry-driven model selection, parameter merging, and context-aware synthetic generation.
- **AI schemas (`backend/app/models/ai.py`):** shared Pydantic models for model metadata, parameter overrides, and structured responses.
- **Existing flows:** uploads/drafts, hotness scoring, pricing stubs, and settings management continue to operate as before.

## Installation & Setup (auto-detected)
1. **Backend:**
   - `cd backend`
   - `python -m venv .venv && source .venv/bin/activate`
   - `pip install -r requirements.txt`
   - `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload`
2. **Frontend:**
   - `cd frontend`
   - `python -m http.server 5173`
3. **Environment:** copy `backend/.env.example` to `backend/.env` and set `ANYTHINGLLM_BASE_URL`, `ANYTHINGLLM_API_KEY`, and eBay credentials when available.

## Contribution Guidelines
- Branch from `main`, name branches descriptively (e.g., `feature/ai-routing`).
- Keep code formatted and typed where applicable; prefer small, reviewable commits.
- Add or update tests alongside features and run the full suite before opening a PR.
- Document API additions in the README or dedicated docs as they land.

## GitHub Pages
- No Pages site is published yet; enable Pages on the repository using the `main` branch or a `/docs` folder build.
- For static docs, mirror the frontend build (or add generated docs) under `/docs` to publish automatically via GitHub Pages.

## Last enhanced by Codex
- Updated: 2025-12-01 06:06 UTC
