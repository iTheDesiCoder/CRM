from fastapi import Request
from .main import app
from .common.Logging import logger
from .contoller import task_router
from app.common.Logging.RequestContext import RequestContext

app.include_router(task_router)


@app.middleware("http")
async def log_request(request: Request, call_next):
    headers = request.headers
    RequestContext.headers.set(dict(headers))
    response = await call_next(request)
    return response

# Expose main components at the package level (optional, depending on your preference)
#__all__ = ["app", "logger"]
