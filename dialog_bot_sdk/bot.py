import grpc
from .internal.bot import InternalBot
from .entity_manager import EntityManager
from .messaging import Messaging
from .updates import Updates


class DialogBot(object):
    """Main Dialog Bot class.

    """
    def __init__(self, channel, bot_token):
        self.internal = InternalBot(channel)
        # TODO: analyze auth errors
        self.internal.authorize(bot_token)
        self.manager = EntityManager(self.internal)
        self.messaging = Messaging(self.manager, self.internal)
        self.updates = Updates(self.manager, self.internal)

    @staticmethod
    def get_insecure_bot(endpoint, bot_token):
        """Returns Dialog bot with established gRPC insecure channel.

        :param endpoint: bot's endpoint address
        :param bot_token: bot's token
        :return: Dialog bot instance
        """
        channel = grpc.insecure_channel(endpoint)
        return DialogBot(channel, bot_token)
