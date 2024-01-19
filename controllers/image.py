import os
import time

from services.do_space import DigitalOceanSpaceService
from utils.qr import generate_qr


async def upload_image(file, long_url, settings):
    do_svc = DigitalOceanSpaceService(settings)
    output_url = f"{file.filename}-{time.time():.0f}.png"
    await generate_qr(file, long_url, output_url)

    with open(output_url, "rb") as output:
        content = output.read()
        do_svc.upload(content, output_url)
        os.remove(output_url)
        return output_url
