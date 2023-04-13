from dialog_api import config_sync_pb2


class Parameter:
    def __init__(self, key: str, value: str, clock: int) -> None:
        self.key = key
        self.value = value
        self.clock = clock

    @classmethod
    def from_api(cls, parameter: config_sync_pb2.Parameter) -> 'Parameter':
        return cls(parameter.key, parameter.value, parameter.clock)

    def __dict__(self):
        return {
            "key": self.key,
            "value": self.value,
            "clock": self.clock,
        }

    def __str__(self):
        return "Parameter({})".format(self.__dict__())


class FeatureFlag:
    def __init__(self, key: str, value: str, clock: int) -> None:
        self.key = key
        self.value = value
        self.clock = clock

    @classmethod
    def from_api(cls, flag: config_sync_pb2.FeatureFlag) -> 'FeatureFlag':
        return cls(flag.key, flag.value, flag.clock)

    def __dict__(self):
        return {
            "key": self.key,
            "value": self.value,
            "clock": self.clock,
        }

    def __str__(self):
        return "FeatureFlag({})".format(self.__dict__())


# updates
class UpdateParameterChanged:
    def __init__(self, key: str, value: str, parameter: Parameter) -> None:
        self.key = key
        self.value = value
        self.parameter = parameter

    @classmethod
    def from_api(cls, update: config_sync_pb2.UpdateParameterChanged) -> 'UpdateParameterChanged':
        return cls(update.key, update.value.value, Parameter.from_api(update.parameter))

    def __dict__(self):
        return {
            "key": self.key,
            "value": self.value,
            "parameter": self.parameter.__dict__(),
        }

    def __str__(self):
        return "UpdateParameterChanged({})".format(self.__dict__())


class UpdateFeatureFlagChanged:
    def __init__(self, feature: FeatureFlag) -> None:
        self.feature = feature

    @classmethod
    def from_api(cls, update: config_sync_pb2.UpdateFeatureFlagChanged) -> 'UpdateFeatureFlagChanged':
        return cls(FeatureFlag.from_api(update.feature))

    def __dict__(self):
        return {
            "feature": self.feature.__dict__(),
        }

    def __str__(self):
        return "UpdateFeatureFlagChanged({})".format(self.__dict__())
