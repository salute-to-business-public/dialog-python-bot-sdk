# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import clickroad_pb2 as clickroad__pb2


class ClickRoadStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TrackEvent = channel.unary_unary(
                '/clickroad.ClickRoad/TrackEvent',
                request_serializer=clickroad__pb2.RequestTrackEvent.SerializeToString,
                response_deserializer=clickroad__pb2.ResponseTrackEvent.FromString,
                )


class ClickRoadServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TrackEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClickRoadServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TrackEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.TrackEvent,
                    request_deserializer=clickroad__pb2.RequestTrackEvent.FromString,
                    response_serializer=clickroad__pb2.ResponseTrackEvent.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'clickroad.ClickRoad', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClickRoad(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TrackEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/clickroad.ClickRoad/TrackEvent',
            clickroad__pb2.RequestTrackEvent.SerializeToString,
            clickroad__pb2.ResponseTrackEvent.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
