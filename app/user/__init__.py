from fastapi import APIRouter
from .views.authentication import router as authen

router = APIRouter()

router.include_router(authen)