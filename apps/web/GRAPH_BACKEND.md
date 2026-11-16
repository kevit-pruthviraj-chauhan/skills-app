# Graph Backend Connection

This frontend was generated with a Python FastAPI backend.

- Backend directory: `apps/server`
- Base URL: `http://localhost:8000`
- Health URL: `http://localhost:8000/health`
- Start command: `cd apps/server && uv run uvicorn app.main:app --reload --host 0.0.0.0 --port ${PORT:-8000}`

The frontend environment file contains the matching public server URL. Keep that value aligned if you change the backend port.
