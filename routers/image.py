from fastapi import APIRouter, Request, UploadFile

from controllers.image import upload_image

router = APIRouter(
    prefix="/image",
    tags=["image"]
)


@router.post("/create")
async def image_post(file: UploadFile, url: str, req: Request):
    settings = req.get("state")["settings"]

    return await upload_image(file, url, settings)
