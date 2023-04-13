from dialog_api.miscellaneous_pb2 import ResponseBool
from dialog_api.profile_pb2 import RequestEditName, RequestEditNickName, RequestCheckNickName, RequestEditAbout, \
    RequestEditAvatar, RequestRemoveAvatar, RequestEditMyTimeZone, RequestEditMyPreferredLanguages, RequestEditSex, \
    RequestEditCustomProfile, RequestChangeUserStatus


class Profile:
    def EditName(self, request: RequestEditName) -> None:
        pass

    def EditNickName(self, request: RequestEditNickName) -> None:
        pass

    def CheckNickName(self, request: RequestCheckNickName) -> ResponseBool:
        if request.nickname == "nick":
            return ResponseBool(value=True)
        return ResponseBool(value=False)

    def EditAbout(self, request: RequestEditAbout) -> None:
        pass

    def EditAvatar(self, request: RequestEditAvatar) -> None:
        pass

    def RemoveAvatar(self, request: RequestRemoveAvatar) -> None:
        pass

    def EditMyTimeZone(self, request: RequestEditMyTimeZone) -> None:
        pass

    def EditMyPreferredLanguages(self, request: RequestEditMyPreferredLanguages) -> None:
        pass

    def EditSex(self, request: RequestEditSex) -> None:
        pass

    def EditCustomProfile(self, request: RequestEditCustomProfile) -> None:
        pass

    def ChangeUserStatus(self, request: RequestChangeUserStatus) -> None:
        pass
