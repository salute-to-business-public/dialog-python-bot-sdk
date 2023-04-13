from dialog_bot_sdk.entity_manager import EntityManager
from dialog_bot_sdk.uploading import Uploading
from tests.fixtures.groups import Groups
from tests.fixtures.media_and_files import MediaAndFiles
from tests.fixtures.messaging import Messaging
from tests.fixtures.presence import Presence
from tests.fixtures.profile import Profile
from tests.fixtures.reactions import Reactions
from tests.fixtures.search import Search
from tests.fixtures.updates import Updates
from tests.fixtures.users import Users


class InternalBot:
    """Class with Dialog bot's internal services.

    """

    def __init__(self, verbose=False, cert=None, private_key=None, access_dir=None, options=None):
        self.messaging = Messaging()
        self.uploading = Uploading(self, cert, private_key, access_dir=access_dir)
        self.updates = Updates()
        self.media_and_files = MediaAndFiles()
        self.groups = Groups()
        self.search = Search()
        self.profile = Profile()
        self.users = Users()
        self.presence = Presence()
        self.reactions = Reactions()


internal = InternalBot()
manager = EntityManager(internal)
