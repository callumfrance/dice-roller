from abc import ABCMeta, abstractmethod
from typing import Dict


class Roller(metaclass=ABCMeta):


    @property
    def style(self):
        return self.style

    @style.setter
    def style(self, style: str=None):
        self._style = style

    @property
    def sign(self):
        return self.sign

    @sign.setter
    def sign(self, sign: str="+"):
        self._sign = sign

    @abstractmethod
    def roll(self) -> int:
        pass

    @abstractmethod
    def probability_dist(self) -> Dict[int, float]:
        pass
