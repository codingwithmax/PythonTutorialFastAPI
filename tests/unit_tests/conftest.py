import pytest
from pydantic import BaseModel
from sqlalchemy import create_engine

from app.services.user import UserService
from app.config import Config
from app.clients.db import DatabaseClient
from models import recreate_tables
from models.base import engine

import pytest_asyncio
from app.schemas.user import FullUserProfile


class SQliteConfig(BaseModel):
    host: str


class SQLiteDatabaseClient(DatabaseClient):
    def __init__(self, sqlite_config: SQliteConfig):
        temp_engine = create_engine(sqlite_config.host)
        recreate_tables(temp_engine)
        super(SQLiteDatabaseClient, self).__init__(sqlite_config, tables=["user", "liked_post"])


@pytest.fixture
def _profile_infos():
    val = {
        0: {
            "short_description": "My bio description",
            "long_bio": "This is our longer bio"
        }
    }
    return val


@pytest.fixture
def _users_content():
    val = {
        0: {
            "liked_posts": [1] * 9,
        }
    }
    return val


@pytest.fixture(scope="session")
def sample_full_user_profile() -> FullUserProfile:
    return FullUserProfile(short_description='short descr',
                           long_bio='def',
                           name='abc',
                           liked_posts=[1, 2, 3])


@pytest.fixture(scope="session")
def testing_config() -> Config:
    return Config()


@pytest.fixture(scope="session")
def sqlite_testing_config() -> SQliteConfig:
    host = "sqlite:///testing.db"
    return SQliteConfig(host=host)


@pytest_asyncio.fixture
async def testing_db_client(testing_config) -> DatabaseClient:
    recreate_tables(engine)
    database_client = DatabaseClient(testing_config, ["user", "liked_post"])
    await database_client.connect()
    yield database_client
    await database_client.disconnect()


@pytest_asyncio.fixture
async def sqlite_testing_db_client(sqlite_testing_config) -> SQLiteDatabaseClient:
    database_client = SQLiteDatabaseClient(sqlite_testing_config)
    return database_client


@pytest.fixture
def user_service(testing_db_client):
    user_service = UserService(testing_db_client)
    return user_service


@pytest.fixture
def sqlite_user_service(sqlite_testing_db_client):
    user_service = UserService(sqlite_testing_db_client)
    return user_service
