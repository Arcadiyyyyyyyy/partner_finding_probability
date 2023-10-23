from datetime import datetime
from typing import Any, Dict
from pydantic import BaseModel

from app.lib.models._ErrorModel import ErrorModel


class MainModel(BaseModel):
    data: Dict[str, Any] = {}
    error: ErrorModel | None = None
    server_time: int = int(datetime.utcnow().timestamp() * 1000)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "data": {},
                    "error": None,
                    "server_time": 1698091830128,
                },
            ]
        }
    }
