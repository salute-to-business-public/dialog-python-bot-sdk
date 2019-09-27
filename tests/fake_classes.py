import time


class FakeMessage:
    def __init__(self, mid):
        self.mid = mid
        self.date = int(time.time() - 1000)


class FakeDialog:
    def __init__(self, user_peers=None, group_peers=None):
        if user_peers:
            self.user_peers = user_peers
        else:
            self.user_peers = [FakeOutpeer()]
        if group_peers:
            self.group_peers = group_peers
        else:
            self.group_peers = [FakeOutpeer()]


class FakeOutpeer:
    def __init__(self):
        self.uid = 0
        self.access_hash = 0


class FakeUsers:
    def __init__(self, nick):
        self.users = [FakeUser(nick)]


class FakeUser:
    def __init__(self, nick):
        self.data = FakeUserData(nick)
        self.id = 0
        self.access_hash = 0


class FakeUserData:
    def __init__(self, nick):
        self.nick = FakeUserDataValue(nick)


class FakeUserDataValue:
    def __init__(self, nick):
        self.value = nick


class FakeFullProfile:
    def __init__(self, full_users=None):
        if full_users:
            self.full_users = full_users


class FakeFullUser:
    def __init__(self, custom_profile=None):
        if custom_profile:
            self.custom_profile = custom_profile


class FakeSearch:
    def __init__(self):
        self.groups = ["group"]
        self.peer = "peer"


class FakeState:
    def __init__(self):
        self.seq = 1


class FakeUrl:
    def __init__(self):
        self.url = "url"


class FakePut:
    def __init__(self, status_code=None, upload_key=None, uploaded_file_location=None):
        self.status_code = status_code
        self.upload_key = upload_key
        self.uploaded_file_location = uploaded_file_location
