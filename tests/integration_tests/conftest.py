import pytest
from app.create_app import create_application
from models import recreate_tables
from models.base import engine


@pytest.fixture(scope='session')
def base_testing_app():
    app = create_application()
    recreate_tables(engine)
    return app


@pytest.fixture
def testing_rate_limit() -> int:
    return 50


@pytest.fixture(scope="session")
def sample_full_user_profile() -> dict:
    return dict(short_description='short descr',
                           long_bio='def',
                           name='abc',
                           liked_posts=[1, 2, 3])
