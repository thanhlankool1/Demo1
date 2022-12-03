from fastapi import APIRouter
from .views.login import router as login
from .views.user import router as user

router = APIRouter()

router.include_router(user)
router.include_router(login)