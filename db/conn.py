from databases import Database
from sqlalchemy import MetaData

from utils.settings import Settings


class DatabaseConnection:
    database = None
    metadata = None

    def __init__(self, settings: Settings):
        db_url = f"postgresql://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

        self.database = Database(db_url)
        self.metadata = MetaData()

    async def connect(self):
        await self.database.connect()

    async def disconnect(self):
        await self.database.disconnect()


settings = Settings()
db = DatabaseConnection(settings)
