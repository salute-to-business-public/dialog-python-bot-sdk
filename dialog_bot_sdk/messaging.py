from service import ManagedService
from dialog_api import messaging_pb2, sequence_and_updates_pb2
from google.protobuf import empty_pb2


class Messaging(ManagedService):
    def send_message(self, peer, text):
        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        return self.internal.messaging.SendMessage(messaging_pb2.RequestSendMessage(
            peer = outpeer,
            message = msg
        )).mid

    def on_message(self, callback):
        for update in self.internal.updates.SeqUpdates(empty_pb2.Empty()):
            #up = sequence_and_updates_pb2.UpdateSeqUpdate()
            return
