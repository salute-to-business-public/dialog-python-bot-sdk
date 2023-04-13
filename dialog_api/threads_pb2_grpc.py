# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import threads_pb2 as threads__pb2


class ThreadsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateThread = channel.unary_unary(
                '/dialog.Threads/CreateThread',
                request_serializer=threads__pb2.RequestCreateThread.SerializeToString,
                response_deserializer=threads__pb2.ResponseCreateThread.FromString,
                )
        self.GetThreads = channel.unary_unary(
                '/dialog.Threads/GetThreads',
                request_serializer=threads__pb2.RequestGetThreads.SerializeToString,
                response_deserializer=threads__pb2.ResponseGetThreads.FromString,
                )
        self.GetConversationThreads = channel.unary_unary(
                '/dialog.Threads/GetConversationThreads',
                request_serializer=threads__pb2.RequestGetConversationThreads.SerializeToString,
                response_deserializer=threads__pb2.ResponseGetConversationThreads.FromString,
                )
        self.Subscribe = channel.unary_unary(
                '/dialog.Threads/Subscribe',
                request_serializer=threads__pb2.RequestSubscribeToThread.SerializeToString,
                response_deserializer=threads__pb2.ResponseSubscribeToThread.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/dialog.Threads/Unsubscribe',
                request_serializer=threads__pb2.RequestUnsubscribeFromThread.SerializeToString,
                response_deserializer=threads__pb2.ResponseUnsubscribeFromThread.FromString,
                )
        self.GetSubscribedThreads = channel.unary_unary(
                '/dialog.Threads/GetSubscribedThreads',
                request_serializer=threads__pb2.RequestSubscribedThreads.SerializeToString,
                response_deserializer=threads__pb2.ResponseSubscribedThreads.FromString,
                )
        self.UnsubscribeFromAllThreads = channel.unary_unary(
                '/dialog.Threads/UnsubscribeFromAllThreads',
                request_serializer=threads__pb2.RequestUnsubscribeFromAllThreads.SerializeToString,
                response_deserializer=threads__pb2.ResponseUnsubscribeFromAllThreads.FromString,
                )


class ThreadsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateThread(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetThreads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConversationThreads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubscribedThreads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnsubscribeFromAllThreads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ThreadsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateThread': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateThread,
                    request_deserializer=threads__pb2.RequestCreateThread.FromString,
                    response_serializer=threads__pb2.ResponseCreateThread.SerializeToString,
            ),
            'GetThreads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetThreads,
                    request_deserializer=threads__pb2.RequestGetThreads.FromString,
                    response_serializer=threads__pb2.ResponseGetThreads.SerializeToString,
            ),
            'GetConversationThreads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConversationThreads,
                    request_deserializer=threads__pb2.RequestGetConversationThreads.FromString,
                    response_serializer=threads__pb2.ResponseGetConversationThreads.SerializeToString,
            ),
            'Subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=threads__pb2.RequestSubscribeToThread.FromString,
                    response_serializer=threads__pb2.ResponseSubscribeToThread.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=threads__pb2.RequestUnsubscribeFromThread.FromString,
                    response_serializer=threads__pb2.ResponseUnsubscribeFromThread.SerializeToString,
            ),
            'GetSubscribedThreads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubscribedThreads,
                    request_deserializer=threads__pb2.RequestSubscribedThreads.FromString,
                    response_serializer=threads__pb2.ResponseSubscribedThreads.SerializeToString,
            ),
            'UnsubscribeFromAllThreads': grpc.unary_unary_rpc_method_handler(
                    servicer.UnsubscribeFromAllThreads,
                    request_deserializer=threads__pb2.RequestUnsubscribeFromAllThreads.FromString,
                    response_serializer=threads__pb2.ResponseUnsubscribeFromAllThreads.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dialog.Threads', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Threads(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateThread(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Threads/CreateThread',
            threads__pb2.RequestCreateThread.SerializeToString,
            threads__pb2.ResponseCreateThread.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetThreads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Threads/GetThreads',
            threads__pb2.RequestGetThreads.SerializeToString,
            threads__pb2.ResponseGetThreads.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConversationThreads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Threads/GetConversationThreads',
            threads__pb2.RequestGetConversationThreads.SerializeToString,
            threads__pb2.ResponseGetConversationThreads.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Threads/Subscribe',
            threads__pb2.RequestSubscribeToThread.SerializeToString,
            threads__pb2.ResponseSubscribeToThread.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Threads/Unsubscribe',
            threads__pb2.RequestUnsubscribeFromThread.SerializeToString,
            threads__pb2.ResponseUnsubscribeFromThread.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSubscribedThreads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Threads/GetSubscribedThreads',
            threads__pb2.RequestSubscribedThreads.SerializeToString,
            threads__pb2.ResponseSubscribedThreads.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnsubscribeFromAllThreads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Threads/UnsubscribeFromAllThreads',
            threads__pb2.RequestUnsubscribeFromAllThreads.SerializeToString,
            threads__pb2.ResponseUnsubscribeFromAllThreads.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)