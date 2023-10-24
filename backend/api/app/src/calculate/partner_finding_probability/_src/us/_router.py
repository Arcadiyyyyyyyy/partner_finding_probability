from fastapi import APIRouter
from app.lib.partner_finding_probability.calculations.us.models import CalculationInputModel, CalculationOutputModel


router = APIRouter(prefix="/us")


@router.post("/generate_probability")
async def generate_probability(calculate_on: CalculationInputModel) -> CalculationOutputModel:
    return CalculationOutputModel(data={"value": calculate_on.body_fat_range})
