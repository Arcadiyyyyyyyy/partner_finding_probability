from pydantic import BaseModel
from app.lib.models.Enums import Gender, SexualOrientation


class BaseCalculationInputModel(BaseModel):
    gender: Gender
    sexual_orientation: SexualOrientation
