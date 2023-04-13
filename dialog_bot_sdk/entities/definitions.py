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
        return "UUID({})".format(self.to_string())

    def to_string(self):
        return (self.digits(self.msb >> 32, 8) + "-" +
                self.digits(self.msb >> 16, 4) + "-" +
                self.digits(self.msb, 4) + "-" +
                self.digits(self.lsb >> 48, 4) + "-" +
                self.digits(self.lsb, 12))

    @staticmethod
    def digits(val: int, digits: int):
        hi = 1 << (digits * 4)
        return str(hex(hi | (val & (hi - 1))))[3:]
