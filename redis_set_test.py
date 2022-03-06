import asyncio
import aioredis

redis = aioredis.from_url("redis://localhost")


async def test_set():
    await redis.sadd("some_set", "val1", "val2", "val3", "val4")
    await redis.sadd("some_set", "val1", "val2")
    await redis.srem("some_set", "val1")
    print(await redis.smembers("some_set"))

    await redis.sadd("some_other_set", "val4", "val5", "val3", "val6")
    print(await redis.smembers("some_other_set"))

    print(await redis.sinter(["some_set", "some_other_set"]))
    print(await redis.sunion(["some_set", "some_other_set"]))

asyncio.run(test_set())
