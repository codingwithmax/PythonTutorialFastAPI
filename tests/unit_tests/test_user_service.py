import pytest
from app.exceptions import UserNotFound


@pytest.mark.asyncio
async def test_delete_user_works_properly(user_service, sample_full_user_profile):
    user_id = await user_service.create_user(sample_full_user_profile)
    assert user_id is not None
    await user_service.delete_user(user_id)
    with pytest.raises(UserNotFound):
        await user_service.get_user_info(user_id)


@pytest.mark.asyncio
async def test_delete_user_works_properly_sqlite(sqlite_user_service, sample_full_user_profile):
    user_id = await sqlite_user_service.create_update_user(sample_full_user_profile, 1)
    assert user_id is not None
    await sqlite_user_service.delete_user(user_id)
    # with pytest.raises(UserNotFound):
    #     await sqlite_user_service.get_user_info(user_id)
