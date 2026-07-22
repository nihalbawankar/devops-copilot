# ============================================================
# DevOps Copilot - Backend Dockerfile
# Production Ready (Single Stage)
# ============================================================

# ---------- Base Image ----------
FROM python:3.12-slim

# ---------- Metadata ----------
LABEL maintainer="Nihal Bawankar"
LABEL project="DevOps Copilot"
LABEL version="0.1.0"
LABEL description="AI-Powered Self-Healing Kubernetes Platform"

# ---------- Environment ----------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# ---------- Working Directory ----------
WORKDIR /app

# ---------- Install System Packages ----------
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------- Copy Dependency File ----------
COPY requirements.txt .

# ---------- Install Python Dependencies ----------
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ---------- Copy Application ----------
COPY . .

# ---------- Create Non-root User ----------
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app

USER appuser

# ---------- Expose Application Port ----------
EXPOSE 8000

# ---------- Health Check ----------
HEALTHCHECK --interval=30s \
            --timeout=5s \
            --start-period=10s \
            --retries=3 \
CMD curl -f http://localhost:8000/health || exit 1

# ---------- Start Application ----------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
