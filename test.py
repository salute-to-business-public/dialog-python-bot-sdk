# coding: utf-8
from dialog_bot_sdk.internal.peers import private_peer
from dialog_bot_sdk.bot import DialogBot
from threading import Thread, Timer
from dialog_bot_sdk import interactive_media
import time


def hello():
    print('Yay!')


def on_msg(*params):
    print('Receiving message...')
    t = Timer(10, hello)
    t.start()
    print('on msg', params[0].message.textMessage.text)
    # for container in d.updates.get_difference(2100).updates:
    #     if container.update_header == 55:
    #         message = messaging_pb2.UpdateMessage()
    #         message.ParseFromString(container.update)
    #         print(message.message.textMessage.text)


if __name__ == '__main__':
    d = DialogBot.get_insecure_bot(
        "grpc-test.transmit.im:8080",
        "6075cd040cb5a43a1362c06612b026f7d58538d5"
    )

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

    def receiver():
        d.messaging.on_message(on_msg)


    receiver()

    # rcvThread = Thread(target=receiver)
    # rcvThread.setDaemon(True)
    # rcvThread.start()
    #
    # # sndThread = Thread(target = sender)
    # # sndThread.setDaemon(True)
    # # sndThread.start()
    # #
    # # sndThread.join(timeout=10.0)
    # # rcvThread.join(timeout=10.0)
    # #
    # time.sleep(60)
