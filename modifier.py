from roller import Roller
from typing import Dict


class Modifier(Roller):


    def __init__(self, value: int=1, style: str=None):
        self.value = value
        self.style = None

    def roll(self) -> int:
        return self.value

    def probability_dist(self) -> Dict[int, float]:
        return {self.value: 1.0}
