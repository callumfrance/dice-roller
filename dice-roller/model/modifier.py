from typing import Dict

from .roller import Roller


class Modifier(Roller):


    def __init__(self, value: int=1, style: str=None, sign: str='+'):
        super().__init__(sign=sign, style=style)
        self.value = value

    @property
    def style(self):
        return super().style

    @style.setter
    def style(self, style: str=None):
        super(Modifier, self.__class__).style.fset(self, style)

    @property
    def sign(self):
        return super().sign

    @sign.setter
    def sign(self, sign: str="+"):
        super(Modifier, self.__class__).sign.fset(self, sign)

    def roll(self) -> int:
        if self.sign == '-':
            return -1 * self.value
        else:
            return self.value

    def probability_dist(self) -> Dict[int, float]:
        return {self.value: 1.0}
