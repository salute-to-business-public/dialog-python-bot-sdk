from dialog_api.groups_pb2 import RequestCreateGroup, ResponseCreateGroup, RequestLoadMembers, ResponseLoadMembers, \
    RequestKickUser, RequestInviteUser, RequestEditGroupBasePermissions, RequestEditMemberPermissions, \
    RequestGetGroupMemberPermissions, ResponseGetGroupMemberPermissions, RequestEditGroupTitle, \
    RequestRemoveGroupAvatar, RequestEditGroupAbout, RequestLeaveGroup, RequestMakeUserAdmin, RequestTransferOwnership, \
    RequestGetGroupInviteUrl, RequestGetGroupInviteUrlBase, ResponseGetGroupInviteUrlBase, RequestRevokeInviteUrl, \
    RequestJoinGroup, ResponseJoinGroup, RequestJoinGroupByPeer, RequestEditGroupAvatar, ResponseEditGroupAvatar, \
    ResponseInviteUrl, RequestDeleteGroup

from tests.fixtures.server_entities import avatar, mid, group, user_outpeer


class Groups:
    def CreateGroup(self, request: RequestCreateGroup) -> ResponseCreateGroup:
        return ResponseCreateGroup(seq=0, state=b'', group=group, user_peers=[user_outpeer])

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

    def GetGroupInviteUrl(self, request: RequestGetGroupInviteUrl) -> ResponseInviteUrl:
        return ResponseInviteUrl(url='url')

    def GetGroupInviteUrlBase(self, request: RequestGetGroupInviteUrlBase) -> ResponseGetGroupInviteUrlBase:
        return ResponseGetGroupInviteUrlBase(url='url')

    def RevokeInviteUrl(self, request: RequestRevokeInviteUrl) -> ResponseInviteUrl:
        return ResponseInviteUrl(url='url')

    def JoinGroup(self, request: RequestJoinGroup) -> ResponseJoinGroup:
        return ResponseJoinGroup(group=group, user_peers=[user_outpeer], mid=mid, seq=0, state=b'', date=0)

    def JoinGroupByPeer(self, request: RequestJoinGroupByPeer) -> None:
        pass

    def EditGroupAvatar(self, request: RequestEditGroupAvatar) -> ResponseEditGroupAvatar:
        return ResponseEditGroupAvatar(avatar=avatar, seq=0, state=b'', date=0, mid=mid)

    def DeleteGroup(self, request: RequestDeleteGroup) -> None:
        pass
