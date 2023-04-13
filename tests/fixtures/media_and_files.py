from dialog_api.media_and_files_pb2 import RequestGetFileUploadUrl, ResponseGetFileUploadUrl, ResponseCommitFileUpload, \
    RequestCommitFileUpload, FileLocation, ResponseGetFileUploadPartUrl, RequestGetFileUploadPartUrl


class Put:
    def __init__(self, code: int) -> None:
        self.status_code = code


class MediaAndFiles:
    def GetFileUploadUrl(self, request: RequestGetFileUploadUrl) -> ResponseGetFileUploadUrl:
        return ResponseGetFileUploadUrl(url=b'', upload_key=b'')

    def CommitFileUpload(self, request: RequestCommitFileUpload) -> ResponseCommitFileUpload:
        return ResponseCommitFileUpload(uploaded_file_location=FileLocation(file_id=0, access_hash=0))

    def GetFileUploadPartUrl(self, request: RequestGetFileUploadPartUrl) -> ResponseGetFileUploadPartUrl:
        return ResponseGetFileUploadPartUrl(url="https://dlg.im")
