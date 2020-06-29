import pyqrcode
import random
from PIL import Image, ImageDraw

def text_to_qr(url, filename, *, scale=500, quality=100):
    qr = pyqrcode.create(url).text().splitlines()

    width = len(qr[0])
    height = len(qr)

    im = Image.new(mode='RGB', size=(width, height))
    draw = ImageDraw.Draw(im)

    colors = [150, 255]

    for y in range(height):
        for x in range(width):
            dot = int(qr[y][x])
            color = tuple([dot * random.randint(151, 255) for i in range(3)])
            draw.point(
                xy=(x, y),
                fill=color
                )
    im = im.resize((scale, scale))
    im.save('qr.jpg', quality=quality)


text_to_qr(
    'hi',
    filename='qr.jpg'
    )
