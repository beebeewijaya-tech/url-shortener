from sqlalchemy import Table, Column, String, Integer, DateTime, func

from db.conn import db

user = Table(
    "users",
    db.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, index=True),
    Column("email", String(200), index=True, unique=True, nullable=False),
    Column("password", String(200), nullable=False),
    Column("fullname", String(150)),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
)
