import contextlib
import tempfile
from typing import Union, IO

import OpenSSL
import requests
from dialog_api import media_and_files_pb2

from dialog_bot_sdk.entities.media_and_files import FileLocation
from dialog_bot_sdk.entities.messaging import DocumentMessage
from dialog_bot_sdk.utils import async_dec


class Downloading(object):
    """Class for high-level file downloading interface.

    """
    def __init__(self, internal):
        self.internal = internal

    @async_dec()
    def download_file(self, file_path: str, document: DocumentMessage, path_to_pfx: str = None, password: str = None,
                      verify: bool = False) -> \
            Union[IO[bytes], IO]:
        file_id = document.file_id
        access_hash = document.access_hash
        location = FileLocation(file_id, access_hash)
        url = self.__get_file_url(location)
        f = open(file_path, 'wb')

        if path_to_pfx is not None and password is not None:
            with self.__pfx_to_pem(path_to_pfx, bytes(password, "UTF-8")) as cert:
                self.__request_for_url(f, url, cert, verify)
        else:
            self.__request_for_url(f, url, verify=verify)

        return f

    def download_file_sync(self, file_path: str, document: DocumentMessage, path_to_pfx: str = None,
                           password: str = None, verify=False) -> Union[IO[bytes], IO]:
        return self.download_file.__wrapped__(self, file_path, document, path_to_pfx, password, verify)

    @staticmethod
    @contextlib.contextmanager
    def __pfx_to_pem(pfx_path, pfx_password):
        with tempfile.NamedTemporaryFile(suffix='.pem') as t_pem:
            f_pem = open(t_pem.name, 'wb')
            pfx = open(pfx_path, 'rb').read()
            p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)
            f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
            f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))
            ca = p12.get_ca_certificates()

            if ca is not None:
                for cert in ca:
                    f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))

            f_pem.close()
            yield t_pem.name

    def __get_file_url(self, location: FileLocation) -> str:
        request = media_and_files_pb2.RequestGetFileUrl(
            file=location.to_api()
        )
        return self.internal.media_and_files.GetFileUrl(request).url

    @staticmethod
    def __request_for_url(file, url, cert=None, verify=False) -> None:
        ufr = requests.get(url, cert=cert, verify=verify)
        if ufr.status_code != 200 and ufr.status_code != 302:
            file.close()
            raise Exception("File download response with code error %s" % ufr.status_code)

        with open(file.name, 'wb') as f:
            for chunk in ufr.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
