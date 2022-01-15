import pytest


@pytest.mark.asyncio
async def test_delete_user_works_properly(user_service):
    user_to_delete = 0
    await user_service.delete_user(user_to_delete)
    assert user_to_delete not in user_service.profile_infos
    assert user_to_delete not in user_service.users_content


# def test_4(testing_fixture):
#     print("testing_fixture:", testing_fixture)
#     assert False
#
# def test_5(testing_fixture):
#     print("testing_fixture:", testing_fixture)
#     assert False
