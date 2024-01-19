from sqlalchemy import Table, Column, String, Integer, DateTime, func, ForeignKey

from db.conn import db

url = Table(
    "urls",
    db.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, index=True),
    Column("short_url", String(200), index=True, nullable=False),
    Column("long_url", String(500), index=True, nullable=False),
    Column("session", String(150)),
    Column("image_url", String(500)),
    Column("title", String(200), nullable=False),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
    Column("user_id", ForeignKey("users.id"), nullable=False),
)
