import pytest
from app.services.user import UserService


@pytest.mark.asyncio
async def test_delete_user_works_properly():
    profile_infos = {
        0: {
            "short_description": "My bio description",
            "long_bio": "This is our longer bio"
        }
    }

    users_content = {
        0: {
            "liked_posts": [1] * 9,
        }
    }

    user_service = UserService(profile_infos, users_content)
    user_to_delete = 0
    await user_service.delete_user(user_to_delete)
    assert user_to_delete not in profile_infos
    assert user_to_delete not in users_content
