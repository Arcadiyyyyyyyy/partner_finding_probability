from fastapi import APIRouter
from ._models.server_time import ServerTime


router = APIRouter(prefix="/general", tags=["General"])


@router.get("/server_time")
async def server_time() -> ServerTime:
    return ServerTime()
