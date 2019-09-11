import cv2
import mimetypes


def get_video_w_h(file):
    """Returns image's width and height

    :param file: path to video
    :return: width, height
    """
    vid = cv2.VideoCapture(file)
    height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    return width, height


def is_video(file):
    mime = mimetypes.guess_type(file)[0]
    return mime in ['video/x-msvideo', 'video/mpeg', 'video/quicktime', 'video/x-sgi-movie', 'video/mp4',
                    'video/quicktime', 'video/webm']
