# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import tts_pb2 as tts__pb2


class TextToSpeechStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMessageVoice = channel.stream_stream(
                '/dialog.TextToSpeech/GetMessageVoice',
                request_serializer=tts__pb2.RequestGetMessageVoice.SerializeToString,
                response_deserializer=tts__pb2.ResponseGetMessageVoice.FromString,
                )
        self.GetVoicesInfo = channel.unary_unary(
                '/dialog.TextToSpeech/GetVoicesInfo',
                request_serializer=tts__pb2.RequestGetVoicesInfo.SerializeToString,
                response_deserializer=tts__pb2.ResponseGetVoicesInfo.FromString,
                )


class TextToSpeechServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMessageVoice(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVoicesInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TextToSpeechServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMessageVoice': grpc.stream_stream_rpc_method_handler(
                    servicer.GetMessageVoice,
                    request_deserializer=tts__pb2.RequestGetMessageVoice.FromString,
                    response_serializer=tts__pb2.ResponseGetMessageVoice.SerializeToString,
            ),
            'GetVoicesInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetVoicesInfo,
                    request_deserializer=tts__pb2.RequestGetVoicesInfo.FromString,
                    response_serializer=tts__pb2.ResponseGetVoicesInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dialog.TextToSpeech', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TextToSpeech(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMessageVoice(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/dialog.TextToSpeech/GetMessageVoice',
            tts__pb2.RequestGetMessageVoice.SerializeToString,
            tts__pb2.ResponseGetMessageVoice.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetVoicesInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.TextToSpeech/GetVoicesInfo',
            tts__pb2.RequestGetVoicesInfo.SerializeToString,
            tts__pb2.ResponseGetVoicesInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
