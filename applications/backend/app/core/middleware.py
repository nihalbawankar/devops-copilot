import time
import logging

from fastapi import Request

logger = logging.getLogger("app")


async def log_requests(request: Request, call_next):
    start_time = time.perf_counter()

    try:
        response = await call_next(request)

        duration = (time.perf_counter() - start_time) * 1000

        logger.info(
            "%s %s | %s | %.2f ms",
            request.method,
            request.url.path,
            response.status_code,
            duration,
        )

        return response

    except Exception:
        duration = (time.perf_counter() - start_time) * 1000

        logger.exception(
            "%s %s | 500 | %.2f ms",
            request.method,
            request.url.path,
            duration,
        )

        raise
