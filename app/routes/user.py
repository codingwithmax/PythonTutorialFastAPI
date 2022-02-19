from fastapi import APIRouter, Depends
from app.schemas.user import (
    CreateUserResponse,
    FullUserProfile,
    MultipleUsersResponse,
)
from app.services.user import UserService
import logging
from app.dependencies import rate_limit
from app.clients.db import DatabaseClient

logger = logging.getLogger(__name__)


def create_user_router(database_client: DatabaseClient) -> APIRouter:
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

        full_user_profile = await user_service.get_user_info(user_id)

        return full_user_profile

    @user_router.put("/{user_id}")
    async def update_user(user_id: int, full_profile_info: FullUserProfile):
        await user_service.create_update_user(full_profile_info, user_id)
        return None

    @user_router.delete("/{user_id}")
    async def remove_user(user_id: int):

        await user_service.delete_user(user_id)

    @user_router.post("/", response_model=CreateUserResponse, status_code=201)
    async def add_user(full_profile_info: FullUserProfile):
        user_id = await user_service.create_update_user(full_profile_info)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    return user_router
