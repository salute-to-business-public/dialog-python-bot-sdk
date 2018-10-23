# coding: utf-8
from dialog_bot_sdk.peers import private_peer
from dialog_bot_sdk.bot import DialogBot
# from dialog_api import messaging_pb2
# from threading import Thread
from dialog_bot_sdk import interactive_media
import time


def on_msg(*params):
    # print('on msg', params)
    for update in d.updates.get_difference(2089).updates:
        print(update)


if __name__ == '__main__':
    d = DialogBot.get_insecure_bot("grpc-test.transmit.im:8080", "ad8db1fbda7ae7465e3517f1e9ea6fb80e8946ac")
    # d = DialogBot.get_insecure_bot("localhost:8080", "a4e1d8a184f2a94400dd19492119cbe427d38ef8")
    # d.messaging.send_message(private_peer(966246115), "test", )

    def sender(count=10):
        i = 0
        while i < count:
            i += 1
            if i % 2 == 0:
                d.messaging.send_message(private_peer(966246115), "Simple text")
            else:
                d.messaging.send_message(
                    private_peer(966246115),
                    "Interactive media %d" % i,
                    [interactive_media.InteractiveMediaGroup(
                        [
                            interactive_media.InteractiveMedia(
                                1,
                                interactive_media.InteractiveMediaButton("Test", "OK"),
                                interactive_media.InteractiveMediaConfirm("Confirm text", "Confirm title")
                            ),
                            interactive_media.InteractiveMedia(
                                1,
                                interactive_media.InteractiveMediaSelect(
                                    "Some select",
                                    'nope',
                                    {'yeah': "Yeah!", "nope": "Nope!", "maybe": "Maybe"}
                                )
                            )
                        ],
                        "Group title",
                        "Group description"
                    )]
                )
            time.sleep(2)
    #


    def receiver():
        d.messaging.on_message(on_msg)

    receiver()

    # rcvThread = Thread(target = receiver)
    # rcvThread.setDaemon(True)
    # rcvThread.start()
    #
    # sndThread = Thread(target = sender)
    # sndThread.setDaemon(True)
    # sndThread.start()
    #
    # sndThread.join(timeout=10.0)
    # rcvThread.join(timeout=10.0)
    #
    # time.sleep(15)
