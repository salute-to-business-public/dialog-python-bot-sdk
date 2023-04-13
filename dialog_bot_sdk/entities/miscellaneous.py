from typing import List
from dialog_api import miscellaneous_pb2
from dialog_bot_sdk.entities.peers import OutPeer


class RtcpMuxPolicy:
    RTCPMUXPOLICY_UNKNOWN = miscellaneous_pb2.RTCPMUXPOLICY_UNKNOWN
    RTCPMUXPOLICY_NEGOTIATE = miscellaneous_pb2.RTCPMUXPOLICY_NEGOTIATE
    RTCPMUXPOLICY_REQUIRE = miscellaneous_pb2.RTCPMUXPOLICY_REQUIRE


class SupportedServerMethodsType:
    NONE_SUPPORTED_METHODS = miscellaneous_pb2.NONE_SUPPORTED_METHODS
    CHANGE_PASSWORD = miscellaneous_pb2.CHANGE_PASSWORD


class Array:
    def __init__(self, values: List) -> None:
        self.values = values

    @classmethod
    def from_api(cls, value: miscellaneous_pb2.RecursiveTypedMap.Array) -> 'Array':
        return cls([Value.from_api(x) for x in value.values])

    def __dict__(self):
        return {"values": [x.__dict__() for x in self.values]}

    def __str__(self):
        return "Array({})".format(self.__dict__())


class Value:
    def __init__(self, d: float, i32: int, i64: int, str_: str, rec, array_rec) -> None:
        self.d = d
        self.i32 = i32
        self.i64 = i64
        self.str = str_
        self.rec = rec
        self.array_rec = array_rec

    @classmethod
    def from_api(cls, value: miscellaneous_pb2.RecursiveTypedMap.Value) -> 'Value':
        return cls(value.d, value.i32, value.i64, value.str,
                   [RecursiveTypedMap.from_api(x) for x in value.rec],
                   [Array.from_api(x) for x in value.array_rec])

    def __dict__(self):
        return {
            "d": self.d,
            "i32": self.i32,
            "i64": self.i64,
            "str_": self.str,
            "rec": [x.__dict__() for x in self.rec],
            "array_rec": [x.__dict__() for x in self.array_rec],
        }

    def __str__(self):
        return "Value({})".format(self.__dict__())


class ItemsEntry:
    def __init__(self, key: str, value: Value) -> None:
        self.key = key
        self.value = value

    @classmethod
    def from_api(cls, value: miscellaneous_pb2.RecursiveTypedMap.ItemsEntry) -> 'ItemsEntry':
        return cls(value.key, Value.from_api(value.value))

    def __dict__(self):
        return {"key": self.key, "value": self.value.__dict__()}

    def __str__(self):
        return "Item({})".format(self.__dict__())


class RecursiveTypedMap:
    def __init__(self, items: List[ItemsEntry]) -> None:
        self.items = items

    @classmethod
    def from_api(cls, map_value: miscellaneous_pb2.RecursiveTypedMap) -> 'RecursiveTypedMap':
        return cls([ItemsEntry.from_api(x) for x in map_value.items])

    def __dict__(self):
        return {"items": [x.__dict__() for x in self.items]}

    def __str__(self):
        return "RecursiveTypedMap({})".format(self.__dict__())


class Discover:
    def __init__(self, peers: List[OutPeer]) -> None:
        self.peers = peers

    @classmethod
    def from_api(cls, discover: miscellaneous_pb2.Discover) -> 'Discover':
        return cls([OutPeer.from_api(x) for x in discover.peers])

    def __dict__(self):
        return {"peers": [x.__dict__() for x in self.peers]}

    def __str__(self):
        return "Discover({})".format(self.__dict__())


class CallsConfig:
    def __init__(
            self,
            calls_enabled: bool,
            video_calls_enabled: bool,
            group_calls_enabled: bool,
            group_calls_max_members: int,
            rtcp_mux_policy: RtcpMuxPolicy,
            emoji_security_enabled: bool,
            screen_sharing_enabled: bool
    ) -> None:
        self.calls_enabled = calls_enabled
        self.video_calls_enabled = video_calls_enabled
        self.group_calls_enabled = group_calls_enabled
        self.group_calls_max_members = group_calls_max_members
        self.rtcp_mux_policy = rtcp_mux_policy
        self.emoji_security_enabled = emoji_security_enabled
        self.screen_sharing_enabled = screen_sharing_enabled

    @classmethod
    def from_api(cls, calls_config: miscellaneous_pb2.CallsConfig) -> 'CallsConfig':
        return cls(
            calls_config.calls_enabled.value,
            calls_config.video_calls_enabled.value,
            calls_config.group_calls_enabled.value,
            calls_config.group_calls_max_members.value,
            calls_config.rtcp_mux_policy,
            calls_config.emoji_security_enabled.value,
            calls_config.screen_sharing_enabled.value
        )

    def __dict__(self):
        return {
            "calls_enabled": self.calls_enabled,
            "video_calls_enabled": self.video_calls_enabled,
            "group_calls_enabled": self.group_calls_enabled,
            "group_calls_max_members": self.group_calls_max_members,
            "rtcp_mux_policy": self.rtcp_mux_policy,
            "emoji_security_enabled": self.emoji_security_enabled,
            "screen_sharing_enabled": self.screen_sharing_enabled
        }

    def __str__(self):
        return "CallsConfig({})".format(self.__dict__())


class InvitesConfig:
    def __init__(self, base_url: str, group_invite_url_prefix: str, resolve_url_prefix: str, 
                 share_invite_url: str) -> None:
        self.base_url = base_url
        self.group_invite_url_prefix = group_invite_url_prefix
        self.resolve_url_prefix = resolve_url_prefix
        self.share_invite_url = share_invite_url

    @classmethod
    def from_api(cls, invite_config: miscellaneous_pb2.InvitesConfig) -> 'InvitesConfig':
        return cls(invite_config.base_url.value, invite_config.group_invite_url_prefix.value,
                   invite_config.resolve_url_prefix.value, invite_config.share_invite_url.value)

    def __dict__(self):
        return {"base_url": self.base_url, "group_invite_url_prefix": self.group_invite_url_prefix,
                "resolve_url_prefix": self.resolve_url_prefix, "share_invite_url": self.share_invite_url}

    def __str__(self):
        return "InvitesConfig({})".format(self.__dict__())


class ServerMetaInfo:
    def __init__(self, release_date: int, api_version: str) -> None:
        self.release_date = release_date
        self.api_version = api_version

    @classmethod
    def from_api(cls, server_meta_info: miscellaneous_pb2.ServerMetaInfo) -> 'ServerMetaInfo':
        return cls(server_meta_info.release_date, server_meta_info.api_version.value)

    def __dict__(self):
        return {"release_date": self.release_date, "api_version": self.api_version}

    def __str__(self):
        return "ServerMetaInfo({})".format(self.__dict__())


class ServicePeers:
    def __init__(self, security: OutPeer, support: OutPeer, stash: OutPeer) -> None:
        self.security = security
        self.support = support
        self.stash = stash

    @classmethod
    def from_api(cls, service_peers: miscellaneous_pb2.ServicePeers) -> 'ServicePeers':
        return cls(OutPeer.from_api(service_peers.security), OutPeer.from_api(service_peers.support),
                   OutPeer.from_api(service_peers.stash))

    def __dict__(self):
        return {"security": self.security.__dict__(), "support": self.support.__dict__(), "stash": self.stash.__dict__()}

    def __str__(self):
        return "ServicePeers({})".format(self.__dict__())


class Any:
    def __init__(self, type_url: str, data: bytes) -> None:
        self.type_url = type_url
        self.data = data

    @classmethod
    def from_api(cls, any: miscellaneous_pb2.Any) -> 'Any':
        return cls(any.data, any.data)

    def __dict__(self):
        return {"type_url": self.type_url, "data": self.data}

    def __str__(self):
        return "Any({})".format(self.__dict__())


class Config:
    def __init__(
            self,
            max_group_size: int,
            discover: Discover,
            share_endpoint: str,
            calls_config: CallsConfig,
            group_invite_config: InvitesConfig,
            server_meta_info: ServerMetaInfo,
            custom_profile_schema: str,
            service_peers: ServicePeers,
            extensions: List[Any],
            client_keep_alive: int,
            supported_methods: List[SupportedServerMethodsType],
            max_channel_size: int
    ) -> None:
        self.max_group_size = max_group_size
        self.discover = discover
        self.share_endpoint = share_endpoint
        self.calls_config = calls_config
        self.group_invite_config = group_invite_config
        self.server_meta_info = server_meta_info
        self.custom_profile_schema = custom_profile_schema
        self.service_peers = service_peers
        self.extensions = extensions
        self.client_keep_alive = client_keep_alive
        self.supported_methods = supported_methods
        self.max_channel_size = max_channel_size

    @classmethod
    def from_api(cls, config: miscellaneous_pb2.Config) -> 'Config':
        return cls(
            config.max_group_size,
            Discover.from_api(config.discover),
            config.share_endpoint.value,
            CallsConfig.from_api(config.calls_config),
            InvitesConfig.from_api(config.group_invite_config),
            ServerMetaInfo.from_api(config.server_meta_info),
            config.custom_profile_schema,
            ServicePeers.from_api(config.service_peers),
            [Any.from_api(x) for x in config.extensions],
            config.client_keep_alive,
            [x for x in config.supported_methods],
            config.max_channel_size
        )

    def __dict__(self):
        return {
            "max_group_size": self.max_group_size,
            "discover": self.discover.__dict__(),
            "share_endpoint": self.share_endpoint,
            "calls_config": self.calls_config.__dict__(),
            "group_invite_config": self.group_invite_config.__dict__(),
            "server_meta_info": self.server_meta_info.__dict__(),
            "custom_profile_schema": self.custom_profile_schema,
            "service_peers": self.service_peers.__dict__(),
            "extensions": [x.__dict__() for x in self.extensions],
            "client_keep_alive": self.client_keep_alive,
            "supported_methods": [x for x in self.supported_methods],
            "max_channel_size": self.max_channel_size
        }

    def __str__(self):
        return "Config({})".format(self.__dict__())


# updates
class UpdateConfig:
    def __init__(self, config: Config, config_hash: int) -> None:
        self.config = config
        self.config_hash = config_hash

    @classmethod
    def from_api(cls, update: miscellaneous_pb2.UpdateConfig) -> 'UpdateConfig':
        return cls(Config.from_api(update.config), update.config_hash.value)

    def __dict__(self):
        return {"config": self.config.__dict__(), "config_hash": self.config_hash}

    def __str__(self):
        return "UpdateConfig({})".format(self.__dict__())

