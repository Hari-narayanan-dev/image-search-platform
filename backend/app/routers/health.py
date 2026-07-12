from fastapi import APIRouter

from app.config.settings import settings

router = APIRouter(
    tags=["Health"]
)


@router.get("/")
def root():
    return {
        "message": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }