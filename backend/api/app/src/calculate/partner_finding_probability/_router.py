from fastapi import APIRouter
from ._src import us_router


router = APIRouter(
    prefix="/partner_finding_probability",
)
router.include_router(us_router)
