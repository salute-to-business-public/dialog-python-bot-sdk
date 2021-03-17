import logging
import grpc
import OpenSSL.crypto
import io
import copy

from grpc._channel import Channel

from .internal.bot import InternalBot
from .entity_manager import EntityManager
from .messaging import Messaging
from .updates import Updates
from .users import Users
from .groups import Groups
from .profile import Profile


DEFAULT_OPTIONS = {
    'grpc.keepalive_timeout_ms': 15000,
    'grpc.keepalive_time_ms': 30000,
    'grpc.keepalive_permit_without_calls': 1,
    'grpc.http2.max_pings_without_data': 0,
    'grpc.http2.min_time_between_pings_ms': 10000,
    'grpc.http2.min_ping_interval_without_data_ms': 5000,
    'grpc.min_reconnect_backoff_ms': 1000,
    'grpc.max_reconnect_backoff_ms': 30000
}


class DialogBot(object):
    """Main Dialog Bot class.
    """
    def __init__(self, channel: Channel, bot_token: str = None, verbose: bool = False, cert=None, private_key=None,
                 access_dir=None, options: dict = None):
        self.internal = InternalBot(channel, verbose=verbose, cert=cert, private_key=private_key, access_dir=access_dir,
                                    options=options)
        self.user_info = None
        if bot_token:
            self.user_info = self.internal.authorize(bot_token)
        else:
            self.user_info = self.internal.anonymous_authorize()
        self.manager = EntityManager(self.internal)
        self.groups = Groups(self.manager, self.internal)
        self.messaging = Messaging(self.manager, self.internal)
        self.updates = Updates(self.manager, self.internal)
        self.users = Users(self.manager, self.internal)
        self.profile = Profile(self.manager, self.internal)
        logging.info('Bot is ready.')

    @staticmethod
    def get_insecure_bot(endpoint: str, bot_token: str, verbose: bool = False, options: dict = None,
                         retry_options: dict = None) -> 'DialogBot':
        """Returns Dialog bot with established gRPC insecure channel.

        :param endpoint: bot's endpoint address
        :param bot_token: bot's token
        :param verbose: verbosity level of functions calling
        :param options: channel's options
        :param retry_options: dict of retries options (delay_factor, min_delay, max_delay, max_retries)
        :return: Dialog bot instance
        """
        options = DialogBot.__get_options(options)
        channel = grpc.insecure_channel(endpoint, options=options)
        return DialogBot(channel, bot_token, verbose=verbose, options=retry_options)

    @staticmethod
    def get_secure_bot(endpoint: str, credentials, bot_token: str, verbose: bool = False, options: dict = None,
                       retry_options: dict = None) -> 'DialogBot':
        """Returns Dialog bot with established gRPC insecure channel.

        :param endpoint: bot's endpoint address
        :param credentials: SSL credentials
        :param bot_token: bot's token
        :param verbose: verbosity level of functions calling
        :param options: channel's options
        :param retry_options: dict of retries options (delay_factor, min_delay, max_delay, max_retries)
        :return: Dialog bot instance
        """
        options = DialogBot.__get_options(options)
        channel = grpc.secure_channel(endpoint, credentials, options=options)
        return DialogBot(channel, bot_token, verbose=verbose, options=retry_options)

    @staticmethod
    def get_secure_bot_with_pfx_certificate(endpoint: str, pfx_certificate: str, pfx_password: str,
                                            verbose: bool = False, access_dir=None, options: dict = None,
                                            retry_options: dict = None) -> 'DialogBot':
        options = DialogBot.__get_options(options)
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
            ),
            options=options
        )

        private_key.seek(0)
        cert.seek(0)

        return DialogBot(channel, verbose=verbose, cert=cert.read(), private_key=private_key.read(),
                         access_dir=access_dir, options=retry_options)

    @staticmethod
    def __get_options(options: dict) -> list:
        options_dict = copy.deepcopy(DEFAULT_OPTIONS)
        if options:
            for key, value in options.items():
                options_dict[key] = value
        return list(options_dict.items())
