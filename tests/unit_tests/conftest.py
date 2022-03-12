import pytest
from app.services.user import UserService
from app.config import Config
from app.clients.db import DatabaseClient
from models import recreate_postgres_tables
import pytest_asyncio
from app.schemas.user import FullUserProfile
from models import User, LikedPost

from unittest.mock import AsyncMock


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


@pytest_asyncio.fixture
async def testing_db_client(testing_config) -> DatabaseClient:  # type: ignore
    recreate_postgres_tables()
    database_client = DatabaseClient(testing_config, ["user", "liked_post"])
    await database_client.connect()
    yield database_client
    await database_client.disconnect()


@pytest.fixture
def user_service(testing_db_client) -> UserService:
    user_service = UserService(testing_db_client)
    return user_service


@pytest.fixture
def mocking_database_client() -> DatabaseClient:
    def side_effect(*args, **kwargs):
        return (1, )

    mock = AsyncMock()
    mock.user = User.__table__
    mock.liked_post = LikedPost.__table__
    mock.get_first.side_effect = side_effect  # AsyncMock(side_effect=[(1, ), (2, )])
    return mock


@pytest.fixture
def user_service_mocked_db(mocking_database_client: DatabaseClient) -> UserService:
    user_service = UserService(mocking_database_client)
    return user_service
