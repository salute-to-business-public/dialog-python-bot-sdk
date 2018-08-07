from dialog_bot_sdk.peers import private_peer
from dialog_bot_sdk.bot import DialogBot

def on_msg(*params):
    print params

if __name__ == '__main__':
    d = DialogBot.get_insecure_bot("grpc-test.transmit.im:8080", "c1ff5ca4b7e5fa4660c6a730fdcb613e31deafd8")
    d.messaging.send_message(private_peer(966246115), "test")
    d.messaging.on_message(on_msg)
