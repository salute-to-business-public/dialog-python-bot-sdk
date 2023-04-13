import os
from time import sleep

import requests
from concurrent.futures import ThreadPoolExecutor
from tempfile import NamedTemporaryFile

from requests import HTTPError
from dialog_api import media_and_files_pb2
from dialog_bot_sdk.entities.media_and_files import FileLocation
from dialog_bot_sdk.utils import async_dec, read_file_in_chunks, read_file_content_in_chunks


class Uploading(object):
    """Class for high-level file uploading interface.

    """

    def __init__(self, internal, cert, private_key, access_dir, parallelism=None, retry=None, retry_period=None):
        self.internal = internal
        self.cert = cert
        self.private_key = private_key
        self.access_dir = access_dir
        self.pool = ThreadPoolExecutor(max_workers=parallelism if parallelism is not None else 10)
        self.retry = retry if retry is not None else 0
        self.retry_period = retry_period if retry_period is not None else 0

    @async_dec()
    def upload_file(self, file: str or bytes, max_chunk_size=1024*1024, verify=None):
        """Upload file for sending.

        :param verify:
        :param file: path to file
        :param max_chunk_size: maximum size of one chunk (default 1024 * 1024)
        :return: FileLocation object if success or None otherwise
        """
        req = media_and_files_pb2.RequestGetFileUploadUrl(
            expected_size=os.path.getsize(file) if isinstance(file, str) else len(file)
        )
        upload_key = self.internal.media_and_files.GetFileUploadUrl(req).upload_key
        result = list(
            self.pool.map(
                lambda x: self.__upload_file_chunk(*x),
                (
                    (part_number, chunk, upload_key, self.access_dir, verify) for part_number, chunk in enumerate(
                     read_file_in_chunks(file, max_chunk_size) if isinstance(file, str) else read_file_content_in_chunks(file, max_chunk_size)
                    )
                )
            )
        )

        if not all(result):
            return None

        request = media_and_files_pb2.RequestCommitFileUpload(
            upload_key=upload_key,
            file_name=os.path.basename(file)
        )
        return FileLocation.from_api(self.internal.media_and_files.CommitFileUpload(request).uploaded_file_location)

    def upload_file_sync(self, file: str or bytes, max_chunk_size=1024*1024, verify=None):
        return self.upload_file.__wrapped__(self, file, max_chunk_size, verify)

    def __upload_file_chunk(self, part_number, chunk, upload_key, access_dir=None, verify=None):
        """Upload file chunk.

        :param part_number: number of chunk (>=0)
        :param chunk: chunk content
        :param upload_key: upload key (need to be received from RequestGetFileUploadUrl request before uploading)
        :return: Response of HTTP PUT request if success or None otherwise
        """

        request = media_and_files_pb2.RequestGetFileUploadPartUrl(
            part_number=part_number,
            part_size=len(chunk),
            upload_key=upload_key
        )
        url = self.internal.media_and_files.GetFileUploadPartUrl(request).url

        retry = 0
        put_response = None

        while retry <= self.retry:
            if self.cert and self.private_key:
                with NamedTemporaryFile(dir=access_dir, delete=False) as cert_file:
                    with NamedTemporaryFile(dir=access_dir, delete=False) as private_key_file:
                        cert_file.write(self.cert)
                        private_key_file.write(self.private_key)
                        cert_file.flush()
                        private_key_file.flush()
                        put_response = requests.put(
                            url,
                            data=chunk,
                            headers={'Content-Type': 'application/octet-stream'},
                            cert=(cert_file.name, private_key_file.name),
                            verify=verify
                        )
                        try:
                            cert_file.close()
                            private_key_file.close()
                            os.unlink(cert_file.name)
                            os.unlink(private_key_file.name)
                        except Exception as e:
                            print(e)
                            pass

            else:
                put_response = requests.put(
                    url,
                    data=chunk,
                    headers={'Content-Type': 'application/octet-stream'},
                    verify=verify
                )

            if put_response.status_code != 200:
                print('Can\'t upload file chunk #%s with status code %s' % (part_number, put_response.status_code))
                retry += 1
                sleep(self.retry_period)
            else:
                return put_response

        if put_response is None:
            raise HTTPError("Bad status code")
        return put_response
