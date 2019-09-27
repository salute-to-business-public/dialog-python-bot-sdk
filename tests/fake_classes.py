import time


class FakeMessage:
    def __init__(self, mid):
        self.mid = mid
        self.date = int(time.time() - 1000)


class FakeDialog:
    def __init__(self):
        self.user_peers = [FakeOutpeer()]


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
