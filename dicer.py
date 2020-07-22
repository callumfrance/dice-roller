from random import randint
from typing import Dict

from roller import Roller


class Dicer(Roller):


    def __init__(self, sides=6, style=None):
        self.sides = sides
        self.style = style

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

