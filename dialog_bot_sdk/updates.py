from .service import ManagedService
from dialog_api import sequence_and_updates_pb2, miscellaneous_pb2

DEFAULT_OPTIMIZATIONS = [
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_ENTITIES,
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_ENTITIES_V2,
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_COUNTERS,
    miscellaneous_pb2.UPDATEOPTIMIZATION_COMPACT_USERS
]


class Updates(ManagedService):
    """Class for handling grpc's server updates.

    """
    def get_difference(self, seq):
        """Raw implementation of API schema GetDifference method, which returns updates between attribute 'seq' and
        current seq at server side.

        :param seq: seq value
        :return: GetDifferenceResponse object
        """
        request = sequence_and_updates_pb2.RequestGetDifference(
            seq=seq,
            optimizations=DEFAULT_OPTIMIZATIONS
        )

        return self._get_difference(request)

    def get_state(self):
        """Current application seq number

        :return: seq
        """
        request = sequence_and_updates_pb2.RequestGetState(
            optimizations=DEFAULT_OPTIMIZATIONS
        )
        return self._get_state(request).seq

    def _get_difference(self, request):
        return self.internal.updates.GetDifference(request)

    def _get_state(self, request):
        return self.internal.updates.GetState(request)

