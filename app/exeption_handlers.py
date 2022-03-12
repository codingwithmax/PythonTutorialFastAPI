from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions import UserNotFound, UserAlreadyExists
import logging
from sqlalchemy.exc import IntegrityError


logger = logging.getLogger(__name__)


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(UserNotFound)
    async def handle_user_not_found_exception(request: Request, exc: UserNotFound):
        logger.error(f"Non-existent user_id: {exc.user_id} was requested")
        return JSONResponse(status_code=404, content="User doesn't exist")

    @app.exception_handler(UserAlreadyExists)
    async def handle_user_already_exists_exception(request: Request, exc: UserAlreadyExists):
        logger.error(f"Tried to insert user that already exists")
        return JSONResponse(status_code=400, content="User already exist")

    @app.exception_handler(IntegrityError)
    async def handle_integrity_error_exception(request: Request, exc: IntegrityError):
        logger.error(f"Encountered integrity error when inserting user: {str(exc)}")
        return JSONResponse(status_code=400, content="User conflicts with existing user")

    return None
