from concurrent.futures import ThreadPoolExecutor
from .service import AuthenticatedService
from dialog_bot_sdk.dialog_api import registration_pb2, registration_pb2_grpc,\
                       sequence_and_updates_pb2_grpc,\
                       authentication_pb2, authentication_pb2_grpc,\
                       contacts_pb2_grpc, search_pb2_grpc, messaging_pb2_grpc,\
                       media_and_files_pb2_grpc, users_pb2_grpc
from dialog_bot_sdk.uploading import Uploading


class InternalBot(object):
    """Class with Dialog bot's internal services.

    """

    def __init__(self, channel, verbose=False, cert=None, private_key=None):
        self.app_id = 10
        self.app_title = "PythonBotSDK/1.0"
        self.channel = channel
        self.registration = self.wrap_service(registration_pb2_grpc.RegistrationStub, verbose=verbose)
        self.messaging = self.wrap_service(messaging_pb2_grpc.MessagingStub, verbose=verbose)
        self.media_and_files = self.wrap_service(media_and_files_pb2_grpc.MediaAndFilesStub, verbose=verbose)
        self.updates = self.wrap_service(sequence_and_updates_pb2_grpc.SequenceAndUpdatesStub, verbose=verbose)
        self.auth = self.wrap_service(authentication_pb2_grpc.AuthenticationStub, verbose=verbose)
        self.contacts = self.wrap_service(contacts_pb2_grpc.ContactsStub, verbose=verbose)
        self.search = self.wrap_service(search_pb2_grpc.SearchStub, verbose=verbose)
        self.users = self.wrap_service(users_pb2_grpc.UsersStub, verbose=verbose)
        self.token = self.get_session_token()
        self.thread_pool_executor = ThreadPoolExecutor(max_workers=10)
        self.uploading = Uploading(self, cert, private_key)

    def authorize(self, bot_token):
        """Authorization function for Internal bot instance.

        :param bot_token: bot token
        :return: auth token (instance of gRPC RequestStartTokenAuth)
        """
        return self.auth.StartTokenAuth(authentication_pb2.RequestStartTokenAuth(
            token=bot_token,
            app_id=self.app_id
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
        return registration_response.token

    def wrap_service(self, stub_func, verbose=False):
        """Wrapper for authenticating of gRPC service calls.

        :param stub_func: name of gRPC service
        :param verbose: verbosity level of functions calling
        :return: wrapped gRPC service
        """
        return AuthenticatedService(
            lambda: self.token if hasattr(self, 'token') else None,
            stub_func(self.channel),
            verbose=verbose
        )
