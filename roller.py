from abc import ABCMeta, abstractmethod


class Roller(metaclass=ABCMeta):


    @property
    def style(self):
        pass

    @style.setter
    def style(self, style=None):
        pass

    @abstractmethod
    def roll(self) -> int:
        pass
