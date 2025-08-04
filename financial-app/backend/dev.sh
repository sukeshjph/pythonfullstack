#!/bin/bash
echo "Starting FastAPI development server..."
./venv/python.exe -m uvicorn books:app --reload --host 0.0.0.0 --port 8000 