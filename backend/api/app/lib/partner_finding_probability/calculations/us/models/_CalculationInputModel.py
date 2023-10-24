from typing import Tuple

from app.lib.models import BaseCalculationInputModel


class CalculationInputModel(BaseCalculationInputModel):
    minimum_yearly_income: int
    exclude_maried: bool
    body_fat_range: Tuple[float, float]
    age_range: Tuple[int, int]
    height_range: Tuple[float, float]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "gender": "male",
                    "sexual_orientation": "gay",
                    "minimum_yearly_income": 100000,
                    "exclude_maried": True,
                    "body_fat_range": (8.5, 12.5),
                    "age_range": (18, 25),
                    "height_range": (6.2, 6.5),
                },
            ]
        }
    }
