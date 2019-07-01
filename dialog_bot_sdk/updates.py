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
        diff = self.internal.updates.GetDifference(
            sequence_and_updates_pb2.RequestGetDifference(
                seq=seq,
                optimizations=DEFAULT_OPTIMIZATIONS
            )
        )

        return diff
