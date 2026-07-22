from fastapi import APIRouter
import logging

router = APIRouter(tags=["Health"])

logger = logging.getLogger("app")


@router.get("/health")
async def health():


    return {
        "status": "healthy"
    }
