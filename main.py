from fastapi import FastAPI
from app.routes.user import create_user_router


def create_application() -> FastAPI:
    user_router = create_user_router()

    app = FastAPI()
    app.include_router(user_router)
    return app


app = create_application()
