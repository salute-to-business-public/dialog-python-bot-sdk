# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import search_pb2 as search__pb2


class SearchStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PeerSearch = channel.unary_unary(
                '/dialog.Search/PeerSearch',
                request_serializer=search__pb2.RequestPeerSearch.SerializeToString,
                response_deserializer=search__pb2.ResponsePeerSearch.FromString,
                )
        self.ResolvePeer = channel.unary_unary(
                '/dialog.Search/ResolvePeer',
                request_serializer=search__pb2.RequestResolvePeer.SerializeToString,
                response_deserializer=search__pb2.ResponseResolvePeer.FromString,
                )
        self.MessageSearch = channel.unary_unary(
                '/dialog.Search/MessageSearch',
                request_serializer=search__pb2.RequestMessageSearch.SerializeToString,
                response_deserializer=search__pb2.ResponseMessageSearchResponse.FromString,
                )
        self.MessageSearchMore = channel.unary_unary(
                '/dialog.Search/MessageSearchMore',
                request_serializer=search__pb2.RequestMessageSearchMore.SerializeToString,
                response_deserializer=search__pb2.ResponseMessageSearchResponse.FromString,
                )
        self.SimpleSearch = channel.unary_unary(
                '/dialog.Search/SimpleSearch',
                request_serializer=search__pb2.RequestSimpleSearch.SerializeToString,
                response_deserializer=search__pb2.ResponseMessageSearchResponse.FromString,
                )
        self.SimpleSearchMore = channel.unary_unary(
                '/dialog.Search/SimpleSearchMore',
                request_serializer=search__pb2.RequestSimpleSearchMore.SerializeToString,
                response_deserializer=search__pb2.ResponseMessageSearchResponse.FromString,
                )
        self.AutocompleteSuggestions = channel.unary_unary(
                '/dialog.Search/AutocompleteSuggestions',
                request_serializer=search__pb2.RequestFieldAutocomplete.SerializeToString,
                response_deserializer=search__pb2.ResponseFieldAutocomplete.FromString,
                )
        self.LoadUserSearchByPredicatesResults = channel.unary_unary(
                '/dialog.Search/LoadUserSearchByPredicatesResults',
                request_serializer=search__pb2.RequestLoadUserSearchByPredicatesResults.SerializeToString,
                response_deserializer=search__pb2.ResponseLoadUserSearchByPredicatesResults.FromString,
                )
        self.LoadUserSearchByPredicatesCount = channel.unary_unary(
                '/dialog.Search/LoadUserSearchByPredicatesCount',
                request_serializer=search__pb2.RequestLoadUserSearchByPredicatesCount.SerializeToString,
                response_deserializer=search__pb2.ResponseLoadUserSearchByPredicatesCount.FromString,
                )
        self.GetRecommendations = channel.unary_unary(
                '/dialog.Search/GetRecommendations',
                request_serializer=search__pb2.RequestGetRecommendations.SerializeToString,
                response_deserializer=search__pb2.ResponseGetRecommendations.FromString,
                )
        self.GetPromotedPeers = channel.unary_unary(
                '/dialog.Search/GetPromotedPeers',
                request_serializer=search__pb2.RequestGetPromotedPeers.SerializeToString,
                response_deserializer=search__pb2.ResponseGetPromotedPeers.FromString,
                )


class SearchServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PeerSearch(self, request, context):
        """/ Search among groups/users/contacts
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResolvePeer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MessageSearch(self, request, context):
        """/ Search by messages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MessageSearchMore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SimpleSearch(self, request, context):
        """/ Custom search by conditions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SimpleSearchMore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AutocompleteSuggestions(self, request, context):
        """/ Search for autocomplete suggestions among custom user profile
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadUserSearchByPredicatesResults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadUserSearchByPredicatesCount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecommendations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPromotedPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PeerSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.PeerSearch,
                    request_deserializer=search__pb2.RequestPeerSearch.FromString,
                    response_serializer=search__pb2.ResponsePeerSearch.SerializeToString,
            ),
            'ResolvePeer': grpc.unary_unary_rpc_method_handler(
                    servicer.ResolvePeer,
                    request_deserializer=search__pb2.RequestResolvePeer.FromString,
                    response_serializer=search__pb2.ResponseResolvePeer.SerializeToString,
            ),
            'MessageSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.MessageSearch,
                    request_deserializer=search__pb2.RequestMessageSearch.FromString,
                    response_serializer=search__pb2.ResponseMessageSearchResponse.SerializeToString,
            ),
            'MessageSearchMore': grpc.unary_unary_rpc_method_handler(
                    servicer.MessageSearchMore,
                    request_deserializer=search__pb2.RequestMessageSearchMore.FromString,
                    response_serializer=search__pb2.ResponseMessageSearchResponse.SerializeToString,
            ),
            'SimpleSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.SimpleSearch,
                    request_deserializer=search__pb2.RequestSimpleSearch.FromString,
                    response_serializer=search__pb2.ResponseMessageSearchResponse.SerializeToString,
            ),
            'SimpleSearchMore': grpc.unary_unary_rpc_method_handler(
                    servicer.SimpleSearchMore,
                    request_deserializer=search__pb2.RequestSimpleSearchMore.FromString,
                    response_serializer=search__pb2.ResponseMessageSearchResponse.SerializeToString,
            ),
            'AutocompleteSuggestions': grpc.unary_unary_rpc_method_handler(
                    servicer.AutocompleteSuggestions,
                    request_deserializer=search__pb2.RequestFieldAutocomplete.FromString,
                    response_serializer=search__pb2.ResponseFieldAutocomplete.SerializeToString,
            ),
            'LoadUserSearchByPredicatesResults': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadUserSearchByPredicatesResults,
                    request_deserializer=search__pb2.RequestLoadUserSearchByPredicatesResults.FromString,
                    response_serializer=search__pb2.ResponseLoadUserSearchByPredicatesResults.SerializeToString,
            ),
            'LoadUserSearchByPredicatesCount': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadUserSearchByPredicatesCount,
                    request_deserializer=search__pb2.RequestLoadUserSearchByPredicatesCount.FromString,
                    response_serializer=search__pb2.ResponseLoadUserSearchByPredicatesCount.SerializeToString,
            ),
            'GetRecommendations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRecommendations,
                    request_deserializer=search__pb2.RequestGetRecommendations.FromString,
                    response_serializer=search__pb2.ResponseGetRecommendations.SerializeToString,
            ),
            'GetPromotedPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPromotedPeers,
                    request_deserializer=search__pb2.RequestGetPromotedPeers.FromString,
                    response_serializer=search__pb2.ResponseGetPromotedPeers.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dialog.Search', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Search(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PeerSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/PeerSearch',
            search__pb2.RequestPeerSearch.SerializeToString,
            search__pb2.ResponsePeerSearch.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResolvePeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/ResolvePeer',
            search__pb2.RequestResolvePeer.SerializeToString,
            search__pb2.ResponseResolvePeer.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MessageSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/MessageSearch',
            search__pb2.RequestMessageSearch.SerializeToString,
            search__pb2.ResponseMessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MessageSearchMore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/MessageSearchMore',
            search__pb2.RequestMessageSearchMore.SerializeToString,
            search__pb2.ResponseMessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SimpleSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/SimpleSearch',
            search__pb2.RequestSimpleSearch.SerializeToString,
            search__pb2.ResponseMessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SimpleSearchMore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/SimpleSearchMore',
            search__pb2.RequestSimpleSearchMore.SerializeToString,
            search__pb2.ResponseMessageSearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AutocompleteSuggestions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/AutocompleteSuggestions',
            search__pb2.RequestFieldAutocomplete.SerializeToString,
            search__pb2.ResponseFieldAutocomplete.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadUserSearchByPredicatesResults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/LoadUserSearchByPredicatesResults',
            search__pb2.RequestLoadUserSearchByPredicatesResults.SerializeToString,
            search__pb2.ResponseLoadUserSearchByPredicatesResults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadUserSearchByPredicatesCount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/LoadUserSearchByPredicatesCount',
            search__pb2.RequestLoadUserSearchByPredicatesCount.SerializeToString,
            search__pb2.ResponseLoadUserSearchByPredicatesCount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRecommendations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/GetRecommendations',
            search__pb2.RequestGetRecommendations.SerializeToString,
            search__pb2.ResponseGetRecommendations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPromotedPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dialog.Search/GetPromotedPeers',
            search__pb2.RequestGetPromotedPeers.SerializeToString,
            search__pb2.ResponseGetPromotedPeers.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
