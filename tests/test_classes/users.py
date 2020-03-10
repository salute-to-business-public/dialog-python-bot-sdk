from dialog_api.users_pb2 import RequestLoadFullUsers, ResponseLoadFullUsers, FullUser


class Users:
    def LoadFullUsers(self, request: RequestLoadFullUsers) -> ResponseLoadFullUsers:
        return ResponseLoadFullUsers(full_users=[FullUser(id=1, contact_info=[], about=None)])
