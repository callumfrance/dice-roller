from random import randint
from typing import Dict

from roller import Roller


class Dicer(Roller):


    def __init__(self, sides=6, style=None):
        self.sides = sides
        self.style = style

    def roll(self) -> int:
        return randint(1, self.sides)

    def probability_dist(self) -> Dict[int, float]:
        dist_vals = dict()

        for i in range(self.sides):
            dist_vals[i + 1] = 1.0 / self.sides

        return dist_vals

