class ManagedService(object):
    """Base class for managed services.

    """
    def __init__(self, manager, internal):
        self.manager = manager
        self.internal = internal
