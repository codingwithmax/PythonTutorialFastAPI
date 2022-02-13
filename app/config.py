from pydantic import BaseSettings, PostgresDsn


class Config(BaseSettings):
    host: PostgresDsn

    class Config:
        env_prefix = "db_"
