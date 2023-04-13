from concurrent.futures.thread import ThreadPoolExecutor
import grpc
import OpenSSL.crypto
import io
import copy
from dialog_bot_sdk.entities.peers import PeerType
from dialog_bot_sdk.entities.messaging import CommandHandler, UpdateMessage
from grpc._channel import Channel
from .entities.authentication import UserInfo
from .favourites_messages import FavouritesMessages
from .internal.bot import InternalBot
from .entity_manager import EntityManager
from .messaging import Messaging
from .pinned_messages import PinnedMessages
from .presence import Presence
from .reactions import Reactions
from .stickers import Stickers
from .threads import Threads
from .updates import Updates
from .users import Users
from .groups import Groups
from .profile import Profile
from .utils import default_logger_config

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
    def __init__(self, channel: Channel, **kwargs) -> None:
        """Init DialogBot class.

        Args:
            :param channel: bot's channel (grpc._channel.Channel)
        Kwargs:
            bot_token: bot's token (str)
            verbose: verbosity level of functions calling (bool)
            cert: bot's certificate (str)
            private_key: bot's private_key (str)
            access_dir: bot's access_dir (str)
            retry_options: dict of retries options (delay_factor, min_delay, max_delay, max_retries) (dict)
            rate_limiter_options: dict of rate limiter options (max_calls, period) (dict)
            stop_updates: dict of stop_updates command (command - str default "stop_updates",
                                                        uids - list of user ids who can use it)
            logger_config: dict of logger config (level - log level, stream_handler_level - log level,
                                                  stream_log_format - logging format)
        Returns: None
        """
        kwargs["logger_config"] = self.__get_logger_config(kwargs.get("logger_config"))
        self.internal = InternalBot(channel, **kwargs)
        self.user_info = None

        if kwargs.get("bot_token"):
            user_info = self.internal.authorize(kwargs.get("bot_token"))
        else:
            user_info = self.internal.anonymous_authorize()

        self.user_info = UserInfo.from_api(user_info)

        if kwargs.get("update_pool"):
            self.update_pool = ThreadPoolExecutor(max_workers=kwargs["update_pool"])
        else:
            self.update_pool = ThreadPoolExecutor(max_workers=10)

        user_info = self.internal.authorize(kwargs.get("bot_token")) if "bot_token" in kwargs else \
            self.internal.anonymous_authorize()
        self.user_info = UserInfo.from_api(user_info)
        self.update_pool = ThreadPoolExecutor(max_workers=kwargs["update_pool"] if "update_pool" in kwargs else 10)
        self.methods_pool = ThreadPoolExecutor(max_workers=kwargs["methods_pool"] if "methods_pool" in kwargs else 10)
        self.manager = EntityManager(
            self.internal, self.update_pool, self.methods_pool, self.user_info, kwargs["logger_config"]
        )
        self.groups = Groups(self.manager, self.internal)
        self.messaging = Messaging(self.manager, self.internal)
        self.updates = Updates(self.manager, self.internal)
        self.users = Users(self.manager, self.internal)
        self.profile = Profile(self.manager, self.internal)
        self.reactions = Reactions(self.manager, self.internal)
        self.presence = Presence(self.manager, self.internal)
        self.favourites_messages = FavouritesMessages(self.manager, self.internal)
        self.pinned_messages = PinnedMessages(self.manager, self.internal)
        self.threads = Threads(self.manager, self.internal)
        self.stickers = Stickers(self.manager, self.internal)
        if kwargs.get("stop_updates") is not None:
            if "uids" not in kwargs["stop_updates"] or not isinstance(kwargs["stop_updates"]["uids"], list):
                raise AttributeError("uids in stop_updates must be list")
            if not kwargs["stop_updates"]["uids"]:
                raise AttributeError("uids in stop_updates must be not empty")
            self.manager.stop_updates_uids = kwargs["stop_updates"]["uids"]
            self.messaging.command_handler(
                [
                    CommandHandler(
                        self.__stop_updates,
                        kwargs["stop_updates"].get("command") if kwargs["stop_updates"].get("command") is not None
                        else "stop_updates",
                        PeerType.PEERTYPE_PRIVATE,
                        True
                    )
                ]
            )

    @staticmethod
    def get_insecure_bot(endpoint: str, token: str, **kwargs) -> 'DialogBot':
        """Returns Dialog bot with established gRPC insecure channel.

        Args:
            :param token: bot's token
            :param endpoint: bot's endpoint address
        Kwargs:
            verbose: verbosity level of functions calling (bool)
            options: channel's options (dict)
            retry_options: dict of retries options (delay_factor, min_delay, max_delay, max_retries) (dict)
            rate_limiter_options: dict of rate limiter options (max_calls, period) (dict)
            stop_updates: dict of stop_updates command (command - str default "stop_updates",
                                                        uids - list of user ids who can use it)
            logger_config: dict of logger config (level - log level, stream_handler_level - log level,
                                                  stream_log_format - logging format)
        Returns: Dialog bot instance
        """
        options = DialogBot.__get_options(kwargs.get("options"))
        channel = grpc.insecure_channel(endpoint, options=options)
        kwargs["bot_token"] = token
        return DialogBot(channel, **kwargs)

    @staticmethod
    def get_secure_bot(endpoint: str, credentials: grpc.ssl_channel_credentials, bot_token: str, **kwargs) \
            -> 'DialogBot':
        """Returns Dialog bot with established gRPC insecure channel.

        Args:
            :param endpoint: bot's endpoint address
            :param credentials: SSL credentials
            :param bot_token: bot's token
        Kwargs:
            verbose: verbosity level of functions calling (bool)
            options: channel's options (dict)
            retry_options: dict of retries options (delay_factor, min_delay, max_delay, max_retries) (dict)
            rate_limiter_options: dict of rate limiter options (max_calls, period) (dict)
            root_certificates: path to PEM-encoded certificates
            stop_updates: dict of stop_updates command (command - str default "stop_updates",
                                                        uids - list of user ids who can use it)
            logger_config: dict of logger config (level - log level, stream_handler_level - log level,
                                                  stream_log_format - logging format)
         Returns: Dialog bot instance
        """
        options = DialogBot.__get_options(kwargs.get("options"))
        root_certificates = DialogBot.get_root_certificates(kwargs.get("root_certificates"))
        if root_certificates is not None:
            credentials = grpc.ssl_channel_credentials(root_certificates=root_certificates)
        channel = grpc.secure_channel(endpoint, credentials, options=options)
        kwargs["bot_token"] = bot_token
        return DialogBot(channel, **kwargs)

    @staticmethod
    def get_secure_bot_with_pfx_certificate(endpoint: str, pfx_certificate: str, pfx_password: str, **kwargs) \
            -> 'DialogBot':
        """Returns Dialog bot with established gRPC insecure channel.

        Args:
            :param endpoint: bot's endpoint address
            :param pfx_certificate: bot's certificate path
            :param pfx_password: bot's certificate password
        Kwargs:
            verbose: verbosity level of functions calling (bool)
            access_dir: bot's access_dir (str)
            options: channel's options (dict)
            retry_options: dict of retries options (delay_factor, min_delay, max_delay, max_retries) (dict)
            rate_limiter_options: dict of rate limiter options (max_calls, period) (dict)
            root_certificates: path to PEM-encoded certificates
            stop_updates: dict of stop_updates command (command - str default "stop_updates",
                                                        uids - list of user ids who can use it)
            logger_config: dict of logger config (level - log level, stream_handler_level - log level,
                                                  stream_log_format - logging format)
        Returns: Dialog bot instance
        """
        options = DialogBot.__get_options(kwargs.get("options"))
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
                root_certificates=DialogBot.get_root_certificates(kwargs.get("root_certificates")),
                private_key=private_key.read(),
                certificate_chain=cert.read()
            ),
            options=options
        )

        private_key.seek(0)
        cert.seek(0)

        kwargs["cert"] = cert.read()
        kwargs["private_key"] = private_key.read()

        return DialogBot(channel, **kwargs)

    @staticmethod
    def __get_options(options: dict) -> list:
        options_dict = copy.deepcopy(DEFAULT_OPTIONS)
        if options:
            for key, value in options.items():
                options_dict[key] = value
        return list(options_dict.items())

    @staticmethod
    def get_root_certificates(root_certificates_path: str or None) -> None or bytes:
        root_certificates = None
        if root_certificates_path is not None:
            with open(root_certificates_path, 'r') as f:
                root_certificates = f.read().encode()
        return root_certificates

    def __stop_updates(self, message: UpdateMessage) -> None:
        if message.peer.id in self.manager.stop_updates_uids:
            self.updates.stop()

    @staticmethod
    def __get_logger_config(logger_config: dict or None) -> dict:
        default = copy.deepcopy(default_logger_config)

        if logger_config is None:
            return default

        default["level"] = default["level"] if logger_config.get("level") is None else logger_config.get("level")
        default["stream_handler_level"] = default["stream_handler_level"] \
            if logger_config.get("stream_handler_level") is None else logger_config.get("stream_handler_level")
        default["stream_log_format"] = default["stream_log_format"] \
            if logger_config.get("stream_log_format") is None else logger_config.get("stream_log_format")

        return default
