from random import randint
from typing import Dict

from .roller import Roller


class Dicer(Roller):


    def __init__(self, \
            sides: int=6, \
            style=None, \
            sign: str='+', \
            name: str=None):
        self.sides = sides
        super().__init__(sign=sign, style=style, name=name)
        if not name:
            self.name = str(self.sign) + "d" + str(self.sides)

    @property
    def sides(self) -> int:
        return self._sides

    @sides.setter
    def sides(self, in_sides: int=6):
        if in_sides < 0:
            in_sides = 1
        self._sides = in_sides

    @property
    def name(self):
        return super().name

    @name.setter
    def name(self, name: str=None):
        super(Dicer, self.__class__).name.fset(self, name)

    @property
    def style(self):
        return super().style

    @style.setter
    def style(self, style: str=None):
        super(Dicer, self.__class__).style.fset(self, style)

    @property
    def sign(self):
        return super().sign

    @sign.setter
    def sign(self, sign: str="+"):
        super(Dicer, self.__class__).sign.fset(self, sign)

    def roll(self) -> int:
        """
        The act of rolling the Roller to produce a value.

        :return: The rolled value
        :rtype: int

        :example:

        >>> a = Dicer(6)
        >>> a.roll()
        4
        """
        if self.sign == '-':
            return -1 * randint(1, self.sides)
        else:
            return randint(1, self.sides)

    def probability_dist(self) -> Dict[int, float]:
        """
        Gives the likelihoods of each number being rolled by the Roller

        The die should have an equal probability of any side being chosen.

        :return: A dictionary of probability distributions, where each key
            is an integer that contains its probability of getting.
        :rtype: dict
        """
        dist_vals = dict()

        for i in range(self.sides):
            dist_vals[i + 1] = 1.0 / self.sides

        return dist_vals

