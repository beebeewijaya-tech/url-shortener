from contextlib import asynccontextmanager
from functools import lru_cache

import uvicorn
from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db.conn import db
from routers.dashboard import router as dashboard_route
from routers.general import router as general_route
from routers.image import router as image_route
from routers.user import router as user_route
from utils.settings import Settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield

    # Clean up the ML models and release the resources
    await db.disconnect()


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")


@lru_cache
def get_settings(req: Request):
    settings = Settings()
    req.state.settings = settings
    return settings


@lru_cache
def load_jinja_template(req: Request):
    templates = Jinja2Templates(directory="templates")
    req.state.templates = templates
    return templates


app.include_router(general_route, dependencies=[Depends(get_settings), Depends(load_jinja_template)])
app.include_router(dashboard_route, dependencies=[Depends(get_settings), Depends(load_jinja_template)])
app.include_router(image_route, dependencies=[Depends(get_settings)])
app.include_router(user_route, dependencies=[Depends(get_settings), Depends(load_jinja_template)])

if __name__ == "__main__":
    uvicorn.run("main:app", port=3000, reload=True)
