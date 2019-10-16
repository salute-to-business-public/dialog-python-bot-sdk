import random

from google.protobuf import wrappers_pb2

from .service import ManagedService
from dialog_api import search_pb2, groups_pb2, peers_pb2, sequence_and_updates_pb2, media_and_files_pb2


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

    def load_members(self, group_peer, limit=0):
        """User's list from group

        :param group_peer: group's peer
        :param limit: count members
        :return: list of User's
        """
        group_out_peer = self.get_group_outpeer(group_peer.id)
        request = groups_pb2.RequestLoadMembers(
            group=group_out_peer,
            limit=limit
        )
        members = self._load_members(request).members
        result = self.internal.updates.GetReferencedEntitites(
            sequence_and_updates_pb2.RequestGetReferencedEntitites(
                group_members=[
                    sequence_and_updates_pb2.GroupMembersSubset(
                        group_peer=group_out_peer,
                        member_ids=[member.uid for member in members]
                    )
                ]
            )
        )

        return result

    def kick_user(self, group_peer, user):
        """return response of KickUser

        :param group_peer: group's peer
        :param user: user's OutPeer
        :return: response
        """
        group_out_peer, user_out_peer = self.get_group_outpeer(group_peer.id), self.get_user_outpeer(user)
        return self.internal.groups.KickUser(
            groups_pb2.RequestKickUser(
                group_peer=group_out_peer,
                user=user_out_peer,
                rid=random.randint(0, 100000000),
            )
        )

    def invite_user(self, group_peer, user):
        """return response of InviteUser

        :param group_peer: group's peer
        :param user: user's OutPeer
        :return: response
        """
        group_out_peer = self.get_group_outpeer(group_peer.id)
        user_out_peer = self.get_user_outpeer(user)
        return self.internal.groups.InviteUser(
            groups_pb2.RequestInviteUser(
                group_peer=group_out_peer,
                user=user_out_peer,
                rid=random.randint(0, 100000000),
            )
        )

    def kick_users(self, group_peer, users):
        """return response list of KickUser

        :param group_peer: group's peer
        :param users: user's OutPeers
        :return: response list
        """
        result = []
        for user in users:
            result.append(self.kick_user(group_peer, user))
        return result

    def invite_users(self, group_peer, users):
        """return response list of InviteUser

        :param group_peer: group's peer
        :param users: user's OutPeers
        :return: response list
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
        :return: response list
        """
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []
        result = []
        group_out_peer = self.get_group_outpeer(group_peer.id)
        for permission in add_permissions:
            request = groups_pb2.RequestEditGroupBasePermissions(
                    group_peer=group_out_peer,
                    random_id=random.randint(0, 100000000),
                    granted_permissions=[self.permissions_map[permission]]
                )
            result.append(self._set_default_group_permissions(request))
        for permission in del_permissions:
            request = groups_pb2.RequestEditGroupBasePermissions(
                    group_peer=group_out_peer,
                    random_id=random.randint(0, 100000000),
                    revoked_permissions=[self.permissions_map[permission]]
                )
            result.append(self._set_default_group_permissions(request))
        return result

    def set_member_permissions(self, group_peer, user, add_permissions=None, del_permissions=None):
        """add/del group's member permissions

        :param group_peer: group's peer
        :param user: OutPeer of user
        :param add_permissions: list of permissions (on permissions_map) to add
        :param del_permissions: list of permissions (on permissions_map) to delete
        :return: response list
        """
        if del_permissions is None:
            del_permissions = []
        if add_permissions is None:
            add_permissions = []
        group_out_peer, user_out_peer = self.get_group_outpeer(group_peer.id), self.get_user_outpeer(user)
        result = []
        for permission in add_permissions:
            request = groups_pb2.RequestEditMemberPermissions(
                    group_peer=group_out_peer,
                    user_peer=user_out_peer,
                    granted_permissions=[self.permissions_map[permission]]
                )
            result.append(self._set_member_permissions(request))
        for permission in del_permissions:
            request = groups_pb2.RequestEditMemberPermissions(
                    group_peer=group_out_peer,
                    user_peer=user_out_peer,
                    revoked_permissions=[self.permissions_map[permission]]
                )
            result.append(self._set_member_permissions(request))
        return result

    def edit_avatar(self, group_id, file):
        outpeer = self.get_group_outpeer(group_id)
        location = self.internal.uploading.upload_file(file)
        request = groups_pb2.RequestEditGroupAvatar(
            group_peer=outpeer,
            rid=random.randint(0, 100000000),
            file_location=location
        )
        return self._edit_group_avatar(request)

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

    def _edit_group_avatar(self, request):
        return self.internal.groups.EditGroupAvatar(request)
