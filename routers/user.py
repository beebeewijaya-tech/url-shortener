from fastapi import APIRouter, Request

from controllers.user import create_user, login_user
from schema.user import User

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.post("/register")
async def register(user: User):
    return await create_user(user)


@router.post("/login")
async def login(user: User):
    return await login_user(user)


@router.get("/auth")
async def get_auth(req: Request):
    templates = req.get("state")["templates"]

    return templates.TemplateResponse(
        request=req, name="auth.html"
    )
