import abc

from fuawei.entities.fuawei_chip import FuaweiChip


class TechProvider(abc.ABC):

    @abc.abstractmethod
    def ask_chip(self) -> FuaweiChip:
        pass
