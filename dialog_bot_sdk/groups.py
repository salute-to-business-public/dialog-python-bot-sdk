import random
from typing import List, Tuple

from google.protobuf import wrappers_pb2

from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.Group import Group
from dialog_bot_sdk.entities.Permissions import Permissions, GroupPermission
from dialog_bot_sdk.entities.ReferencedEntities import ReferencedEntities
from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.entities.User import User
from dialog_bot_sdk.entities.Peer import Peer, PeerType
from dialog_bot_sdk.utils import async_dec, AsyncTask, get_peer
from .service import ManagedService
from dialog_api import search_pb2, groups_pb2, peers_pb2, sequence_and_updates_pb2, media_and_files_pb2


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

    @async_dec()
    def find_group_by_short_name(self, short_name: str) -> Group or None:
        """Find a groups by short_name

        :param short_name: short_name of group
        :return: PeerSearchResult or None if could not find
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
        response = self.__peer_search(request).search_results
        for result in response:
            print(result)
            if result.peer.type == PeerType.PEERTYPE_GROUP and hasattr(result, 'shortname') and \
                    result.shortname.value == short_name:
                return self.find_group_by_id(result.peer.id)

    @async_dec()
    def find_group_by_id(self, group_id: int) -> Group or None:
        """search and return group by id

        :param group_id: group's
        :return: Group or None if could not find
        """
        out_peer = self.__get_out_peer(Peer(group_id, PeerType.PEERTYPE_GROUP))
        if out_peer is None:
            return None
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            groups=[out_peer[1]]
        )
        result = self.__get_referenced_entities(request).groups
        self.manager.add_out_peer(self.__get_out_peer(Peer(result[0].id, PeerType.PEERTYPE_GROUP))[0])
        return Group.from_api(result[0])

    @async_dec()
    def load_members(self, group_peer: Peer or AsyncTask, limit: int = 0) -> List[User] or None:
        """User's list from group

        :param group_peer: group's Peer
        :param limit: count members
        :return: list of User's
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)

        if not out_peer:
            return None

        request = groups_pb2.RequestLoadMembers(
            group=out_peer,
            limit=limit
        )
        members = self.__load_members(request).members
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            group_members=[
                sequence_and_updates_pb2.GroupMembersSubset(
                    group_peer=out_peer,
                    member_ids=[member.uid for member in members]
                )
            ]
        )
        return self.__get_referenced_entities(request).users

    @async_dec()
    def kick_user(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        """return response of KickUser

        :param group_peer: group's Peer
        :param user_peer: user's Peer
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer)[1], self.__get_out_peer(user_peer)[1]
        request = groups_pb2.RequestKickUser(
            group_peer=group_out_peer,
            user=user_out_peer,
            rid=random.randint(0, 100000000),
        )
        self.__kick_user(request)

    @async_dec()
    def invite_user(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        """return response of InviteUser

        :param group_peer: group's Peer
        :param user_peer: user's Peer
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer)[1], self.__get_out_peer(user_peer)[1]
        request = groups_pb2.RequestInviteUser(
            group_peer=group_out_peer,
            user=user_out_peer,
            rid=random.randint(0, 100000000),
        )
        self.__invite_user(request)

    @async_dec()
    def set_default_group_permissions(self, group_peer: Peer or AsyncTask,
                                      add_permissions: List[GroupPermission] = None,
                                      del_permissions: List[GroupPermission] = None) -> None:
        """add/del default group permissions

        :param group_peer: group's peer
        :param add_permissions: list of permissions to add
        :param del_permissions: list of permissions to delete
        :return: None
        """
        group_peer = get_peer(group_peer)
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []

        group_out_peer = self.__get_out_peer(group_peer)[1]
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

        self.__set_default_group_permissions(add_request)
        self.__set_default_group_permissions(del_request)

    @async_dec()
    def set_member_permissions(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask,
                               add_permissions: List[GroupPermission] = None,
                               del_permissions: List[GroupPermission] = None) -> None:
        """add/del group's member permissions

        :param group_peer: group's peer
        :param user_peer: OutPeer of user
        :param add_permissions: list of permissions to add
        :param del_permissions: list of permissions to delete
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer)[1], self.__get_out_peer(user_peer)[1]
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

        self.__set_member_permissions(add_request)
        self.__set_member_permissions(del_request)

    @async_dec()
    def get_group_member_permissions(self, group_peer: Peer or AsyncTask, user_peers: List[Peer or AsyncTask]) \
            -> List[Permissions]:
        """return group member's permissions

        :param group_peer: Group's Peer
        :param user_peers: User's Peer
        :return: group member's permissions
        """
        group_peer, user_peers = get_peer(group_peer), [get_peer(x) for x in user_peers]
        request = groups_pb2.RequestGetGroupMemberPermissions(
            group_id=group_peer.id,
            user_ids=[peer.id for peer in user_peers]
        )
        return self.__get_group_member_permissions(request)

    @async_dec()
    def edit_group_title(self, group_peer: Peer or AsyncTask, title: str) -> None:
        """change group's title

        :param group_peer: group's Peer
        :param title: new title (string)
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        request = groups_pb2.RequestEditGroupTitle(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
            title=title
        )
        self.__edit_group_title(request)

    @async_dec()
    def edit_avatar(self, group_peer: Peer or AsyncTask, file: str) -> Avatar:
        """change group's avatar

        :param group_peer: group's Peer
        :param file: file path
        :return: Avatar
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        location = self.__upload(file)
        request = groups_pb2.RequestEditGroupAvatar(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
            file_location=location
        )
        return self.__edit_group_avatar(request)

    @async_dec()
    def remove_group_avatar(self, group_peer: Peer or AsyncTask) -> None:
        """deleted group's avatar

        :param group_peer: group's Peer
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        request = groups_pb2.RequestRemoveGroupAvatar(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
        )
        self.__remove_group_avatar(request)

    @async_dec()
    def edit_group_about(self, group_peer: Peer or AsyncTask, about: str) -> None:
        """change group's "about"

        :param group_peer: group's peer
        :param about: about text (string)
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        request = groups_pb2.RequestEditGroupAbout(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
            about=wrappers_pb2.StringValue(value=about)
        )
        self.__edit_group_about(request)

    @async_dec()
    def leave_group(self, group_peer: Peer or AsyncTask) -> None:
        """leave from group

        :param group_peer: group's Peer
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)
        request = groups_pb2.RequestLeaveGroup(
            group_peer=out_peer,
            rid=random.randint(0, 100000000),
        )
        self.__leave_group(request)

    @async_dec()
    def make_user_admin(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask,
                        permissions: List[GroupPermission]) -> None:
        """Set new user's permissions (old permissions will be revoke)

        :param group_peer: group's Peer
        :param user_peer: user's Peer
        :param permissions: permissions list (for admin)
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        group_out_peer, user_out_peer = self.__get_out_peer(group_peer)[1], self.__get_out_peer(user_peer)[1]
        request = groups_pb2.RequestMakeUserAdmin(
            group_peer=group_out_peer,
            user_peer=user_out_peer,
            permissions=permissions
        )
        self.__make_user_admin(request)

    @async_dec()
    def transfer_ownership(self, group_peer: Peer or AsyncTask, user_peer: Peer or AsyncTask) -> None:
        """change group's owner to user

        :param group_peer: group's Peer
        :param user_peer: user's Peer
        :return: None
        """
        group_peer, user_peer = get_peer(group_peer), get_peer(user_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        request = groups_pb2.RequestTransferOwnership(
            group_peer=out_peer,
            new_owner=user_peer.id
        )
        self.__transfer_ownership(request)

    @async_dec()
    def get_group_invite_url(self, group_peer: Peer or AsyncTask) -> str:
        """return group's invite url

        :param group_peer: Peer
        :return: invite url
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        request = groups_pb2.RequestGetGroupInviteUrl(
            group_peer=out_peer
        )
        return self.__get_group_invite_url(request)

    @async_dec()
    def get_group_invite_url_base(self) -> str:
        """return group's invite url without token/short_name (example https://domain/@)

        :return: invite url (string)
        """
        request = groups_pb2.RequestGetGroupInviteUrlBase()
        return self.__get_group_invite_url_base(request)

    @async_dec()
    def revoke_invite_url(self, group_peer: Peer or AsyncTask) -> str:
        """revoke current invite url and return new group's invite url

        :return: invite url
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        request = groups_pb2.RequestRevokeInviteUrl(
            group_peer=out_peer
        )
        return self.__revoke_invite_url(request)

    @async_dec()
    def join_group(self, token_or_url: str) -> Group:
        """join to group by token or invite url (used for private groups)

        :param token_or_url: group's token or invite url
        :return: Group
        """
        request = groups_pb2.RequestJoinGroup(
            token=token_or_url
        )
        return self.__join_group(request)

    @async_dec()
    def join_group_by_peer(self, group_peer: Peer or AsyncTask) -> None:
        """join to group by group's peer (used for public groups)

        :param group_peer: Peer
        :return: None
        """
        group_peer = get_peer(group_peer)
        out_peer = self.__get_out_peer(group_peer)[1]
        request = groups_pb2.RequestJoinGroupByPeer(
            peer=out_peer
        )
        self.__join_group_by_peer(request)

    def __get_out_peer(self, peer: peers_pb2.Peer) -> Tuple[peers_pb2.OutPeer,
                                                      peers_pb2.GroupOutPeer or peers_pb2.UserOutPeer] or None:
        out_peer = self.manager.get_out_peer(peer)
        if out_peer is None:
            return None
        if peer.type == PeerType.PEERTYPE_GROUP:
            return out_peer, peers_pb2.GroupOutPeer(group_id=out_peer.id, access_hash=out_peer.access_hash)
        elif peer.type == PeerType.PEERTYPE_PRIVATE:
            return out_peer, peers_pb2.UserOutPeer(uid=out_peer.id, access_hash=out_peer.access_hash)

    def __create_group(self, request: groups_pb2.RequestCreateGroup) -> Group:
        """return Group by RequestCreateGroup

        :param request: RequestCreateGroup
        :return: Group
        """
        group = self.internal.groups.CreateGroup(request).group
        self.manager.add_out_peer(
            peers_pb2.OutPeer(id=group.id, access_hash=group.access_hash, type=PeerType.PEERTYPE_GROUP))
        return Group.from_api(group)

    def __peer_search(self, request: search_pb2.RequestPeerSearch) -> search_pb2.ResponsePeerSearch:
        return self.internal.search.PeerSearch(request)

    def __load_members(self, request: groups_pb2.RequestLoadMembers) -> groups_pb2.ResponseLoadMembers:
        return self.internal.groups.LoadMembers(request)

    def __set_default_group_permissions(self, request: groups_pb2.RequestEditGroupBasePermissions) -> None:
        return self.internal.groups.EditGroupBasePermissions(request)

    def __set_member_permissions(self, request: groups_pb2.RequestEditMemberPermissions) -> None:
        return self.internal.groups.EditMemberPermissions(request)

    def __get_group_member_permissions(self, request: groups_pb2.RequestGetGroupMemberPermissions) -> List[Permissions]:
        return [Permissions.from_api(x) for x in self.internal.groups.GetGroupMemberPermissions(request).permissions]

    def __edit_group_title(self, request: groups_pb2.RequestEditGroupTitle) -> None:
        self.internal.groups.EditGroupTitle(request)

    def __edit_group_avatar(self, request: groups_pb2.RequestEditGroupAvatar) -> Avatar:
        return Avatar.from_api(self.internal.groups.EditGroupAvatar(request).avatar)

    def __remove_group_avatar(self, request: groups_pb2.RequestRemoveGroupAvatar) -> UUID:
        return UUID.from_api(self.internal.groups.RemoveGroupAvatar(request).mid)

    def __edit_group_about(self, request: groups_pb2.RequestEditGroupAbout) -> None:
        self.internal.groups.EditGroupAbout(request)

    def __leave_group(self, request: groups_pb2.RequestLeaveGroup) -> None:
        self.internal.groups.LeaveGroup(request)

    def __make_user_admin(self, request: groups_pb2.RequestMakeUserAdmin) -> None:
        self.internal.groups.MakeUserAdmin(request)

    def __transfer_ownership(self, request: groups_pb2.RequestTransferOwnership) -> None:
        self.internal.groups.TransferOwnership(request)

    def __get_group_invite_url(self, request: groups_pb2.RequestGetGroupInviteUrl) -> str:
        return self.internal.groups.GetGroupInviteUrl(request).url

    def __get_group_invite_url_base(self, request: groups_pb2.RequestGetGroupInviteUrlBase) -> str:
        return self.internal.groups.GetGroupInviteUrlBase(request).url

    def __revoke_invite_url(self, request: groups_pb2.RequestRevokeInviteUrl) -> str:
        return self.internal.groups.RevokeInviteUrl(request).url

    def __join_group(self, request: groups_pb2.RequestJoinGroup) -> Group:
        response = self.internal.groups.JoinGroup(request)
        self.manager.add_out_peer(response.group.out_peer)
        return Group.from_api(response.group)

    def __join_group_by_peer(self, request: groups_pb2.RequestJoinGroupByPeer) -> None:
        return self.internal.groups.JoinGroupByPeer(request)

    def __get_referenced_entities(self, request: sequence_and_updates_pb2.RequestGetReferencedEntitites) \
            -> ReferencedEntities:
        return self.internal.updates.GetReferencedEntitites(request)

    def __kick_user(self, request: groups_pb2.RequestKickUser) -> None:
        self.internal.groups.KickUser(request)

    def __invite_user(self, request: groups_pb2.RequestInviteUser) -> None:
        self.internal.groups.InviteUser(request)

    def __upload(self, file: str) -> media_and_files_pb2.FileLocation:
        return self.internal.uploading.upload_file(file)
