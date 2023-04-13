from dialog_api.users_pb2 import RequestLoadFullUsers, ResponseLoadFullUsers, RequestLoadUserData, ResponseLoadUserData

from tests.fixtures.server_entities import full_user, user


class Users:
    def LoadFullUsers(self, request: RequestLoadFullUsers) -> ResponseLoadFullUsers:
        return ResponseLoadFullUsers(full_users=[full_user])

    def LoadUserData(self, request: RequestLoadUserData) -> ResponseLoadUserData:
        return ResponseLoadUserData(users=[user])
