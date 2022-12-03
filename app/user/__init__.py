from fastapi import APIRouter
from .views.user import router as authen

router = APIRouter()

router.include_router(authen)