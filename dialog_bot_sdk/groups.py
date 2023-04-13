import random
from typing import List

from google.protobuf import wrappers_pb2
from google.protobuf.wrappers_pb2 import BytesValue
from dialog_api.users_pb2 import RequestLoadUserData

from dialog_bot_sdk.utils import async_dec, AsyncTask, get_peer
from .entities.groups import Group, GroupPermission, Permissions, Member
from .entities.media_and_files import Avatar
from .entities.peers import PeerType, Peer
from .entities.users import User
from .service import ManagedService
from dialog_api import search_pb2, groups_pb2, peers_pb2, sequence_and_updates_pb2


class Groups(ManagedService):
    """Class for handling groups

    """
    @async_dec()
    def create_public_group(self, title: str, short_name: str) -> Group:
        """Create public group

        :param title: title of group
        :param short_name: group name
        :return: Group
        """
        request = groups_pb2.RequestCreateGroup(
            title=title,
            username=wrappers_pb2.StringValue(value=short_name),
            group_type=groups_pb2.GROUPTYPE_GROUP
        )
        return self.__create_group(request)

    def create_public_group_sync(self, title: str, short_name: str) -> Group:
        return self.create_public_group.__wrapped__(self, title, short_name)

    @async_dec()
    def create_private_group(self, title: str) -> Group:
        """Create private group

        :param title: title of group
        :return: Group
        """
        request = groups_pb2.RequestCreateGroup(
            title=title,
            group_type=groups_pb2.GROUPTYPE_GROUP
        )
        return self.__create_group(request)

    def create_private_group_sync(self, title: str) -> Group:
        return self.create_private_group.__wrapped__(self, title)

    @async_dec()
    def create_public_channel(self, title: str, short_name: str) -> Group:
        """Create public channel

        :param title: title of group
        :param short_name: group name
        :return: Group
        """

        request = groups_pb2.RequestCreateGroup(
            title=title,
            username=wrappers_pb2.StringValue(value=short_name),
            group_type=groups_pb2.GROUPTYPE_CHANNEL
        )
        return self.__create_group(request)

    def create_public_channel_sync(self, title: str, short_name: str) -> Group:
        return self.create_public_channel.__wrapped__(self, title, short_name)

    @async_dec()
    def create_private_channel(self, title: str) -> Group:
        """Create private channel

        :param title: title of group
        :return: Group
        """

        request = groups_pb2.RequestCreateGroup(
            title=title,
            group_type=groups_pb2.GROUPTYPE_CHANNEL
        )
        return self.__create_group(request)

    def create_private_channel_sync(self, title: str) -> Group:
        return self.create_private_channel.__wrapped__(self, title)

    @async_dec()
    def find_group_by_short_name(self, short_name: str) -> Group or None:
        """Find a Group by short_name

        :param short_name: short_name of group
        :return: Group or None if could not find
        """
        request = search_pb2.RequestPeerSearch(
            query=[
                search_pb2.SearchCondition(
                    searchPeerTypeCondition=search_pb2.SearchPeerTypeCondition(
                        peer_type=search_pb2.SEARCHPEERTYPE_GROUPS
                    )
                ),
                search_pb2.SearchCondition(
                    searchPieceText=search_pb2.SearchPieceText(query=short_name)
                )
            ]
        )
        response = self.internal.search.PeerSearch(request).search_results
        for result in response:
            if result.peer.type == PeerType.PEERTYPE_GROUP and hasattr(result, 'shortname') and \
                    result.shortname.value == short_name:
                return self.find_group_by_id_sync(result.peer.id)

    def find_group_by_short_name_sync(self, short_name: str) -> Group or None:
        return self.find_group_by_short_name.__wrapped__(self, short_name)

    @async_dec()
    def find_group_by_id(self, group_id: int) -> Group or None:
        """Find and return Group by id

        :param group_id: group's
        :return: Group or None if could not find
        """
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            groups=[peers_pb2.GroupOutPeer(group_id=group_id, access_hash=0)]
        )
        result = self.internal.updates.GetReferencedEntitites(request).groups

        if not result:
            return

        self.manager.add_out_peer(peers_pb2.OutPeer(id=result[0].id, type=PeerType.PEERTYPE_GROUP,
                                                    access_hash=result[0].access_hash))
        return Group.from_api(result[0])

    def find_group_by_id_sync(self, group_id: int) -> Group or None:
        return self.find_group_by_id.__wrapped__(self, group_id)

    @async_dec()
    def load_members(self, group_peer: Peer or AsyncTask, limit: int = 0, cursor: bytes = b"",
                     cursor_flag: bool = False) -> List[User] or List[User] and bytes or None:
        """Load Group members by peer

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param limit: count members
        :param cursor: bytes object that specify to the user from whom to start (returned from this method)
        :param cursor_flag: returned cursor? (True/False)
        :return: list of User's
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        if out_peer is None:
            return None

        request = groups_pb2.RequestLoadMembers(
            group=out_peer,
            limit=limit,
            next=BytesValue(value=cursor)
        )
        response = self.internal.groups.LoadMembers(request)
        members = response.members
        cursor = response.cursor.value
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            group_members=[
                sequence_and_updates_pb2.GroupMembersSubset(
                    group_peer=out_peer,
                    member_ids=[member.uid for member in members]
                )
            ]
        )
        users = self.internal.updates.GetReferencedEntitites(request).users
        for user in users:
            self.manager.add_out_peer(
                peers_pb2.OutPeer(
                    id=user.id,
                    type=peers_pb2.PEERTYPE_PRIVATE,
                    access_hash=user.access_hash
                )
            )
        if cursor_flag:
            return [User.from_api(x) for x in users], cursor
        return [User.from_api(x) for x in users]

    def load_members_sync(self, group_peer: Peer or AsyncTask, limit: int = 0, cursor: bytes = b"",
                     cursor_flag: bool = False) -> List[User] or List[User] and bytes or None:
        return self.load_members.__wrapped__(self, group_peer, limit, cursor, cursor_flag)

    @async_dec()
    def get_member(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> Member or None:
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer), self.__get_out_peer(user_peer)

        if group_out_peer is None:
            return
        if user_out_peer is None:
            request = RequestLoadUserData(
                claims=[
                    RequestLoadUserData.Claim(
                        user_peer=peers_pb2.Peer(id=user_peer.id, type=peers_pb2.PEERTYPE_PRIVATE),
                        group_member=peers_pb2.Peer(id=group_peer.id, type=peers_pb2.PEERTYPE_GROUP)
                    ),
                ]
            )
            result = self.internal.users.LoadUserData(request).users
            for user in result:
                self.manager.add_out_peer(
                    peers_pb2.OutPeer(
                        id=user.id,
                        type=peers_pb2.PEERTYPE_PRIVATE,
                        access_hash=user.access_hash
                    )
                )
            user_out_peer = self.__get_out_peer(user_peer)
        if user_out_peer is None:
            return
        request = groups_pb2.RequestGetMember(
            group_peer=group_out_peer,
            user_peer=user_out_peer,
        )
        response = self.internal.groups.GetMember(request)
        return Member.from_api(response.member) if response.member.uid != 0 else None

    def get_member_sync(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> Member:
        return self.get_member.__wrapped__(self, group_peer, user_peer)

    @async_dec()
    def kick_user(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        """Kick user from Group

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param user_peer: Peer or AsyncTask (in which located User)
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer), self.__get_out_peer(user_peer)

        request = groups_pb2.RequestKickUser(
            group_peer=group_out_peer,
            user=user_out_peer,
            rid=random.randint(0, 100000000),
        )
        self.internal.groups.KickUser(request)

    def kick_user_sync(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        return self.kick_user.__wrapped__(self, group_peer, user_peer)

    @async_dec()
    def invite_user(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        """Invite user in Group

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param user_peer: Peer or AsyncTask (in which located User)
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer), self.__get_out_peer(user_peer)

        request = groups_pb2.RequestInviteUser(
            group_peer=group_out_peer,
            user=user_out_peer,
            rid=random.randint(0, 100000000),
        )
        self.internal.groups.InviteUser(request)

    def invite_user_sync(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        return self.invite_user.__wrapped__(self, group_peer, user_peer)

    @async_dec()
    def set_default_group_permissions(self, group_peer: Peer or AsyncTask,
                                      add_permissions: List[GroupPermission] = None,
                                      del_permissions: List[GroupPermission] = None) -> None:
        """add/del default group permissions

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param add_permissions: list of permissions to add
        :param del_permissions: list of permissions to delete
        :return: None
        """
        group_peer = get_peer(group_peer)
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []

        group_out_peer = self.__get_out_peer(group_peer)
        add_request = groups_pb2.RequestEditGroupBasePermissions(
            group_peer=group_out_peer,
            random_id=random.randint(0, 100000000),
            granted_permissions=[x for x in add_permissions]
        )
        del_request = groups_pb2.RequestEditGroupBasePermissions(
            group_peer=group_out_peer,
            random_id=random.randint(0, 100000000),
            revoked_permissions=[x for x in del_permissions]
        )

        self.internal.groups.EditGroupBasePermissions(add_request)
        self.internal.groups.EditGroupBasePermissions(del_request)

    def set_default_group_permissions_sync(self, group_peer: Peer or AsyncTask,
                                           add_permissions: List[GroupPermission] = None,
                                           del_permissions: List[GroupPermission] = None) -> None:
        return self.set_default_group_permissions.__wrapped__(self, group_peer, add_permissions, del_permissions)

    @async_dec()
    def set_member_permissions(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask,
                               add_permissions: List[GroupPermission] = None,
                               del_permissions: List[GroupPermission] = None) -> None:
        """add/del group's member permissions

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param user_peer: Peer or AsyncTask (in which located User)
        :param add_permissions: list of permissions to add
        :param del_permissions: list of permissions to delete
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer), self.__get_out_peer(user_peer)
        add_request = groups_pb2.RequestEditMemberPermissions(
            group_peer=group_out_peer,
            user_peer=user_out_peer,
            granted_permissions=[x for x in add_permissions]
        )
        del_request = groups_pb2.RequestEditMemberPermissions(
            group_peer=group_out_peer,
            user_peer=user_out_peer,
            revoked_permissions=[x for x in del_permissions]
        )

        self.internal.groups.EditMemberPermissions(add_request)
        self.internal.groups.EditMemberPermissions(del_request)

    def set_member_permissions_sync(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask,
                               add_permissions: List[GroupPermission] = None,
                               del_permissions: List[GroupPermission] = None) -> None:
        return self.set_member_permissions.__wrapped__(self, group_peer, user_peer, add_permissions, del_permissions)

    @async_dec()
    def get_group_member_permissions(self, group_peer: Peer or AsyncTask, user_peers: List[Peer or AsyncTask]) \
            -> List[Permissions]:
        """return group member's permissions

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param user_peers: Peer or AsyncTask (in which located User)
        :return: group member's permissions
        """
        group_peer, user_peers = get_peer(group_peer), [get_peer(x) for x in user_peers]
        request = groups_pb2.RequestGetGroupMemberPermissions(
            group_id=group_peer.id,
            user_ids=[peer.id for peer in user_peers]
        )
        return [Permissions.from_api(x) for x in self.internal.groups.GetGroupMemberPermissions(request).permissions]

    def get_group_member_permissions_sync(self, group_peer: Peer or AsyncTask, user_peers: List[Peer or AsyncTask]) \
            -> List[Permissions]:
        return self.get_group_member_permissions.__wrapped__(self, group_peer, user_peers)

    @async_dec()
    def edit_group_title(self, group_peer: Peer or AsyncTask, title: str) -> None:
        """change group's title

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param title: new title
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestEditGroupTitle(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
            title=title
        )
        self.internal.groups.EditGroupTitle(request)

    def edit_group_title_sync(self, group_peer: Peer or AsyncTask, title: str) -> None:
        return self.edit_group_title.__wrapped__(self, group_peer, title)

    @async_dec()
    def edit_avatar(self, group_peer: Peer or AsyncTask, file: str) -> Avatar or None:
        """change group's avatar

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param file: file path
        :return: Avatar
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        location = self.internal.uploading.upload_file_sync(file)
        if location is None:
            return None
        request = groups_pb2.RequestEditGroupAvatar(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
            file_location=location.to_api()
        )
        return Avatar.from_api(self.internal.groups.EditGroupAvatar(request).avatar)

    def edit_avatar_sync(self, group_peer: Peer or AsyncTask, file: str) -> Avatar or None:
        return self.edit_avatar.__wrapped__(self, group_peer, file)

    @async_dec()
    def remove_group_avatar(self, group_peer: Peer or AsyncTask) -> None:
        """deleted group's avatar

        :param group_peer: Peer or AsyncTask (in which located User)
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestRemoveGroupAvatar(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
        )
        self.internal.groups.RemoveGroupAvatar(request)

    def remove_group_avatar_sync(self, group_peer: Peer or AsyncTask) -> None:
        return self.remove_group_avatar.__wrapped__(self, group_peer)

    @async_dec()
    def edit_group_about(self, group_peer: Peer or AsyncTask, about: str) -> None:
        """change group's "about"

        :param group_peer: Peer or AsyncTask (in which located User)
        :param about: about text
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestEditGroupAbout(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
            about=wrappers_pb2.StringValue(value=about)
        )
        self.internal.groups.EditGroupAbout(request)

    def edit_group_about_sync(self, group_peer: Peer or AsyncTask, about: str) -> None:
        return self.edit_group_about.__wrapped__(self, group_peer, about)

    @async_dec()
    def leave_group(self, group_peer: Peer or AsyncTask) -> None:
        """leave from group

        :param group_peer: Peer or AsyncTask (in which located Group)
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestLeaveGroup(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
        )
        self.internal.groups.LeaveGroup(request)

    def leave_group_sync(self, group_peer: Peer or AsyncTask) -> None:
        return self.leave_group.__wrapped__(self, group_peer)

    @async_dec()
    def make_user_admin(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        """Set new user's permissions (old permissions will be revoke)

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param user_peer: Peer or AsyncTask (in which located User)
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer), self.__get_out_peer(user_peer)
        request = groups_pb2.RequestMakeUserAdmin(
            group_peer=group_out_peer,
            user_peer=user_out_peer,
        )
        self.internal.groups.MakeUserAdmin(request)

    def make_user_admin_sync(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        return self.make_user_admin.__wrapped__(self, group_peer, user_peer)

    @async_dec()
    def transfer_ownership(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        """change group's owner to user

        :param group_peer: Peer or AsyncTask (in which located Group)
        :param user_peer: Peer or AsyncTask (in which located User)
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestTransferOwnership(
            group_peer=out_peer,
            new_owner=user_peer.id
        )
        self.internal.groups.TransferOwnership(request)

    def transfer_ownership_sync(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        return self.transfer_ownership.__wrapped__(self, group_peer, user_peer)

    @async_dec()
    def get_group_invite_url(self, group_peer: Peer or AsyncTask) -> str:
        """return group's invite url

        :param group_peer: Peer or AsyncTask (in which located Group)
        :return: invite url
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestGetGroupInviteUrl(
            group_peer=out_peer
        )
        return self.internal.groups.GetGroupInviteUrl(request).url

    def get_group_invite_url_sync(self, group_peer: Peer or AsyncTask) -> str:
        return self.get_group_invite_url.__wrapped__(self, group_peer)

    @async_dec()
    def get_group_invite_url_base(self) -> str:
        """return group's invite url without token/short_name (example https://domain/@)

        :return: invite url (string)
        """
        request = groups_pb2.RequestGetGroupInviteUrlBase()
        return self.internal.groups.GetGroupInviteUrlBase(request).url

    def get_group_invite_url_base_sync(self) -> str:
        return self.get_group_invite_url_base.__wrapped__(self)

    @async_dec()
    def revoke_invite_url(self, group_peer: Peer or AsyncTask) -> str:
        """revoke current invite url and return new group's invite url

        :return: invite url
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestRevokeInviteUrl(
            group_peer=out_peer
        )
        return self.internal.groups.RevokeInviteUrl(request).url

    def revoke_invite_url_sync(self, group_peer: Peer or AsyncTask) -> str:
        return self.revoke_invite_url.__wrapped__(self, group_peer)

    @async_dec()
    def join_group(self, token_or_url: str) -> Group:
        """join to group by token or invite url (used for private groups)

        :param token_or_url: group's token or invite url
        :return: Group
        """
        request = groups_pb2.RequestJoinGroup(
            token=token_or_url
        )
        response = self.internal.groups.JoinGroup(request)
        self.manager.add_out_peer(peers_pb2.OutPeer(id=response.group.id, access_hash=response.group.access_hash,
                                                    type=PeerType.PEERTYPE_GROUP))
        return Group.from_api(response.group)

    def join_group_sync(self, token_or_url: str) -> Group:
        return self.join_group.__wrapped__(self, token_or_url)

    @async_dec()
    def join_group_by_peer(self, group_peer: Peer or AsyncTask) -> None:
        """join to group by group's peer (used for public groups)

        :param group_peer: Peer or AsyncTask (in which located Group)
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestJoinGroupByPeer(
            peer=out_peer
        )
        self.internal.groups.JoinGroupByPeer(request)

    def join_group_by_peer_sync(self, group_peer: Peer or AsyncTask) -> None:
        return self.join_group_by_peer.__wrapped__(self, group_peer)

    @async_dec()
    def delete_group(self, group_id: int or AsyncTask) -> None:
        """delete group by id. Need permission GROUPADMINPERMISSION_DELETE.

        :param group_id: group's id or AsyncTask (in which located Group)
        :return: None
        """
        if not isinstance(group_id, int):
            group_id = get_peer(group_id).id

        request = groups_pb2.RequestDeleteGroup(
            group_id=group_id
        )
        self.internal.groups.DeleteGroup(request)

    def delete_group_sync(self, group_id: int or AsyncTask) -> None:
        return self.delete_group.__wrapped__(self, group_id)

    @async_dec()
    def set_hide_system_messages(self, group_peer: Peer or AsyncTask, hide: bool) -> None:
        """Hide system messages for group

        :param group_peer: group's peer or AsyncTask (in which located Group)
        :param hide: True or False
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)

        request = groups_pb2.RequestSetHideSystemMessages(
            group_peer=out_peer,
            hide=hide
        )
        self.internal.groups.SetHideSystemMessages(request)

    def set_hide_system_messages_sync(self, group_peer: Peer or AsyncTask, hide: bool) -> None:
        return self.set_hide_system_messages.__wrapped__(self, group_peer, hide)

    @async_dec()
    def set_threads_enabled(self, group_peer: Peer or AsyncTask, threads_enabled: bool) -> None:
        """Hide system messages for group

        :param group_peer: group's peer or AsyncTask (in which located Group)
        :param threads_enabled: True or False
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)

        request = groups_pb2.RequestSetThreadsEnabled(
            group_peer=out_peer,
            threads_enabled=threads_enabled
        )
        self.internal.groups.SetThreadsEnabled(request)

    def set_threads_enabled_sync(self, group_peer: Peer or AsyncTask, threads_enabled: bool) -> None:
        return self.set_threads_enabled.__wrapped__(self, group_peer, threads_enabled)

    def __get_out_peer(self, peer: peers_pb2.Peer) -> peers_pb2.GroupOutPeer or peers_pb2.UserOutPeer or None:
        out_peer = self.manager.get_out_peer(peer)
        if out_peer is None:
            return None
        if peer.type == PeerType.PEERTYPE_GROUP:
            return peers_pb2.GroupOutPeer(group_id=out_peer.id, access_hash=out_peer.access_hash)
        elif peer.type == PeerType.PEERTYPE_PRIVATE:
            return peers_pb2.UserOutPeer(uid=out_peer.id, access_hash=out_peer.access_hash)

    def __create_group(self, request: groups_pb2.RequestCreateGroup) -> Group:
        request.rid = random.randint(0, 100000000)
        group = self.internal.groups.CreateGroup(request).group
        self.manager.add_out_peer(
            peers_pb2.OutPeer(id=group.id, access_hash=group.access_hash, type=PeerType.PEERTYPE_GROUP))
        return Group.from_api(group)
