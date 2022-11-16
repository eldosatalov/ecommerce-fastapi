from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import get_settings
from app.models import Base

settings = get_settings()

class AsyncDatabaseSession:
    def __getattr__(self, name):
        return getattr(self._session, name)

    def __init__(self):
        self._engine = create_async_engine(
            settings.DB_CONFIG,
            future=True,
        )
        self._session = sessionmaker(
            self._engine, expire_on_commit=False, class_=AsyncSession
        )()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


db = AsyncDatabaseSession()
