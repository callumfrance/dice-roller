from abc import ABCMeta, abstractmethod
from typing import Dict


class Roller(metaclass=ABCMeta):
    """
    The Roller class is an interface of things of indeterminate value.

    :param str style: The hexadecimal string colour of the Roller object
    :param str sign: The + or - sign indicator of the Roller's value
    """

    @abstractmethod
    def __init__(self, sign, style):
        self.sign = sign
        self.style = style


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
        """
        The act of rolling the Roller to produce a value.

        :return: The rolled value
        :rtype: int

        :example:

        >>> a = Dicer(6)
        >>> a.roll()
        4
        """
        pass

    @abstractmethod
    def probability_dist(self) -> Dict[int, float]:
        """
        Gives the likelihoods of each number being rolled by the Roller

        :return: A dictionary of probability distributions, where each key
            is an integer that contains its probability of getting.
        :rtype: dict
        """
        pass
