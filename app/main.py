from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware
from app.configs import settings
from app.utils.logger import logger
from app.user import router as user

logger.critical("Stast app")

app = FastAPI(
    title=settings.APP_PROJECT_NAME,
    description="Demo App",
    # middleware=middlewares,
    docs_url=settings.APP_DOCS_URL,
    openapi_url='/api/openapi.json',
    redoc_url=None
)


for i in (
    {'router':user, "prefix" : "/user"},
):
    app.include_router(
        router = i.get("router"),  # type: ignore
        prefix = i.get("prefix")   # type: ignore
    )

@app.get("/")
async def root():
    return {"message": "Demo App!"}