import os
import requests
from concurrent.futures import ThreadPoolExecutor

from .utils.read_file_in_chunks import read_file_in_chunks
from .dialog_api import media_and_files_pb2


class Uploading(object):
    """Class for high-level file uploading interface.

    """

    def __init__(self, internal):
        self.internal = internal

    def upload_file_chunk(self, part_number, chunk, upload_key):
        """Upload file chunk.

        :param part_number: number of chunk (>=0)
        :param chunk: chunk content
        :param upload_key: upload key (need to be received from RequestGetFileUploadUrl request before uploading)
        :return: Response of HTTP PUT request if success or None otherwise
        """

        url = self.internal.media_and_files.GetFileUploadPartUrl(
            media_and_files_pb2.RequestGetFileUploadPartUrl(
                part_number=part_number,
                part_size=len(chunk),
                upload_key=upload_key
            )
        ).url

        put_response = requests.put(
            url,
            data=chunk,
            headers={'Content-Type': 'application/octet-stream'}
        )

        if put_response.status_code != 200:
            print('Can\'t upload file chunk #{}'.format(part_number))
            return None

        return put_response

    def upload_file(self, file, max_chunk_size=1024*1024, parallelism=10):
        """Upload file for sending.

        :param file: path to file
        :param max_chunk_size: maximum size of one chunk (default 1024 * 1024)
        :param parallelism: number of uploading threads (default: 10)
        :return: FileLocation object if success or None otherwise
        """

        upload_key = self.internal.media_and_files.GetFileUploadUrl(
            media_and_files_pb2.RequestGetFileUploadUrl(
                expected_size=os.path.getsize(file)
            )
        ).upload_key

        with ThreadPoolExecutor(max_workers=parallelism) as executor:
            result = list(
                executor.map(
                    lambda x: self.upload_file_chunk(*x),
                    (
                        (part_number, chunk, upload_key) for part_number, chunk in enumerate(
                            read_file_in_chunks(file, max_chunk_size)
                        )
                    )
                )
            )

            if not all(result):
                return None

        return self.internal.media_and_files.CommitFileUpload(
            media_and_files_pb2.RequestCommitFileUpload(
                upload_key=upload_key,
                file_name=os.path.basename(file)
            )
        ).uploaded_file_location
