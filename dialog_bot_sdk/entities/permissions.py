from typing import List

from dialog_api import permissions_pb2


class Permission:
    PERMISSION_UNKNOWN = permissions_pb2.PERMISSION_UNKNOWN
    PERMISSION_SEARCH = permissions_pb2.PERMISSION_SEARCH
    PERMISSION_CREATE_GROUPS = permissions_pb2.PERMISSION_CREATE_GROUPS
    PERMISSION_LEAVE_GROUPS = permissions_pb2.PERMISSION_LEAVE_GROUPS
    PERMISSION_LANDLINE_CALL = permissions_pb2.PERMISSION_LANDLINE_CALL
    PERMISSION_DELETE_ANY_P2P_MESSAGE = permissions_pb2.PERMISSION_DELETE_ANY_P2P_MESSAGE


# updates
class UpdatePermissionsChange:
    def __init__(self, permissions: List[Permission], clock: int) -> None:
        self.permissions = permissions
        self.clock = clock

    @classmethod
    def from_api(cls, update: permissions_pb2.UpdatePermissionsChange) -> 'UpdatePermissionsChange':
        return cls(update.permissions, update.clock)

    def __dict__(self):
        return {
            "permissions": self.permissions,
            "clock": self.clock,
        }

    def __str__(self):
        return "UpdatePermissionsChange({})".format(self.__dict__())
