from typing import Any, Dict, Tuple
from pydantic import BaseModel


class CalculationInputModel(BaseModel):
    minimum_yearly_income: int
    body_fat_range: Tuple[float, float]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "minimum_yearly_income": 100000,
                    "body_fat_range": (8.5, 12.5),
                },
            ]
        }
    }
