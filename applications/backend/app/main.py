from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 DevOps Copilot is starting...")
    yield
    print("🛑 DevOps Copilot is shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(health_router)


@app.get("/", tags=["Root"])
async def root():
    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }
