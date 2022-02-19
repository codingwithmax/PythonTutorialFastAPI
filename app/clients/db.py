from typing import Optional, Union

from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine import Row
from sqlalchemy.sql.expression import Select, Delete, Insert

from app.config import Config


class DatabaseClient:
    def __init__(self, config: Config, tables: Optional[list[str]]):
        self.config = config
        self.engine = create_engine(self.config.host, future=True)
        self.metadata = MetaData(self.engine)
        self._reflect_metadata()  # metadata.tables["user"]
        if tables:  # does not trigger if tables is None, or len(tables) == 0
            self._set_internal_database_tables(tables)

        self.database = Database(self.config.host)

    def _reflect_metadata(self) -> None:
        self.metadata.reflect()

    async def connect(self):
        await self.database.connect()

    async def disconnect(self):
        await self.database.disconnect()

    def _set_internal_database_tables(self, tables: list[str]):
        # e.g. sets DatabaseClient.user = DatabaseClient.metadata.tables["user"] if "user" in tables
        for table in tables:
            setattr(self, table, self.metadata.tables[table])

    async def get_first(self, query: Union[Select, Insert]) -> Optional[Row]:
        async with self.database.transaction():
            res = await self.database.fetch_one(query)
        return res

    async def get_all(self, query: Select) -> list[Row]:
        async with self.database.transaction():
            res = await self.database.fetch_all(query)
        return res

    async def get_paginated(self, query: Select, limit: int, offset: int) -> list[Row]:
        query = query.limit(limit).offset(offset)
        return await self.get_all(query)

    async def execute_in_transaction(self, query: Delete):
        async with self.database.transaction():
            await self.database.execute(query)
