from fastapi import APIRouter

from app.core.exceptions import DevOpsCopilotException

router = APIRouter(tags=["Analyze"])


@router.get("/analyze")
async def analyze():
    raise DevOpsCopilotException(
        "Analyze service not implemented yet",
        status_code=501,
    )
