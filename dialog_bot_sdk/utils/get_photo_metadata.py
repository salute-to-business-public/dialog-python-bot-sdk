from PIL import Image
import io


def get_photo_w_h(file):
    im = Image.open(file)
    return im.size


def get_photo_thumb_bytes(file):
    size = 90, 90

    im = Image.open(file)
    im = im.convert('RGB')
    im.thumbnail(get_photo_w_h(file))
    stream = io.BytesIO()
    im.save(stream, "JPEG")

    return size[0], size[1], stream.getvalue()
