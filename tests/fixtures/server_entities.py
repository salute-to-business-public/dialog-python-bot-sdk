from dialog_api.definitions_pb2 import UUIDValue
from dialog_api.groups_pb2 import GroupData, Group, GroupType
from dialog_api.media_and_files_pb2 import FileLocation, Avatar, AvatarImage
from dialog_api.messaging_pb2 import HistoryMessage, DeletedMessage, DocumentMessage, JsonMessage, ServiceMessage, \
    TextMessage, MessageContent, ServiceEx, DocumentEx, DocumentExPhoto, DocumentExVideo, DocumentExVoice, \
    ServiceExChangedAbout, ServiceExChangedAvatar, ServiceExChangedTitle, ServiceExChangedTopic, ServiceExUserInvited, \
    ServiceExUserKicked, ReferencedMessages, Mention
from dialog_api.peers_pb2 import UserOutPeer, GroupOutPeer, Peer, PeerType, OutPeer, PEERTYPE_GROUP, PEERTYPE_PRIVATE
from dialog_api.reactions_pb2 import MessageReactions, Reaction
from dialog_api.search_pb2 import PeerSearchResult
from dialog_api.users_pb2 import UserData, User, FullUser
from google.protobuf.wrappers_pb2 import Int64Value, BoolValue, StringValue, Int32Value
from tests.fixtures.client_entities import rnd

user_outpeer = UserOutPeer(uid=rnd(), access_hash=rnd())
group_outpeer = GroupOutPeer(group_id=rnd(), access_hash=rnd())
user_peer = Peer(id=rnd(), type=PeerType.PEERTYPE_PRIVATE)
group_peer = Peer(id=rnd(), type=PeerType.PEERTYPE_GROUP)
uop = OutPeer(id=rnd(), type=PeerType.PEERTYPE_PRIVATE, access_hash=rnd())
gop = OutPeer(id=rnd(), type=PeerType.PEERTYPE_GROUP, access_hash=rnd())
mid = UUIDValue(msb=rnd(), lsb=rnd())
prev_mid = UUIDValue(msb=rnd(), lsb=rnd())
deleted_message = DeletedMessage(is_local=BoolValue(value=False))
document_ext = DocumentEx(photo=DocumentExPhoto(w=rnd(), h=rnd()),
                          video=DocumentExVideo(w=rnd(), h=rnd(), duration=rnd()),
                          voice=DocumentExVoice(duration=rnd()))
document_message = DocumentMessage(file_id=rnd(), access_hash=rnd(), file_size=rnd(), mime_type="", name="", ext=document_ext)
json_message = JsonMessage(raw_json='')
file_location = FileLocation(file_id=rnd(), access_hash=rnd())
avatar_image = AvatarImage(file_location=file_location, width=rnd(), height=rnd(), file_size=rnd())
avatar = Avatar(small_image=avatar_image, large_image=avatar_image, full_image=avatar_image)
service_ex = ServiceEx(changedAbout=ServiceExChangedAbout(about=StringValue(value='about')),
                       changedAvatar=ServiceExChangedAvatar(avatar=avatar),
                       changedTitle=ServiceExChangedTitle(title='title'),
                       changedTopic=ServiceExChangedTopic(topic=StringValue(value='topic')),
                       userInvited=ServiceExUserInvited(invited_uid=rnd()),
                       userKicked=ServiceExUserKicked(kicked_uid=rnd()))
service_message = ServiceMessage(text='', ext=service_ex)
text_message = TextMessage(text="text", media=[], mentions=[Mention(peer=Peer(id=rnd(), type=PEERTYPE_PRIVATE))])
message_content = MessageContent(deletedMessage=deleted_message, documentMessage=document_message,
                                 jsonMessage=json_message, serviceMessage=service_message, textMessage=text_message)
history_message = HistoryMessage(mid=mid, prev_mid=prev_mid, sender_peer=uop, message=message_content, date=0,
                                 forward=ReferencedMessages(mids=[mid]), reply=ReferencedMessages(mids=[prev_mid]),
                                 edited_at=Int64Value(value=0))
user_data = UserData(name="name", about=StringValue(value="about"), nick=StringValue(value="nick"),
                     avatar=avatar)
group_data = GroupData(about=StringValue(value="about"), avatar=avatar,
                       title="title", group_type=GroupType.GROUPTYPE_GROUP, owner_user_id=rnd(),
                       conference_link=StringValue(value="conference_link"), members_amount=rnd(),
                       members_count_limit=Int32Value(value=rnd()),
                       shortname=StringValue(value="shortname"))
user = User(id=rnd(), access_hash=rnd(), data=user_data)
group = Group(id=rnd(), access_hash=rnd(), data=group_data)

search_result = [PeerSearchResult(peer=Peer(id=group.id, type=PEERTYPE_GROUP), shortname=StringValue(value="text")),
                 PeerSearchResult(peer=Peer(id=user.id, type=PEERTYPE_PRIVATE), shortname=StringValue(value="text"))]

full_user = FullUser(id=rnd(), custom_profile="custom_profile", about=StringValue(value="about"),
                     preferred_languages=["ru"], time_zone=StringValue(value="MsK"))

message_reactions = MessageReactions(mid=mid, reactions=[Reaction(code="😀", users=[rnd()], users_amount=rnd())])