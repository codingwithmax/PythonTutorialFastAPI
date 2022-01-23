from typing import Optional, Tuple
from app.schemas.user import (
    FullUserProfile,
    User,
)
from app.exceptions import UserNotFound


class UserService:

    def __init__(self, profile_infos: dict, users_content: dict):
        self.profile_infos = profile_infos
        self.users_content = users_content

    async def get_all_users_with_pagination(self, start: int, limit: int) -> Tuple[list[FullUserProfile], int]:
        list_of_users = []
        keys = list(self.profile_infos.keys())
        total = len(keys)
        for index in range(0, len(keys), 1):
            if index < start:
                continue
            current_key = keys[index]
            user = await self.get_user_info(current_key)
            list_of_users.append(user)
            if len(list_of_users) >= limit:
                break

        return list_of_users, total

    async def get_user_info(self, user_id: int = 0) -> FullUserProfile:
        if user_id not in self.profile_infos:
            raise UserNotFound(user_id=user_id)

        profile_info = self.profile_infos[user_id]
        user_content = self.users_content[user_id]

        user = User(**user_content)

        full_user_profile = {
            **profile_info,
            **user.dict()
        }

        return FullUserProfile(**full_user_profile)

    async def create_update_user(self, full_profile_info: FullUserProfile, user_id: Optional[int] = None) -> int:
        if user_id is None:
            user_id = len(self.profile_infos)
        liked_posts = full_profile_info.liked_posts
        short_description = full_profile_info.short_description
        long_bio = full_profile_info.long_bio

        self.users_content[user_id] = {"liked_posts": liked_posts}
        self.profile_infos[user_id] = {
            "short_description": short_description,
            "long_bio": long_bio
        }

        return user_id

    async def delete_user(self, user_id: int) -> None:

        if user_id not in self.profile_infos:
            raise UserNotFound(user_id=user_id)

        del self.profile_infos[user_id]
        del self.users_content[user_id]
