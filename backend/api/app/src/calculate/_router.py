from fastapi import APIRouter
from .partner_finding_probability import partner_finding_probability_router


router = APIRouter(
    prefix="/calculate",
    tags=["Calculate"]
)
router.include_router(partner_finding_probability_router)
