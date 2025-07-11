#!/bin/bash
echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting FastAPI app on port 8001..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
