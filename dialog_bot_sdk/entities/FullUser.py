from typing import List

from dialog_api import users_pb2


class FullUser:
    def __init__(self, id_: int, about: str, preferred_languages: List[str],
                 time_zone: str, custom_profile: str) -> None:
        self.id = id_
        self.about = about
        self.preferred_languages = preferred_languages
        self.time_zone = time_zone
        self.custom_profile = custom_profile

    @classmethod
    def from_api(cls, full_user: users_pb2.FullUser) -> 'FullUser':
        return cls(full_user.id, full_user.about.value, [x for x in full_user.preferred_languages],
                   full_user.time_zone.value, full_user.custom_profile)

    def __dict__(self):
        return {"id": self.id, "about": self.about, "preferred_languages": self.preferred_languages,
                "time_zone": self.time_zone, "custom_profile": self.custom_profile}

    def __str__(self):
        return "full_user: {}".format(self.__dict__())
