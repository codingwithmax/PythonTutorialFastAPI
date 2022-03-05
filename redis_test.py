import asyncio

import aioredis

redis = aioredis.from_url(
    "redis://localhost",
    encoding="utf-8",
    decode_responses=True,
    db=1,
)


async def test_get(key):
    val = await redis.get(key)

    print("key:", key, "val:", val, "value type:", type(val))


async def test_set_and_then_get(key, value):
    await redis.set(key, value, ex=1)
    await asyncio.sleep(0.5)
    await redis.set(key, value)
    await asyncio.sleep(0.6)
    await test_get(key)
    await asyncio.sleep(1)

    # await redis.delete(key)
    #
    await test_get(key)

# asyncio.run(test_get("test"))
asyncio.run(test_set_and_then_get("test", 3))