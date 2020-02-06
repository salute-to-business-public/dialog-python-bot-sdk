from typing import List

from dialog_api import groups_pb2

PERMISSIONS_TO_STRING = {
    groups_pb2.GROUPADMINPERMISSION_EDITSHORTNAME: 'edit_shortname',
    groups_pb2.GROUPADMINPERMISSION_INVITE: 'invite',
    groups_pb2.GROUPADMINPERMISSION_KICK: 'kick',
    groups_pb2.GROUPADMINPERMISSION_UPDATEINFO: 'update_info',
    groups_pb2.GROUPADMINPERMISSION_SETPERMISSIONS: 'set_permissions',
    groups_pb2.GROUPADMINPERMISSION_EDITMESSAGE: 'edit_message',
    groups_pb2.GROUPADMINPERMISSION_DELETEMESSAGE: 'delete_message',
    groups_pb2.GROUPADMINPERMISSION_GETINTEGRATIONTOKEN: 'get_integration_token',
    groups_pb2.GROUPADMINPERMISSION_SENDMESSAGE: 'send_message',
    groups_pb2.GROUPADMINPERMISSION_PINMESSAGE: 'pin_message',
    groups_pb2.GROUPADMINPERMISSION_VIEWMEMBERS: 'view_members',
}


class Permissions:
    def __init__(self, user_id: int, permissions: List[str]) -> None:
        self.user_id = user_id
        self.permissions = permissions

    @classmethod
    def from_api(cls, permissions: groups_pb2.GroupMemberPermission) -> 'Permissions':
        return cls(permissions.user_id, [PERMISSIONS_TO_STRING[x] for x in permissions.permissions])
