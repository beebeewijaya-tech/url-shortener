import html

from fastapi import APIRouter, Request, Depends

from controllers import url as url_controller
from managers.auth import oauth2_scheme
from schema.url_shorten import UrlShorten

router = APIRouter(
    prefix="/dashboard",
    tags=["dashboard"],
    dependencies=[Depends(oauth2_scheme)]
)


@router.get("/list")
async def dashboard_list(req: Request):
    settings = req.get("state")["settings"]
    templates = req.get("state")["templates"]
    u_session = req.cookies.get('u_session')
    user = req.state.user
    list_url = await url_controller.list_url_by_session(u_session, user)
    do_spaces_url = f"{settings.spaces_bucket_url}/{settings.spaces_bucket_name}"

    data = []
    for i in list_url:
        data.append({
            "title": i.title,
            "short_url": i.short_url,
            "long_url": i.long_url,
            "id": i.id,
            "image_url": i.image_url
        })
    return templates.TemplateResponse(
        request=req, name="dashboard.html", context={
            "list_url": data,
            "do_spaces_url": do_spaces_url
        }
    )


@router.get("/create")
async def dashboard_create(req: Request):
    templates = req.get("state")["templates"]

    return templates.TemplateResponse(
        request=req, name="create.html"
    )


@router.post("/create")
async def dashboard_create(body: UrlShorten, req: Request):
    settings = req.get("state")["settings"]
    u_session = req.cookies.get('u_session')
    user = req.state.user

    return await url_controller.create_url({
        "long_url": html.escape(body.url),
        "session": u_session,
        "image_url": body.image_url,
        "title": body.title,
    }, settings, user)


@router.delete("/delete/{id}")
async def dashboard_create(id: str):
    return await url_controller.delete_url(int(id))
