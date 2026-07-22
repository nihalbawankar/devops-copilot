import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import DevOpsCopilotException

logger = logging.getLogger("app")


async def devops_exception_handler(
    request: Request,
    exc: DevOpsCopilotException,
):
    logger.error(exc.message)

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "message": exc.message,
            },
        },
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception("Unhandled exception")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": {
                "message": "Internal Server Error",
            },
        },
    )
