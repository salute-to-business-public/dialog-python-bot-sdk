from PIL import Image
import mimetypes
import io


def get_image_w_h(file):
    """Returns image's width and height

    :param file: path to image
    :return: (width, height) tuple
    """

    im = Image.open(file)
    return im.size


def get_image_thumb_bytes(file):
    """Returns image's thumbnail in form of byte array

    :param file: path to image
    :return: size and byte array
    """

    size = 90, 90

    im = Image.open(file)
    im = im.convert('RGB')
    im.thumbnail(size)
    stream = io.BytesIO()
    im.save(stream, "JPEG")

    return size[0], size[1], stream.getvalue()


def is_image(file):
    mime = mimetypes.guess_type(file)[0]
    return mime in ['image/jpeg', 'image/png', 'image/gif', 'image/bmp']
