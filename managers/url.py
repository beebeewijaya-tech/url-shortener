from db.conn import db
from models.url import url


class UrlManager:
    @staticmethod
    async def get_url_by_session(session, user):
        query = "SELECT * FROM urls WHERE session = :session OR user_id = :user_id"
        ex = await db.database.fetch_all(query=query, values={"session": session, "user_id": user.id})
        return ex

    @staticmethod
    async def create_url(payload, user):
        query = url.insert().values(
            long_url=payload["long_url"],
            session=payload["session"],
            image_url=payload["image_url"],
            title=payload["title"],
            short_url=payload["short_url"],
            user_id=user.id
        )
        _id = await db.database.execute(query)
        ex = await db.database.fetch_one(url.select().where(url.c.id == _id))
        return ex

    @staticmethod
    async def delete_url(id):
        query = url.delete().where(url.c.id == id)
        ex = await db.database.execute(query)
        return ex

    @staticmethod
    async def get_url_by_short(short):
        query = "SELECT * FROM urls WHERE short_url = :short"
        ex = await db.database.fetch_one(query=query, values={"short": short})
        return ex
