from db.conn import db
from models.user import user
from schema.user import User


class UserManager:
    @staticmethod
    async def create_user(u: User):
        query = user.insert().values(**u.dict())
        _id = await db.database.execute(query)
        _u = await db.database.fetch_one(user.select().where(user.c.id == _id))
        return _u

    @staticmethod
    async def get_user(u: User):
        query = user.select().where(user.c.email == u.email)
        _u = await db.database.fetch_one(query)
        return _u
