from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.analyze import router as analyze_router
from app.api.health import router as health_router
from app.core.config import settings
from app.core.exceptions import DevOpsCopilotException
from app.core.handlers import (
    devops_exception_handler,
    generic_exception_handler,
)
from app.core.logging import setup_logging
from app.core.middleware import log_requests

logger = setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("DevOps Copilot is starting...")
    yield
    logger.info( "DevOps Copilot is shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,

)
# Middleware
app.middleware("http")(log_requests)

# Exception Handlers
app.add_exception_handler(
    DevOpsCopilotException,
    devops_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

# Routers
app.include_router(health_router)
app.include_router(analyze_router)


@app.get("/", tags=["Root"])
async def root():

    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }
