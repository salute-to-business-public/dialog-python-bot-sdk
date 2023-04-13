import json
from typing import List

from dialog_api import stickers_pb2

from dialog_bot_sdk.entities.media_and_files import ImageLocation


class ShowcaseSort:
    NEWEST = 0
    POPULARITY = 1


class StickerDescriptor:
    def __init__(
            self,
            id: int,
            emoji: str,
            image_128: ImageLocation,
            image_512: ImageLocation,
            image_256: ImageLocation,
            animated_sticker_json: dict or None,
    ) -> None:
        self.id = id
        self.emoji = emoji
        self.image_128 = image_128
        self.image_512 = image_512
        self.image_256 = image_256
        self.animated_sticker_json = animated_sticker_json

    @classmethod
    def from_api(cls, update: stickers_pb2.StickerDescriptor) -> 'StickerDescriptor':
        return cls(
            update.id,
            update.emoji.value,
            ImageLocation.from_api(update.image_128),
            ImageLocation.from_api(update.image_512),
            ImageLocation.from_api(update.image_256),
            json.loads(update.animatedStickerJson.value) if update.animatedStickerJson.value else None,
        )

    def __dict__(self):
        return {
            "id": self.id,
            "emoji": self.emoji,
            "image_128": self.image_128.__dict__(),
            "image_512": self.image_512.__dict__(),
            "image_256": self.image_256.__dict__(),
            "animated_sticker_json": self.animated_sticker_json,
        }

    def __str__(self):
        return "StickerDescriptor({})".format(self.__dict__())


class StickerCollection:
    def __init__(
            self,
            id: int,
            title: str,
            stickers: List[StickerDescriptor],
            owned_by_me: bool,
            clock: int,
            cover_sticker_id: int,
            author: str,
    ) -> None:
        self.id = id
        self.title = title
        self.stickers = stickers
        self.owned_by_me = owned_by_me
        self.clock = clock
        self.cover_sticker_id = cover_sticker_id
        self.author = author

    @classmethod
    def from_api(cls, sticker_collection: stickers_pb2.StickerCollection) -> 'StickerCollection':
        return cls(
            sticker_collection.id,
            sticker_collection.title.value,
            [StickerDescriptor.from_api(x) for x in sticker_collection.stickers],
            sticker_collection.owned_by_me.value,
            sticker_collection.clock,
            sticker_collection.cover_sticker_id.value,
            sticker_collection.author.value,

        )

    def __dict__(self):
        return {
            "id": self.id,
            "title": self.title,
            "stickers": [x.__dict__() for x in self.stickers],
            "owned_by_me": self.owned_by_me,
            "clock": self.clock,
            "cover_sticker_id": self.cover_sticker_id,
            "author": self.author,

        }

    def __str__(self):
        return "StickerCollection({})".format(self.__dict__())


class StickersShowcase:
    def __init__(
            self,
            collections: List[StickerCollection],
            load_showcase_more: bytes,
    ) -> None:
        self.collections = collections
        self.load_showcase_more = load_showcase_more

    @classmethod
    def from_api(cls, sticker_showcase: stickers_pb2.ResponseLoadStickersShowcase) -> 'StickersShowcase':
        return cls(
            [StickerCollection.from_api(x) for x in sticker_showcase.collections],
            sticker_showcase.load_showcase_more.value,
        )

    def __dict__(self):
        return {
            "collections": [x.__dict__() for x in self.collections],
            "load_showcase_more": self.load_showcase_more,
        }

    def __str__(self):
        return "StickersShowcase({})".format(self.__dict__())


# updates
class UpdateStickerCollectionsChanged:
    def __init__(self, updated_collections: List[StickerCollection]) -> None:
        self.updated_collections = updated_collections

    @classmethod
    def from_api(cls, update: stickers_pb2.UpdateStickerCollectionsChanged) -> 'UpdateStickerCollectionsChanged':
        return cls([StickerCollection.from_api(x) for x in update.updated_collections])

    def __dict__(self):
        return {"updated_collections": [x.__dict__() for x in self.updated_collections]}

    def __str__(self):
        return "UpdateStickerCollectionsChanged({})".format(self.__dict__())


class UpdateStickerPackRemoved:
    def __init__(self, pack_id: int) -> None:
        self.pack_id = pack_id

    @classmethod
    def from_api(cls, update: stickers_pb2.UpdateStickerPackRemoved) -> 'UpdateStickerPackRemoved':
        return cls(update.pack_id)

    def __dict__(self):
        return {"pack_id": self.pack_id}

    def __str__(self):
        return "UpdateStickerPackRemoved({})".format(self.__dict__())


class UpdateStickerPackAdded:
    def __init__(self, pack: StickerCollection) -> None:
        self.pack = pack

    @classmethod
    def from_api(cls, update: stickers_pb2.UpdateStickerPackAdded) -> 'UpdateStickerPackAdded':
        return cls(StickerCollection.from_api(update.pack))

    def __dict__(self):
        return {"pack": self.pack.__dict__()}

    def __str__(self):
        return "UpdateStickerPackAdded({})".format(self.__dict__())


class UpdateUserStickerPackCollectionChanged:
    def __init__(self, updated_collections: List[StickerCollection]) -> None:
        self.updated_collections = updated_collections

    @classmethod
    def from_api(cls, update: stickers_pb2.UpdateUserStickerPackCollectionChanged) -> 'UpdateUserStickerPackCollectionChanged':
        return cls([StickerCollection.from_api(x) for x in update.updated_collections])

    def __dict__(self):
        return {"updated_collections": [x.__dict__() for x in self.updated_collections]}

    def __str__(self):
        return "UpdateUserStickerPackCollectionChanged({})".format(self.__dict__())
