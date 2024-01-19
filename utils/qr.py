import io

import segno
from colorthief import ColorThief


def get_main_color(file):
    colors = ColorThief(file)
    palette = colors.get_palette(color_count=5, quality=1)

    return palette


async def generate_qr(file, long_url, output_url):
    file_open = await file.read()
    file_bytes = io.BytesIO(file_open)
    qrcode = segno.make_qr(long_url)
    color = get_main_color(file_bytes)

    qrcode.to_artistic(
        background=file_bytes,
        target=output_url,
        scale=20,
        border=1,
        dark=color[0],
        light="#faf3e1",
    )
