from app.lib.models import MainModel
from typing import Dict


class ServerTime(MainModel):
    data: Dict[str, str] = {"ping": "pong"}
