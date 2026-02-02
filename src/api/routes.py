from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import FileResponse
from sse_starlette.sse import EventSourceResponse

from src.components.sse.service import event_creator
from src.core.config import STATIC_DIR

router = APIRouter()

@router.get("/")
async def index():
    return FileResponse(STATIC_DIR / "index.html")

@router.get("/flow")
async def flow(request: Request):
    return EventSourceResponse(event_creator(request))