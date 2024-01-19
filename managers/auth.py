from datetime import datetime, timedelta
from typing import Optional, Tuple

import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from db.conn import db
from models.user import user
from schema.user import User
from utils.settings import Settings

settings = Settings()


class AuthManager:
    @staticmethod
    def generate_token(u: User):
        try:
            payload = {
                'sub': u.email,
                "exp": datetime.now() + timedelta(minutes=24 * 60 * 60)
            }
            token = jwt.encode(payload, settings.jwt_secret, algorithm="HS256")
            return token
        except Exception as e:
            raise e


class HTTPCredentials:
    scheme = ""
    credentials = ""

    def __init__(self, token: str):
        self.scheme, self.credentials = self.get_authorization_scheme_param(token)

    def get_authorization_scheme_param(self, token: Optional[str]) -> Tuple[str, str]:
        if not token:
            return "", ""
        scheme, _, param = token.partition(" ")
        return scheme, param


class CustomHTTPBearer(HTTPBearer):
    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        auth = request.cookies.get("u-auth")
        if not auth or "Bearer" not in auth:
            raise HTTPException(401, "empty token")
        res = HTTPCredentials(auth)
        try:
            payload = jwt.decode(res.credentials, settings.jwt_secret, algorithms=["HS256"])
            query = user.select().where(user.c.email == payload["sub"])
            u_data = await db.database.fetch_one(query)
            request.state.user = u_data
            return u_data
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "expired token")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "invalid token")


oauth2_scheme = CustomHTTPBearer()
