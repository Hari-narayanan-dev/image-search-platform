# from backend import app
from app.config.settings import settings
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.exceptions.auth import EmailAlreadyExistsError
from app.schemas.auth import (
    LoginRequest,
    Token,
)

router = APIRouter(
    prefix=settings.prefix,
    tags=["Authentication"],
)


@router.post(
    "/signup",
    response_model=UserResponse,
    status_code=201,
)
def signup(
    user: UserCreate,
    db: Session = Depends(get_db),
):

    return AuthService.register_user(
        db=db,
        user=user,
    )

@router.post(
    "/login",
    response_model=Token,
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db),
):

    return AuthService.login_user(
        db=db,
        email=credentials.email,
        password=credentials.password,
    )