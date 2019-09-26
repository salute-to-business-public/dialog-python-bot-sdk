import audioread
import mimetypes


def get_audio_duration(file):
    """Returns audio's duration

    :param file: path to audio
    :return: duration (int)
    """
    audio = audioread.audio_open(file)
    return int(audio.duration)


def is_audio(file):
    mime = mimetypes.guess_type(file)[0]
    return mime in ['audio/x-aiff', 'audio/basic', 'audio/mpeg', 'audio/x-pn-realaudio', 'audio/x-wav', 'audio/midi']
