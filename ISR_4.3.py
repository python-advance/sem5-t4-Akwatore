import pyqrcode
import random
from PIL import Image, ImageDraw

def text_to_qr(url, filename, *, scale=500, quality=100):
    result = pyqrcode.create(url).text().splitlines()

    width = len(result[0])
    height = len(result)

    im = Image.new(mode='RGB', size=(width, height))
    draw = ImageDraw.Draw(im)

    colors = [127, 255]

    for y in range(height):
        for x in range(width):
            dot = int(result[y][x])
            color = tuple([dot * random.randint(128, 255) for i in range(3)])
            draw.point(
                xy=(x, y),
                fill=color
                )
    im = im.resize((scale, scale))
    im.save('result.jpg', quality=quality)


text_to_qr(
    'haha pyqrcode go brrr | pls dont yoink the code i wrote it myself @3am',
    filename='result.jpg'
    )
