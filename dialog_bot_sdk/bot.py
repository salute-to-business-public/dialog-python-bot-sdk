import grpc
import OpenSSL.crypto
import io

from .internal.bot import InternalBot
from .entity_manager import EntityManager
from .messaging import Messaging
from .updates import Updates
from .uploading import Uploading
from .users import Users


class DialogBot(object):
    """Main Dialog Bot class.

    """
    def __init__(self, channel, bot_token=None):
        self.internal = InternalBot(channel)
        self.user_info = None
        if bot_token:
            self.user_info = self.internal.authorize(bot_token)
        else:
            self.user_info = self.internal.anonymous_authorize()
        self.manager = EntityManager(self.internal)
        self.messaging = Messaging(self.manager, self.internal)
        self.uploading = Uploading(self.internal)
        self.updates = Updates(self.manager, self.internal)
        self.users = Users(self.manager, self.internal)
        print('Bot is ready.')

    @staticmethod
    def get_insecure_bot(endpoint, bot_token):
        """Returns Dialog bot with established gRPC insecure channel.

        :param endpoint: bot's endpoint address
        :param bot_token: bot's token
        :return: Dialog bot instance
        """
        channel = grpc.insecure_channel(endpoint)
        return DialogBot(channel, bot_token)

    @staticmethod
    def get_secure_bot(endpoint, credentials, bot_token):
        """Returns Dialog bot with established gRPC insecure channel.

        :param endpoint: bot's endpoint address
        :param credentials: SSL credentials
        :param bot_token: bot's token
        :return: Dialog bot instance
        """
        channel = grpc.secure_channel(endpoint, credentials)
        return DialogBot(channel, bot_token)

    @staticmethod
    def get_secure_bot_with_pfx_certificate(endpoint, pfx_certificate, pfx_password):
        pfx1 = open(pfx_certificate, 'rb').read()
        p12 = OpenSSL.crypto.load_pkcs12(pfx1, pfx_password)

        private_key = io.BytesIO()
        cert = io.BytesIO()

        private_key.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
        cert.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))

        private_key.seek(0)
        cert.seek(0)

        channel = grpc.secure_channel(
            endpoint,
            grpc.ssl_channel_credentials(
                root_certificates=None,
                private_key=private_key.read(),
                certificate_chain=cert.read()
            )
        )

        return DialogBot(channel)
