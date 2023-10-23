from typing import Any, Dict

from app.lib.models import MainModel


class CalculationOutputModel(MainModel):
    data: Dict[Any, Any]
