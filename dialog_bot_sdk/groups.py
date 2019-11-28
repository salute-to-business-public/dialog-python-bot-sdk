import random
from google.protobuf import wrappers_pb2

from .service import ManagedService
from dialog_api import search_pb2, groups_pb2, peers_pb2, sequence_and_updates_pb2


class Groups(ManagedService):
    """Class for handling groups

    """
    permissions_map = {
        'edit_shortname': groups_pb2.GROUPADMINPERMISSION_EDITSHORTNAME,
        'invite': groups_pb2.GROUPADMINPERMISSION_INVITE,
        'kick': groups_pb2.GROUPADMINPERMISSION_KICK,
        'update_info': groups_pb2.GROUPADMINPERMISSION_UPDATEINFO,
        'set_permissions': groups_pb2.GROUPADMINPERMISSION_SETPERMISSIONS,
        'edit_message': groups_pb2.GROUPADMINPERMISSION_EDITMESSAGE,
        'delete_message': groups_pb2.GROUPADMINPERMISSION_DELETEMESSAGE,
        'get_integration_token': groups_pb2.GROUPADMINPERMISSION_GETINTEGRATIONTOKEN,
        'send_message': groups_pb2.GROUPADMINPERMISSION_SENDMESSAGE,
        'pin_message': groups_pb2.GROUPADMINPERMISSION_PINMESSAGE,
        'view_members': groups_pb2.GROUPADMINPERMISSION_VIEWMEMBERS,
    }

    def create_public_group(self, title, shortname):
        """Create public group

        :param title: title of group
        :param shortname: group name
        :return: group
        """

        request = groups_pb2.RequestCreateGroup(
            title=title,
            username=wrappers_pb2.StringValue(value=shortname),
            group_type=groups_pb2.GROUPTYPE_GROUP
        )
        return self._create_group(request)

    def create_private_group(self, title):
        """Create private group

        :param title: title of group
        :return: group
        """
        request = groups_pb2.RequestCreateGroup(
            title=title,
            group_type=groups_pb2.GROUPTYPE_GROUP
        )
        return self._create_group(request)

    def create_public_channel(self, title, shortname):
        """Create public channel

        :param title: title of group
        :param shortname: group name
        :return: group
        """

        request = groups_pb2.RequestCreateGroup(
            title=title,
            username=wrappers_pb2.StringValue(value=shortname),
            group_type=groups_pb2.GROUPTYPE_CHANNEL
        )
        return self._create_group(request)

    def create_private_channel(self, title):
        """Create private channel

        :param title: title of group
        :return: group
        """

        request = groups_pb2.RequestCreateGroup(
            title=title,
            group_type=groups_pb2.GROUPTYPE_CHANNEL
        )
        return self._create_group(request)

    def find_group_by_shortname(self, query):
        """Find a groups by shortname

        :param query: shortname of group
        :return: Group
        """
        request = search_pb2.RequestPeerSearch(
            query=[
                search_pb2.SearchCondition(
                    searchPeerTypeCondition=search_pb2.SearchPeerTypeCondition(
                        peer_type=search_pb2.SEARCHPEERTYPE_GROUPS
                    )
                ),
                search_pb2.SearchCondition(
                    searchPieceText=search_pb2.SearchPieceText(query=query)
                )
            ]
        )
        response = self._peer_search(request).search_results
        for result in response:
            if result.peer.type == peers_pb2.PEERTYPE_GROUP:
                if hasattr(result, 'shortname'):
                    if result.shortname.value == query:
                        return result

    def find_group_by_id(self, group_id):
        """search and return group by id

        :param group_id: group's
        :return: Group
        """
        group_out_peer = self.get_group_outpeer(group_id)

        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            groups=[group_out_peer]
        )
        result = self._get_referenced_entities(request).groups
        return result[0]

    def load_members(self, group_peer, limit=0):
        """User's list from group

        :param group_peer: group's Peer
        :param limit: count members
        :return: list of User's
        """
        group_out_peer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestLoadMembers(
            group=group_out_peer,
            limit=limit
        )
        members = self._load_members(request).members
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                group_members=[
                    sequence_and_updates_pb2.GroupMembersSubset(
                        group_peer=group_out_peer,
                        member_ids=[member.uid for member in members]
                    )
                ]
            )
        result = self._get_referenced_entities(request)

        return result

    def kick_user(self, group_peer, user):
        """return response of KickUser

        :param group_peer: group's Peer
        :param user: user's OutPeer
        :return: response (date, mid)
        """
        group_out_peer, user_out_peer = self.get_group_outpeer(group_peer.id), self.get_user_outpeer(user)
        request = groups_pb2.RequestKickUser(
                group_peer=group_out_peer,
                user=user_out_peer,
                rid=random.randint(0, 100000000),
            )
        return self._kick_user(request)

    def invite_user(self, group_peer, user):
        """return response of InviteUser

        :param group_peer: group's Peer
        :param user: user's OutPeer
        :return: response (date, mid)
        """
        group_out_peer = self.get_group_outpeer(group_peer.id)
        user_out_peer = self.get_user_outpeer(user)
        request = groups_pb2.RequestInviteUser(
                group_peer=group_out_peer,
                user=user_out_peer,
                rid=random.randint(0, 100000000),
            )
        return self._invite_user(request)

    def kick_users(self, group_peer, users):
        """return response list of KickUser

        :param group_peer: group's Peer
        :param users: user's OutPeers
        :return: response list (date, mid)
        """
        result = []
        for user in users:
            result.append(self.kick_user(group_peer, user))
        return result

    def invite_users(self, group_peer, users):
        """return response list of InviteUser

        :param group_peer: group's Peer
        :param users: user's OutPeers
        :return: response list (date, mid)
        """
        result = []
        for user in users:
            result.append(self.invite_user(group_peer, user))
        return result

    def set_default_group_permissions(self, group_peer, add_permissions=None, del_permissions=None):
        """add/del default group permissions

        :param group_peer: group's peer
        :param add_permissions: list of permissions (on permissions_map) to add
        :param del_permissions: list of permissions (on permissions_map) to delete
        :return: None
        """
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []

        group_out_peer = self.get_group_outpeer(group_peer.id)
        for permission in add_permissions:
            request = groups_pb2.RequestEditGroupBasePermissions(
                    group_peer=group_out_peer,
                    random_id=random.randint(0, 100000000),
                    granted_permissions=[self.permissions_map[permission]]
                )
            self._set_default_group_permissions(request)
        for permission in del_permissions:
            request = groups_pb2.RequestEditGroupBasePermissions(
                    group_peer=group_out_peer,
                    random_id=random.randint(0, 100000000),
                    revoked_permissions=[self.permissions_map[permission]]
                )
            self._set_default_group_permissions(request)

    def set_member_permissions(self, group_peer, user, add_permissions=None, del_permissions=None):
        """add/del group's member permissions

        :param group_peer: group's peer
        :param user: OutPeer of user
        :param add_permissions: list of permissions (on permissions_map) to add
        :param del_permissions: list of permissions (on permissions_map) to delete
        :return: None
        """
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []
        group_out_peer, user_out_peer = self.get_group_outpeer(group_peer.id), self.get_user_outpeer(user)
        for permission in add_permissions:
            request = groups_pb2.RequestEditMemberPermissions(
                    group_peer=group_out_peer,
                    user_peer=user_out_peer,
                    granted_permissions=[self.permissions_map[permission]]
                )
            self._set_member_permissions(request)
        for permission in del_permissions:
            request = groups_pb2.RequestEditMemberPermissions(
                    group_peer=group_out_peer,
                    user_peer=user_out_peer,
                    revoked_permissions=[self.permissions_map[permission]]
                )
            self._set_member_permissions(request)

    def get_group_member_permissions(self, group_peer, user_peers):
        """return group member's permissions

        :param group_peer: Group's Peer
        :param user_peers: User's Peer
        :return: group member's permissions
        """
        if type(user_peers) != list:
            user_peers = [user_peers]
        request = groups_pb2.RequestGetGroupMemberPermissions(
            group_id=group_peer.id,
            user_ids=[peer.id for peer in user_peers]
        )
        return self._get_group_member_permissions(request)

    def edit_group_title(self, group_peer, title):
        """change group's title

        :param group_peer: group's Peer
        :param title: new title (string)
        :return: response (seq, date, mid)
        """
        outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestEditGroupTitle(
            group_peer=outpeer,
            rid=random.randint(0, 100000000),
            title=title
        )
        return self._edit_group_title(request)

    def edit_avatar(self, group_id, file):
        """change group's avatar

        :param group_id: group's id
        :param file: file path
        :return: response (avatar, seq, date, mid)
        """
        outpeer = self.get_group_outpeer(group_id)
        location = self._upload(file)
        request = groups_pb2.RequestEditGroupAvatar(
            group_peer=outpeer,
            rid=random.randint(0, 100000000),
            file_location=location
        )
        return self._edit_group_avatar(request)

    def remove_group_avatar(self, group_peer):
        """deleted group's avatar

        :param group_peer: group's Peer
        :return: response (seq, date, mid)
        """
        outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestRemoveGroupAvatar(
            group_peer=outpeer,
            rid=random.randint(0, 100000000),
        )
        return self._remove_group_avatar(request)

    def edit_group_about(self, group_peer, about):
        """change group's "about"

        :param group_peer: group's peer
        :param about: about text (string)
        :return: response (seq, date)
        """
        outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestEditGroupAbout(
            group_peer=outpeer,
            rid=random.randint(0, 100000000),
            about=wrappers_pb2.StringValue(value=about)
        )
        return self._edit_group_about(request)

    def leave_group(self, group_peer):
        """leave from group

        :param group_peer: group's Peer
        :return: response (date, mid)
        """
        outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestLeaveGroup(
            group_peer=outpeer,
            rid=random.randint(0, 100000000),
        )
        return self._leave_group(request)

    def make_user_admin(self, group_peer, user_peer, permissions):
        """Set new user's permissions (old permissions will be revoke)

        :param group_peer: group's Peer
        :param user_peer: user's Peer
        :param permissions: permissions list (for admin)
        :return: None
        """
        group_outpeer = self.get_group_outpeer(group_peer.id)
        outpeer = self.manager.get_outpeer(user_peer)
        user_outpeer = self.get_user_outpeer(outpeer)
        request = groups_pb2.RequestMakeUserAdmin(
            group_peer=group_outpeer,
            user_peer=user_outpeer,
            permissions=[self.permissions_map[permission] for permission in permissions]
        )
        self._make_user_admin(request)

    def transfer_ownership(self, group_peer, user_peer):
        """change group's owner to user

        :param group_peer: group's Peer
        :param user_peer: user's Peer
        :return: seq
        """
        group_outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestTransferOwnership(
            group_peer=group_outpeer,
            new_owner=user_peer.id
        )
        return self._transfer_ownership(request)  # return seq

    def get_group_invite_url(self, group_peer):
        """return group's invite url

        :param group_peer: Peer
        :return: invite url (string)
        """
        group_outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestGetGroupInviteUrl(
            group_peer=group_outpeer
        )
        return self._get_group_invite_url(request).url

    def get_group_invite_url_base(self):
        """return group's invite url without token/shortname (example https://domain/@)

        :return: invite url (string)
        """
        request = groups_pb2.RequestGetGroupInviteUrlBase()
        return self._get_group_invite_url_base(request).url

    def revoke_invite_url(self, group_peer):
        """revoke current invite url and return new group's invite url

        :return: invite url (string)
        """
        group_outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestRevokeInviteUrl(
            group_peer=group_outpeer
        )
        return self._revoke_invite_url(request).url

    def join_group(self, token_or_url):
        """join to group by token or invite url (used for private groups)

        :param token_or_url: group's token or invite url
        :return: response (group, date, mid)
        """
        request = groups_pb2.RequestJoinGroup(
            token=token_or_url
        )
        return self._join_group(request)

    def join_group_by_peer(self, group_peer):
        """join to group by group's peer (used for public groups)

        :param group_peer: Peer
        :return: None
        """
        group_outpeer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestJoinGroupByPeer(
            peer=group_outpeer
        )
        self._join_group_by_peer(request)

    def get_group_outpeer(self, group_id):
        """return GroupOutPeer object

        :param group_id: group's id
        :return: GroupOutPeer
        """
        gop = self.manager.get_outpeer(peers_pb2.Peer(id=group_id, type=peers_pb2.PEERTYPE_GROUP))
        return peers_pb2.GroupOutPeer(group_id=gop.id, access_hash=gop.access_hash)

    def get_outpeer(self, group_id):
        """return OutPeer object

        :param group_id: group's id
        :return: OutPeer
        """
        request = peers_pb2.Peer(id=group_id, type=peers_pb2.PEERTYPE_GROUP)
        return self.manager.get_outpeer(request)

    @staticmethod
    def get_user_outpeer(user):
        """return UserOutPeer object

        :param user: OutPeer
        :return: UserOutPeer
        """
        return peers_pb2.UserOutPeer(uid=user.id, access_hash=user.access_hash)

    def _create_group(self, request):
        """return Group by RequestCreateGroup

        :param request: RequestCreateGroup
        :return: Group
        """
        group = self.internal.groups.CreateGroup(request).group
        self.manager.adopt_peer(peers_pb2.GroupOutPeer(group_id=group.id, access_hash=group.access_hash))
        return group

    def _peer_search(self, request):
        return self.internal.search.PeerSearch(request)

    def _load_members(self, request):
        return self.internal.groups.LoadMembers(request)

    def _set_default_group_permissions(self, request):
        return self.internal.groups.EditGroupBasePermissions(request)

    def _set_member_permissions(self, request):
        return self.internal.groups.EditMemberPermissions(request)

    def _get_group_member_permissions(self, request):
        return self.internal.groups.GetGroupMemberPermissions(request)

    def _edit_group_title(self, request):
        return self.internal.groups.EditGroupTitle(request)

    def _edit_group_avatar(self, request):
        return self.internal.groups.EditGroupAvatar(request)

    def _remove_group_avatar(self, request):
        return self.internal.groups.RemoveGroupAvatar(request)

    def _edit_group_about(self, request):
        return self.internal.groups.EditGroupAbout(request)

    def _leave_group(self, request):
        return self.internal.groups.LeaveGroup(request)

    def _make_user_admin(self, request):
        return self.internal.groups.MakeUserAdmin(request)

    def _transfer_ownership(self, request):
        return self.internal.groups.TransferOwnership(request)

    def _get_group_invite_url(self, request):
        return self.internal.groups.GetGroupInviteUrl(request)

    def _get_group_invite_url_base(self, request):
        return self.internal.groups.GetGroupInviteUrlBase(request)

    def _revoke_invite_url(self, request):
        return self.internal.groups.RevokeInviteUrl(request)

    def _join_group(self, request):
        return self.internal.groups.JoinGroup(request)

    def _join_group_by_peer(self, request):
        return self.internal.groups.JoinGroupByPeer(request)

    def _get_referenced_entities(self, request):
        return self.internal.updates.GetReferencedEntitites(request)

    def _kick_user(self, request):
        return self.internal.groups.KickUser(request)

    def _invite_user(self, request):
        return self.internal.groups.InviteUser(request)

    def _upload(self, file):
        return self.internal.uploading.upload_file(file)
