import time

from dialog_api import peers_pb2
from google.protobuf import wrappers_pb2


class FakeMessage:
    def __init__(self, mid):
        self.mid = mid
        self.date = int(time.time() / 1000)
        self.edited_at = wrappers_pb2.Int32Value(value=int(time.time() / 1000))


class FakeMessageFromSend:
    def __init__(self, mid):
        self.message_id = mid
        self.date = int(time.time() / 1000)
        self.edited_at = wrappers_pb2.Int32Value(value=int(time.time() / 1000))


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
    def __init__(self, shortname=None):
        self.groups = ["group"]
        self.peer = "peer"
        self.search_results = [FakeSearchResult(shortname)]


class FakeSearchResult:
    def __init__(self, shortname=None):
        self.peer = peers_pb2.Peer(id=0, type=peers_pb2.PEERTYPE_GROUP)
        self.shortname = wrappers_pb2.StringValue(value=shortname)


class FakeEntities:
    def __init__(self):
        self.messages = ["your message"]


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


class FakeMembers:
    def __init__(self):
        self.members = [FakeOutpeer()]
