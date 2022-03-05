import logging

import aioredis

from app.config import Config

logger = logging.getLogger(__name__)


class RedisCache:
    user_prefix = "user"

    def __init__(self, config: Config, ttl: int = 60 * 60):
        self._host = config.redis_host
        self.redis = aioredis.from_url(self._host, decode_responses=True, db=0)
        self.ttl = ttl

    async def get(self, key, prefix):
        try:
            storage_key = f"{prefix}:{key}"
            val = await self.redis.get(storage_key)
            return val
        except Exception as e:
            logger.error(f"Encountered error {str(e)} when trying to read: {storage_key}")
        return

    async def set(self, key, value, prefix):
        try:
            storage_key = f"{prefix}:{key}"
            await self.redis.set(storage_key, value, ex=self.ttl)
        except Exception as e:
            logger.error(f"Encountered error {str(e)} when trying to save: {value} to {storage_key}")
        return

    async def delete(self, *args, prefix):
        prefixed_args = [f"{prefix}:{key}" for key in args]
        await self.redis.delete(*prefixed_args)
        return
