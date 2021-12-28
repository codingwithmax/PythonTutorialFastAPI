from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The Username",
        description="This is the username of the user",
        min_length=1,
        default=None
    )
    liked_posts: list[int] = Field(
        description="Array of post ids the user liked",
    )


class FullUserProfile(User):
    short_description: str
    long_bio: str


class CreateUserResponse(BaseModel):
    user_id: int


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


def get_user_info(user_id: int = 0) -> FullUserProfile:

    profile_info = profile_infos[user_id]

    user_content = users_content[user_id]

    user = User(**user_content)

    full_user_profile = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**full_user_profile)


def create_user(full_profile_info: FullUserProfile) -> int:
    global profile_infos
    global users_content

    new_user_id = len(profile_infos)
    liked_posts = full_profile_info.liked_posts
    short_description = full_profile_info.short_description
    long_bio = full_profile_info.long_bio

    print("before:")
    print("users_content:", users_content)
    print("profile_infos:", profile_infos)

    users_content[new_user_id] = {"liked_posts": liked_posts}
    profile_infos[new_user_id] = {
        "short_description": short_description,
        "long_bio": long_bio
    }
    print("after:")
    print("users_content:", users_content)
    print("profile_infos:", profile_infos)
    return new_user_id


@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():
    full_user_profile = get_user_info()

    return full_user_profile


@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: int):

    full_user_profile = get_user_info(user_id)

    return full_user_profile


@app.post("/users", response_model=CreateUserResponse)
def add_user(full_profile_info: FullUserProfile):
    user_id = create_user(full_profile_info)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user
