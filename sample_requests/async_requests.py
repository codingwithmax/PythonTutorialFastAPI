import asyncio
import aiohttp


async def sample_async_get_request(base_url: str, endpoint_prefix: str, user_id: int) -> (int, dict):
    url = f"{base_url}{endpoint_prefix}{user_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            json_response = await response.json()
            status_code = response.status
            return status_code, json_response, response.headers


async def sample_async_post_request():
    sample_data_to_send = {
        "name": "bob",
        "liked_posts": [
            0, 1, 2
        ],
        "short_description": "some short description",
        "long_bio": "some long bio"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("http://127.0.0.1:8000/user/", json=sample_data_to_send) as response:
            print(response.status)
            print(response.headers)
            print(await response.json())


# asyncio.run(sample_async_post_request())
