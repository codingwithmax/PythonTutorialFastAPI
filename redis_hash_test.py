import asyncio
import aioredis

redis = aioredis.from_url("redis://localhost")

# users key:value user2:value key3:value key4:value


async def test_hash():
    name = "test_some_hash"
    await redis.hset(name, mapping={"key1": "value1", "key2": "value2", "key3": "value3"})
    print(await redis.hmget(name, ["key1", "key2"]))
    # await redis.hdel(name, "key1", "key3")
    print(await redis.hgetall(name))
    # print(await redis.hexists(name, "key4"))
    # for i in range(1, 7):
    #     print(await redis.exists(f"user:{i}"))
    print(await redis.hsetnx(name, "key4", "value2"))
    print(await redis.hgetall(name))
    await redis.expire(name, 1)
    await asyncio.sleep(1)
    print(await redis.hgetall(name))


asyncio.run(test_hash())
