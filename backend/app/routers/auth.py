from backend import app
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.exceptions.auth import EmailAlreadyExistsError

router = APIRouter(
    prefix="/api/v1/auth",
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

    try:
        return AuthService.register_user(
            db=db,
            user=user,
        )
    except EmailAlreadyExistsError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )