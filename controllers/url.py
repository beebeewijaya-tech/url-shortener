from starlette.responses import JSONResponse

from managers.url import UrlManager
from utils.url import build_short_url


async def create_url(payload, settings, user):
    try:
        payload["short_url"] = build_short_url(settings.host, "")
        response = await UrlManager.create_url(payload, user)
        return response
    except Exception as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})


async def list_url_by_session(session, user):
    try:
        response = await UrlManager.get_url_by_session(session, user)
        return response
    except Exception as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})


async def list_url_by_short_url(short):
    try:
        response = await UrlManager.get_url_by_short(short)
        return response
    except Exception as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})


async def delete_url(id):
    try:
        response = await UrlManager.delete_url(id)
        return response
    except Exception as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})
