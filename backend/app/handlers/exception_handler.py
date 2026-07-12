from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions.auth import (
    EmailAlreadyExistsError,
    InvalidCredentialsError,
)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all application exception handlers.
    """

    @app.exception_handler(EmailAlreadyExistsError)
    async def email_exists_handler(
        request: Request,
        exc: EmailAlreadyExistsError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": str(exc)
            },
        )

    @app.exception_handler(InvalidCredentialsError)
    async def invalid_credentials_handler(
        request: Request,
        exc: InvalidCredentialsError,
    ):
        return JSONResponse(
            status_code=401,
            content={
                "detail": str(exc),
            },
        )