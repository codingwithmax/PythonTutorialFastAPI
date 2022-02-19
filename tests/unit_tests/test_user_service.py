import pytest
from app.exceptions import UserNotFound


@pytest.mark.asyncio
async def test_delete_user_works_properly(user_service, sample_full_user_profile):
    user_id = await user_service.create_user(sample_full_user_profile)
    assert user_id is not None
    await user_service.delete_user(user_id)
    with pytest.raises(UserNotFound):
        await user_service.get_user_info(user_id)
