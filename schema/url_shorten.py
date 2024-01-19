import datetime
from typing import Optional

from pydantic import BaseModel


class UrlShorten(BaseModel):
    url: str
    image_url: Optional[str] = ""
    title: str


class UrlShortenResponse(BaseModel):
    id: str
    short_url: str
    long_url: str
    session: str
    image_url: str
    title: str
    created_at: datetime.datetime
    user_id: int
