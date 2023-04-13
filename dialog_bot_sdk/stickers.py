from dialog_bot_sdk.entities.stickers import StickerCollection, ShowcaseSort, StickersShowcase
from dialog_api import stickers_pb2
from dialog_bot_sdk.service import ManagedService
from dialog_bot_sdk.utils import async_dec


class Stickers(ManagedService):
    """Class for handling users
    """
    @async_dec()
    def load_stickers_showcase(self, sort_type: ShowcaseSort = ShowcaseSort.NEWEST) -> StickersShowcase:
        """return thread peer

        :param sort_type: type of sorting
        :return: thread peer
        """
        request = stickers_pb2.RequestLoadStickersShowcase(
            sortType=sort_type
        )
        return StickersShowcase.from_api(self.internal.stickers.LoadStickersShowcase(request))

    def load_stickers_showcase_sync(self, sort_type: ShowcaseSort = ShowcaseSort.NEWEST) -> StickersShowcase:
        return self.load_stickers_showcase.__wrapped__(self, sort_type)

    @async_dec()
    def load_stickers_showcase_more(self, load_showcase_more: bytes) -> StickersShowcase:
        """return thread peer

        :param load_showcase_more: cursor on end last chunk
        :return: thread peer
        """
        request = stickers_pb2.RequestLoadStickersShowcaseMore(
            load_showcase_more=load_showcase_more
        )
        return StickersShowcase.from_api(self.internal.stickers.LoadStickersShowcaseMore(request))

    def load_stickers_showcase_more_sync(self, load_showcase_more: bytes) -> StickersShowcase:
        return self.load_stickers_showcase_more.__wrapped__(self, load_showcase_more)

    @async_dec()
    def load_sticker_collection(self, collection_id: int) -> StickerCollection:
        """return thread peer

        :param collection_id: sticker's collection id
        :return: sticker collection
        """
        request = stickers_pb2.RequestLoadStickerCollection(
            id=collection_id
        )
        return StickerCollection.from_api(self.internal.stickers.LoadStickerCollection(request).collection)

    def load_sticker_collection_sync(self, collection_id: int) -> StickerCollection:
        return self.load_sticker_collection.__wrapped__(self, collection_id)

