import json
import logging

from fastapi import APIRouter, Depends

from app.schemas.user import (
    CreateUserResponse,
    FullUserProfile,
    MultipleUsersResponse,
)
from app.services.user import UserService
from app.dependencies import rate_limit
from app.clients.db import DatabaseClient
from app.clients.redis import RedisCache

logger = logging.getLogger(__name__)


def create_user_router(database_client: DatabaseClient, redis_cache: RedisCache) -> APIRouter:
    user_router = APIRouter(
        prefix="/user",
        tags=["user"],
        dependencies=[Depends(rate_limit)]
    )
    user_service = UserService(database_client)

    @user_router.get("/all", response_model=MultipleUsersResponse)
    async def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users

    @user_router.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id(user_id: int):
        full_user_profile_str = await redis_cache.get(user_id, redis_cache.user_prefix)
        if full_user_profile_str:
            full_user_profile = FullUserProfile(**json.loads(full_user_profile_str))
            return full_user_profile

        full_user_profile = await user_service.get_user_info(user_id)
        await redis_cache.set(user_id, full_user_profile.json(), redis_cache.user_prefix)

        return full_user_profile

    @user_router.put("/{user_id}", response_model=CreateUserResponse)
    async def update_user(user_id: int, full_profile_info: FullUserProfile) -> int:
        user_id = await user_service.create_update_user(full_profile_info, user_id)
        await redis_cache.set(user_id, full_profile_info.json(), redis_cache.user_prefix)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    @user_router.delete("/{user_id}")
    async def remove_user(user_id: int):

        await user_service.delete_user(user_id)
        await redis_cache.delete(user_id, prefix=redis_cache.user_prefix)

    @user_router.post("/", response_model=CreateUserResponse, status_code=201)
    async def add_user(full_profile_info: FullUserProfile):
        user_id = await user_service.create_user(full_profile_info)
        await redis_cache.set(user_id, full_profile_info.json(), redis_cache.user_prefix)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    @user_router.on_event("startup")
    async def startup():
        await database_client.connect()

    @user_router.on_event("shutdown")
    async def shutdown():
        await database_client.disconnect()

    return user_router
