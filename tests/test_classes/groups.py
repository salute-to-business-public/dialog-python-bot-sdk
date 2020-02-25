from dialog_api.groups_pb2 import RequestCreateGroup, ResponseCreateGroup, RequestLoadMembers, ResponseLoadMembers, \
    RequestKickUser, RequestInviteUser, RequestEditGroupBasePermissions, RequestEditMemberPermissions, \
    RequestGetGroupMemberPermissions, ResponseGetGroupMemberPermissions, RequestEditGroupTitle, \
    RequestRemoveGroupAvatar, RequestEditGroupAbout, RequestLeaveGroup, RequestMakeUserAdmin, RequestTransferOwnership, \
    RequestGetGroupInviteUrl, RequestGetGroupInviteUrlBase, ResponseGetGroupInviteUrlBase, RequestRevokeInviteUrl, \
    RequestJoinGroup, ResponseJoinGroup, Group, RequestJoinGroupByPeer, RequestEditGroupAvatar, ResponseEditGroupAvatar


class ResponseGetGroupInviteUrl:
    def __init__(self, url: str) -> None:
        self.url = url


class ResponseRevokeInviteUrl:
    def __init__(self, url: str) -> None:
        self.url = url


class Groups:
    def CreateGroup(self, request: RequestCreateGroup) -> ResponseCreateGroup:
        return ResponseCreateGroup(seq=0, state=b'', group=None, user_peers=[])

    def LoadMembers(self, request: RequestLoadMembers):
        return ResponseLoadMembers(cursor=None, members=[])

    def KickUser(self, request: RequestKickUser) -> None:
        pass

    def InviteUser(self, request: RequestInviteUser) -> None:
        pass

    def EditGroupBasePermissions(self, request: RequestEditGroupBasePermissions) -> None:
        pass

    def EditMemberPermissions(self, request: RequestEditMemberPermissions) -> None:
        pass

    def GetGroupMemberPermissions(self, request: RequestGetGroupMemberPermissions) -> ResponseGetGroupMemberPermissions:
        return ResponseGetGroupMemberPermissions(permissions=[])

    def EditGroupTitle(self, request: RequestEditGroupTitle) -> None:
        pass

    def RemoveGroupAvatar(self, request: RequestRemoveGroupAvatar) -> None:
        pass

    def EditGroupAbout(self, request: RequestEditGroupAbout) -> None:
        pass

    def LeaveGroup(self, request: RequestLeaveGroup) -> None:
        pass

    def MakeUserAdmin(self, request: RequestMakeUserAdmin) -> None:
        pass

    def TransferOwnership(self, request: RequestTransferOwnership) -> None:
        pass

    def GetGroupInviteUrl(self, request: RequestGetGroupInviteUrl) -> ResponseGetGroupInviteUrl:
        return ResponseGetGroupInviteUrl("url")

    def GetGroupInviteUrlBase(self, request: RequestGetGroupInviteUrlBase) -> ResponseGetGroupInviteUrlBase:
        return ResponseGetGroupInviteUrlBase(url='url')

    def RevokeInviteUrl(self, request: RequestRevokeInviteUrl) -> ResponseRevokeInviteUrl:
        return ResponseRevokeInviteUrl("url")

    def JoinGroup(self, request: RequestJoinGroup) -> ResponseJoinGroup:
        return ResponseJoinGroup(group=Group(id=0, access_hash=0, data=None),
                                 user_peers=[], mid=None, seq=0, state=b'', date=0)

    def JoinGroupByPeer(self, request: RequestJoinGroupByPeer) -> None:
        pass

    def EditGroupAvatar(self, request: RequestEditGroupAvatar) -> ResponseEditGroupAvatar:
        return ResponseEditGroupAvatar(avatar=None, seq=0, state=b'', date=0, mid=None)
