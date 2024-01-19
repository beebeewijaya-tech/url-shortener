from fastapi import HTTPException
from starlette.responses import JSONResponse

from managers.auth import AuthManager
from managers.user import UserManager
from schema.user import User
from utils.password import get_password_hash, verify_password


async def create_user(user: User):
    try:
        user.password = get_password_hash(user.password)
        response = await UserManager.create_user(user)
        return response
    except Exception as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})


async def login_user(user: User):
    try:
        response = await UserManager.get_user(user)
        if not response:
            raise HTTPException(400, "user not found")
        elif not verify_password(user.password, response.password):
            raise HTTPException(400, "incorrect password")

        token = AuthManager.generate_token(response)

        return {
            "token": token
        }
    except Exception as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})
