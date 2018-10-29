from .service import AuthenticatedService
from dialog_api import registration_pb2, registration_pb2_grpc,\
                       sequence_and_updates_pb2_grpc,\
                       authentication_pb2, authentication_pb2_grpc,\
                       contacts_pb2_grpc, search_pb2_grpc, messaging_pb2_grpc


class InternalBot(object):
    """Class with Dialog bot's internal services.

    """

    def __init__(self, channel):
        self.app_id = 10
        self.app_title = "PythonBotSDK/1.0"
        self.channel = channel
        self.registration = self.wrap_service(registration_pb2_grpc.RegistrationStub)
        self.messaging = self.wrap_service(messaging_pb2_grpc.MessagingStub)
        self.updates = self.wrap_service(sequence_and_updates_pb2_grpc.SequenceAndUpdatesStub)
        self.auth = self.wrap_service(authentication_pb2_grpc.AuthenticationStub)
        self.contacts = self.wrap_service(contacts_pb2_grpc.ContactsStub)
        self.search = self.wrap_service(search_pb2_grpc.SearchStub)
        self.token = self.get_session_token()


    def authorize(self, bot_token):
        """Authorization function for Internal bot instance.

        :param bot_token: bot token
        :return: auth token (instance of gRPC RequestStartTokenAuth)
        """
        return self.auth.StartTokenAuth(authentication_pb2.RequestStartTokenAuth(
            token=bot_token,
            app_id=self.app_id
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
        print(registration_response.token)
        return registration_response.token

    def wrap_service(self, stub_func):
        """Wrapper for authenticating of gRPC service calls.

        :param stub_func: name of gRPC service
        :return: wrapped gRPC service
        """
        return AuthenticatedService(lambda: self.token if hasattr(self, 'token') else None, stub_func(self.channel))
