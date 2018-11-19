# coding: utf-8
from dialog_bot_sdk.internal.peers import private_peer
from dialog_bot_sdk.bot import DialogBot
from threading import Thread, Timer
from dialog_bot_sdk import interactive_media
import time


def on_msg(*params):
    print('on msg', params[0].message.textMessage.text)
    # d.messaging.send_message(params[0].peer, 'Reply to: ' + str(params[0].message.textMessage.text))
    # d.updates.get_difference(5272)
    d.messaging.send_photo(params[0].peer, 'image.png')


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
