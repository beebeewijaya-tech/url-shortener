from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from controllers import url as url_controller

router = APIRouter(
    tags=["general"]
)


@router.get("/ping")
def ping():
    return "PONG!"


@router.get("/")
async def get_home(req: Request):
    templates = req.get("state")["templates"]

    return templates.TemplateResponse(
        request=req, name="home.html"
    )


@router.get("/{short}")
async def get_url_page(req: Request, short: str):
    settings = req.get("state")["settings"]
    short_url = f"{settings.host}/{short}"

    url_by_short = await url_controller.list_url_by_short_url(short_url)

    if url_by_short is not None:
        long_url = url_by_short.long_url
        if long_url.find("https://") == -1:
            long_url = f"https://{long_url}"

        return RedirectResponse(
            url=long_url,
            status_code=302
        )
