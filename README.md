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
