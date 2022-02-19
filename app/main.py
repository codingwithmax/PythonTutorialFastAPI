from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exeption_handlers import add_exception_handlers
from app.clients.db import DatabaseClient
from app.config import Config


def create_application() -> FastAPI:

    config = Config()
    tables = ["user", "liked_post"]
    database_client = DatabaseClient(config, tables)
    user_router = create_user_router(database_client)

    app = FastAPI()
    app.include_router(user_router)
    add_exception_handlers(app)
    
    return app


app = create_application()
