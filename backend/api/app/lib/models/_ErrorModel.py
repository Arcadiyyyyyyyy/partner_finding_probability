from typing import Any, Dict
from pydantic import BaseModel


class ErrorModel(BaseModel):
    code: int = 404
    extended: Dict[str, Any] = {}
