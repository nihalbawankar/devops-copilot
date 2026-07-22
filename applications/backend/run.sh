#!/bin/bash

source .venv/bin/activate


echo "Stopping any process using port 8000..."
fuser -k 8000/tcp 2>/dev/null

echo "Starting DevOps Copilot..."
uvicorn app.main:app --reload
