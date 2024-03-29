# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import miniappsregistry_pb2 as miniappsregistry__pb2


class ClientsMiniAppsRegistryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindApp = channel.unary_unary(
                '/dialog.ClientsMiniAppsRegistry/FindApp',
                request_serializer=miniappsregistry__pb2.FindAppRequest.SerializeToString,
                response_deserializer=miniappsregistry__pb2.FindAppResponse.FromString,
                )
        self.GetApps = channel.unary_unary(
                '/dialog.ClientsMiniAppsRegistry/GetApps',
                request_serializer=miniappsregistry__pb2.GetAppsRequest.SerializeToString,
                response_deserializer=miniappsregistry__pb2.GetAppsResponse.FromString,
                )
        self.GetExtensions = channel.unary_unary(
                '/dialog.ClientsMiniAppsRegistry/GetExtensions',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=miniappsregistry__pb2.GetExtensionsResponse.FromString,
                )
        self.IssueAccessToken = channel.unary_unary(
                '/dialog.ClientsMiniAppsRegistry/IssueAccessToken',
                request_serializer=miniappsregistry__pb2.IssueAccessTokenRequest.SerializeToString,
                response_deserializer=miniappsregistry__pb2.AccessTokenResponse.FromString,
                )


class ClientsMiniAppsRegistryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindApp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetApps(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExtensions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IssueAccessToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientsMiniAppsRegistryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindApp': grpc.unary_unary_rpc_method_handler(
                    servicer.FindApp,
                    request_deserializer=miniappsregistry__pb2.FindAppRequest.FromString,
                    response_serializer=miniappsregistry__pb2.FindAppResponse.SerializeToString,
            ),
            'GetApps': grpc.unary_unary_rpc_method_handler(
                    servicer.GetApps,
                    request_deserializer=miniappsregistry__pb2.GetAppsRequest.FromString,
                    response_serializer=miniappsregistry__pb2.GetAppsResponse.SerializeToString,
            ),
            'GetExtensions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExtensions,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=miniappsregistry__pb2.GetExtensionsResponse.SerializeToString,
            ),
            'IssueAccessToken': grpc.unary_unary_rpc_method_handler(
                    servicer.IssueAccessToken,
                    request_deserializer=miniappsregistry__pb2.IssueAccessTokenRequest.FromString,
                    response_serializer=miniappsregistry__pb2.AccessTokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dialog.ClientsMiniAppsRegistry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientsMiniAppsRegistry(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindApp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.ClientsMiniAppsRegistry/FindApp',
            miniappsregistry__pb2.FindAppRequest.SerializeToString,
            miniappsregistry__pb2.FindAppResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetApps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.ClientsMiniAppsRegistry/GetApps',
            miniappsregistry__pb2.GetAppsRequest.SerializeToString,
            miniappsregistry__pb2.GetAppsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExtensions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.ClientsMiniAppsRegistry/GetExtensions',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            miniappsregistry__pb2.GetExtensionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IssueAccessToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.ClientsMiniAppsRegistry/IssueAccessToken',
            miniappsregistry__pb2.IssueAccessTokenRequest.SerializeToString,
            miniappsregistry__pb2.AccessTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
