from .service import ManagedService
from dialog_api import sequence_and_updates_pb2, miscellaneous_pb2

DEFAULT_OPTIMIZATIONS = [
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_ENTITIES,
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_ENTITIES_V2,
    miscellaneous_pb2.UPDATEOPTIMIZATION_STRIP_COUNTERS,
    miscellaneous_pb2.UPDATEOPTIMIZATION_COMPACT_USERS
]


class Updates(ManagedService):
    def get_difference(self, seq):
        return self.internal.updates.GetDifference(
            sequence_and_updates_pb2.RequestGetDifference(
                seq=seq,
                optimizations=DEFAULT_OPTIMIZATIONS
            )
        )
