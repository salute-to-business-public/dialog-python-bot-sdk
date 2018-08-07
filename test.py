from dialog_bot_sdk.peers import private_peer
from dialog_bot_sdk.bot import DialogBot
from threading import Thread
import time

def on_msg(*params):
    print 'on msg', params

if __name__ == '__main__':
    # d = DialogBot.get_insecure_bot("grpc-test.transmit.im:8080", "c1ff5ca4b7e5fa4660c6a730fdcb613e31deafd8")
    d = DialogBot.get_insecure_bot("localhost:8080", "a4e1d8a184f2a94400dd19492119cbe427d38ef8")
    # d.messaging.send_message(private_peer(966246115), "test")

    def sender():
        i = 0
        while True:
            d.messaging.send_message(private_peer(10), "test %d" % i)
            time.sleep(2)

    def receiver():
        d.messaging.on_message(on_msg)

    rcvThread = Thread(target = receiver)
    rcvThread.setDaemon(True)
    rcvThread.start()

    sndThread = Thread(target = sender)
    sndThread.setDaemon(True)
    sndThread.start()

    sndThread.join(timeout=10.0)
    rcvThread.join(timeout=10.0)

    time.sleep(15)
