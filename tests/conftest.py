import pytest
from app.schemas.user import FullUserProfile


@pytest.fixture(scope="session")
def valid_user_id() -> int:
    return 0


@pytest.fixture(scope="session")
def invalid_user_delete_id() -> int:
    return 1


@pytest.fixture(scope="session")
def sample_full_user_profile() -> FullUserProfile:
    return FullUserProfile(short_description='short descr',
                           long_bio='def',
                           username='abc',
                           liked_posts=[1, 2, 3])
