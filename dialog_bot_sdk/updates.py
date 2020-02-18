from dialog_bot_sdk.utils import async_dec
from .service import ManagedService
from dialog_api import sequence_and_updates_pb2


class Updates(ManagedService):
    """Class for handling grpc's server updates.

    """
    @async_dec()
    def get_difference(self, seq):
        """Raw implementation of API schema GetDifference method, which returns updates between attribute 'seq' and
        current seq at server side.

        :param seq: seq value
        :return: GetDifferenceResponse object
        """
        return self.internal.updates.GetDifference(sequence_and_updates_pb2.RequestGetDifference(seq=seq))

    @async_dec()
    def get_state(self):
        """Current application seq number

        :return: seq
        """
        return self.internal.updates.GetState(sequence_and_updates_pb2.RequestGetState()).seq
