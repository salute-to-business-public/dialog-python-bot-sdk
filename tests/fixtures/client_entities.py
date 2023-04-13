import os
from random import randint

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.media_and_files import FileLocation, AvatarImage, Avatar, ImageLocation, AudioLocation
from dialog_bot_sdk.entities.messaging import DeletedMessage, DocumentMessage, JsonMessage, ServiceEx, ServiceMessage, \
    TextMessage, MessageContent, Message, WebPageMedia, ImageMedia, AudioMedia, MessageMedia, DocumentEx, \
    DocumentExPhoto, DocumentExVideo, DocumentExVoice
from dialog_bot_sdk.entities.peers import Peer, PeerType
from dialog_bot_sdk.interactive_media import InteractiveMediaGroup, InteractiveMedia, InteractiveMediaButton, \
    InteractiveMediaSelect


def rnd():
    return randint(0, 100000)


user_peer = Peer(id=rnd(), type=PeerType.PEERTYPE_PRIVATE)
group_peer = Peer(id=rnd(), type=PeerType.PEERTYPE_GROUP)
user_peer_invalid = Peer(id="1", type="1")
group_peer_invalid = Peer(id="2", type="2")

valid_actions = [
    InteractiveMediaGroup(
        [
            InteractiveMedia(
                "1",
                InteractiveMediaButton("Yes", "Да")
            ),
            InteractiveMedia(
                "2",
                InteractiveMediaSelect({"No": "Нет"})
            ),
        ]
    )
]

empty_text = ""
invalid_text = 7347
text = "text"
file = os.getcwd() + "/dialog_bot_sdk/examples/files/example.png"

invalid_actions = [
    InteractiveMediaGroup(
        [
            InteractiveMedia(
                "1",
                InteractiveMediaButton(1, 1)
            ),
            InteractiveMedia(
                "2",
                InteractiveMediaSelect({2: 2})
            ),
        ]
    )
]

mid = UUID(rnd(), rnd())
prev_mid = UUID(rnd(), rnd())
invalid_mid = UUID("1", "1")
deleted_message = DeletedMessage(False)
document_ext = DocumentEx(DocumentExPhoto(rnd(), rnd()), DocumentExVideo(rnd(), rnd(), rnd()), DocumentExVoice(rnd()))
document_message = DocumentMessage(rnd(), rnd(), rnd(), "", "", document_ext)
json_message = JsonMessage('')
file_location = FileLocation(rnd(), rnd())
avatar_image = AvatarImage(file_location, rnd(), rnd(), rnd())
avatar = Avatar(avatar_image, avatar_image, avatar_image)
service_ext = ServiceEx('', avatar, '', '', rnd(), rnd())
service_message = ServiceMessage('', service_ext)
text_message = TextMessage("text", [], [])
message_content = MessageContent(deleted_message, document_message, json_message, service_message, text_message)
message = Message(mid, prev_mid, user_peer, user_peer, message_content, [], [], rnd(), rnd())
image_location = ImageLocation(file_location, rnd(), rnd(), rnd())
web_page = WebPageMedia("dlg.im", "title", "description", image_location)
image_media = ImageMedia(image_location)
audio_media = AudioMedia(AudioLocation(file_location, rnd(), "", rnd()))
media = MessageMedia(web_page, image_media, audio_media)
