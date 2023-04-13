import math

from ratelimiter import RateLimiter
from .service import AuthenticatedService
from dialog_api import registration_pb2, registration_pb2_grpc, \
    sequence_and_updates_pb2_grpc, \
    authentication_pb2, authentication_pb2_grpc, \
    contacts_pb2_grpc, search_pb2_grpc, messaging_pb2_grpc, \
    media_and_files_pb2_grpc, users_pb2_grpc, groups_pb2_grpc, profile_pb2_grpc, presence_pb2_grpc, reactions_pb2_grpc, \
    favourites_messages_pb2_grpc, pinned_messages_pb2_grpc, threads_pb2_grpc, stickers_pb2_grpc
from dialog_bot_sdk.uploading import Uploading
from ..downloading import Downloading
from ..utils import get_logger

DEFAULT_OPTIONS_RATE_LIMITER = {
    "max_calls": 100,
    "period": 1,  # in seconds
}
DEFAULT_OPTIONS_RETRY = {
    "min_delay": 1,
    "max_delay": 50,
    "delay_factor": math.exp(1),
    "max_retries": 10
}


class InternalBot(object):
    """Class with Dialog bot's internal services.

    """
    def __init__(self, channel, **kwargs) -> None:
        self.app_id = 10
        self.app_title = "PythonBotSDK/1.0"
        self.channel = channel
        rl_options = self.parse_options(kwargs.get("rate_limiter_options"), DEFAULT_OPTIONS_RATE_LIMITER)
        rate_limiter = RateLimiter(max_calls=rl_options["max_calls"], period=rl_options["period"])
        retry_options = self.parse_options(kwargs.get("retry_options"), DEFAULT_OPTIONS_RETRY)
        kv_wrap = {
            "verbose": kwargs.get("verbose"), "retry_options": retry_options, "rate_limiter": rate_limiter,
            "logger": get_logger("dialog_bot_sdk.internal.service", kwargs["logger_config"])
        }
        self.registration = self.wrap_service(registration_pb2_grpc.RegistrationStub, **kv_wrap)
        self.updates = self.wrap_service(sequence_and_updates_pb2_grpc.SequenceAndUpdatesStub, **kv_wrap)
        self.auth = self.wrap_service(authentication_pb2_grpc.AuthenticationStub, **kv_wrap)
        kv_wrap["timeout"] = kwargs.get("timeout")
        self.messaging = self.wrap_service(messaging_pb2_grpc.MessagingStub, **kv_wrap)
        self.media_and_files = self.wrap_service(media_and_files_pb2_grpc.MediaAndFilesStub, **kv_wrap)
        self.contacts = self.wrap_service(contacts_pb2_grpc.ContactsStub, **kv_wrap)
        self.search = self.wrap_service(search_pb2_grpc.SearchStub, **kv_wrap)
        self.users = self.wrap_service(users_pb2_grpc.UsersStub, **kv_wrap)
        self.groups = self.wrap_service(groups_pb2_grpc.GroupsStub, **kv_wrap)
        self.profile = self.wrap_service(profile_pb2_grpc.ProfileStub, **kv_wrap)
        self.presence = self.wrap_service(presence_pb2_grpc.PresenceStub, **kv_wrap)
        self.reactions = self.wrap_service(reactions_pb2_grpc.ReactionsStub, **kv_wrap)
        self.favourites_messages = self.wrap_service(favourites_messages_pb2_grpc.FavouritesMessagesStub, **kv_wrap)
        self.pinned_messages = self.wrap_service(pinned_messages_pb2_grpc.PinnedMessagesStub, **kv_wrap)
        self.threads = self.wrap_service(threads_pb2_grpc.ThreadsStub, **kv_wrap)
        self.stickers = self.wrap_service(stickers_pb2_grpc.StickersStub, **kv_wrap)
        self.token, self.client_auth_id = self.get_session_token()
        upload_options = kwargs.get("upload_options") if isinstance(kwargs.get("upload_options"), dict) else {}
        self.uploading = Uploading(
            self, kwargs.get("cert"), kwargs.get("private_key"), kwargs.get("access_dir"),
            upload_options.get("parallelism"), upload_options.get("retry"), upload_options.get("retry_period")
        )
        self.downloading = Downloading(self)

    def authorize(self, bot_token):
        """Authorization function for Internal bot instance.

        :param bot_token: bot token
        :return: auth token (instance of gRPC RequestStartTokenAuth)
        """
        return self.auth.StartTokenAuth(authentication_pb2.RequestStartTokenAuth(
            token=bot_token,
        ))

    def anonymous_authorize(self, name='dumb'):
        return self.auth.StartAnonymousAuth(authentication_pb2.RequestStartAnonymousAuth(
            name=name
        ))

    def get_session_token(self):
        """Requests for sessions token for device.

        :return: session token
        """
        registration_response = self.registration.RegisterDevice(
            registration_pb2.RequestRegisterDevice(
                app_id=self.app_id,
                app_title=self.app_title,
                device_title=self.app_title
            )
        )
        return registration_response.token, registration_response.auth_id

    @staticmethod
    def parse_options(options, default):
        if options is None:
            options = {}
        for option, value in default.items():
            if option not in options:
                options[option] = value
        return options

    def wrap_service(self, stub_func, **kwargs):
        """Wrapper for authenticating of gRPC service calls.

        :param stub_func: name of gRPC service
        :return: wrapped gRPC service
        """
        return AuthenticatedService(
            lambda: self.token if hasattr(self, 'token') else None,
            stub_func(self.channel),
            **kwargs
        )
