from typing import List

from dialog_api import groups_pb2


class GroupPermission:
    GROUPADMINPERMISSION_EDITSHORTNAME = groups_pb2.GROUPADMINPERMISSION_EDITSHORTNAME
    GROUPADMINPERMISSION_INVITE = groups_pb2.GROUPADMINPERMISSION_INVITE
    GROUPADMINPERMISSION_KICK = groups_pb2.GROUPADMINPERMISSION_KICK
    GROUPADMINPERMISSION_UPDATEINFO = groups_pb2.GROUPADMINPERMISSION_UPDATEINFO
    GROUPADMINPERMISSION_SETPERMISSIONS = groups_pb2.GROUPADMINPERMISSION_SETPERMISSIONS
    GROUPADMINPERMISSION_EDITMESSAGE = groups_pb2.GROUPADMINPERMISSION_EDITMESSAGE
    GROUPADMINPERMISSION_DELETEMESSAGE = groups_pb2.GROUPADMINPERMISSION_DELETEMESSAGE
    GROUPADMINPERMISSION_GETINTEGRATIONTOKEN = groups_pb2.GROUPADMINPERMISSION_GETINTEGRATIONTOKEN
    GROUPADMINPERMISSION_SENDMESSAGE = groups_pb2.GROUPADMINPERMISSION_SENDMESSAGE
    GROUPADMINPERMISSION_PINMESSAGE = groups_pb2.GROUPADMINPERMISSION_PINMESSAGE
    GROUPADMINPERMISSION_VIEWMEMBERS = groups_pb2.GROUPADMINPERMISSION_VIEWMEMBERS


class Permissions:
    def __init__(self, user_id: int, permissions: List[GroupPermission]) -> None:
        self.user_id = user_id
        self.permissions = permissions

    @classmethod
    def from_api(cls, permissions: groups_pb2.GroupMemberPermission) -> 'Permissions':
        return cls(permissions.user_id, [x for x in permissions.permissions])

    def __dict__(self):
        return {"user_id": self.user_id, "permissions": self.permissions}

    def __str__(self):
        return "permissions: {}".format(self.__dict__())
