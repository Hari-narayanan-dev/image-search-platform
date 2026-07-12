from app.schemas.auth import Token
from sqlalchemy.orm import Session
from app.config.security import hash_password, create_access_token, verify_password
from app.models.user import User
from app.schemas.user import UserCreate
from app.exceptions.auth import EmailAlreadyExistsError,InvalidCredentialsError



class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user: UserCreate,
    ) -> User:

        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise EmailAlreadyExistsError()

        db_user = User(
            full_name=user.full_name,
            email=user.email,
            hashed_password=hash_password(
                user.password
            ),
        )

        db.add(db_user)

        db.commit()

        db.refresh(db_user)

        return db_user
    
    @staticmethod
    def login_user(
        db: Session,
        email: str,
        password: str,
    ):

        user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if not user:
            raise InvalidCredentialsError()

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise InvalidCredentialsError()

        access_token = create_access_token(
            {
                "sub": user.email,
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )