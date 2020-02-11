from dialog_api.definitions_pb2 import UUIDValue


class UUID:
    def __init__(self, msb: int, lsb: int) -> None:
        self.msb = msb
        self.lsb = lsb

    def to_api(self) -> UUIDValue:
        return UUIDValue(msb=self.msb, lsb=self.lsb)

    @classmethod
    def from_api(cls, uuid: UUIDValue) -> 'UUID':
        return cls(uuid.msb, uuid.lsb)

    def __dict__(self):
        return {"msb": self.msb, "lsb": self.lsb}

    def __str__(self):
        return "{}".format(self.__dict__())
