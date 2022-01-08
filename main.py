from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exeption_handlers import add_exception_handlers


def create_application() -> FastAPI:
    user_router = create_user_router()

    app = FastAPI()
    app.include_router(user_router)
    add_exception_handlers(app)
    
    return app


app = create_application()
