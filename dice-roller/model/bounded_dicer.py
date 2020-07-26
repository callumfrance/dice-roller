from typing import Dict

from .dicer import Dicer


class BoundedDicer(Dicer):


    def __init__(self, in_min: int=1, in_max=None):
        """ Constructor for the BoundedDicer class

        :param in_min: The minimum possible integer to roll
        :param in_max: The maximum possible integer to roll
        """
        super().__init__(self)
        self.min_value = in_min
        self.max_value = in_max if in_max else self.sides

    @property
    def min_value(self) -> int:
        return self.min_value

    @min_value.setter
    def min_value(self, min_value: int=1):
        """
        Sets the minimum value that can be rolled as an object property

        :param int min_value: The minimum value to set that can be rolled on die
        """

        if min_value < 0:
            min_value = 1
        if min_value > self.sides:
            min_value = self.sides
        if self.max_value:
            if min_value > self.max_value:
                min_value = self.max_value
        self._min_value = min_value

    @property
    def min_value(self) -> int:
        return self.min_value

    @min_value.setter
    def min_value(self, max_value: int=6):
        """
        Sets the maximum value that can be rolled as an object property

        :param int max_value: The maximum value to set that can be rolled on die
        """
        if max_value < 0:
            max_value = 1
        if max_value > self.sides:
            max_value = self.sides
        if self.min_value:
            if self.min_value > max_value:
                max_value = self.min_value
        self._max_value = max_value


    def roll(self) -> int:
        """
        :return: The roll, bounded by either the min or max value
        :rtype: int
        """
        base_roll = abs(super().roll(self))

        if base_roll < self.min_value:
            base_roll = self.min_value
        elif base_roll > self.max_value:
            base_roll = self.max_value

        if self.sign == '-':
            return -1 * base_roll

        return base_roll

    def probability_dist(self) -> Dict[int, float]:
        """
        Gives the likelihoods of each number being rolled by the Roller

        Because of the way that the roll is implemented to simply go to the
        nearest boundary value, this means the probability of any roll that
        lands outside of the boundaries needs to be added into the boundaries.

        Most of the legwork is already done in the parent method.

        :return: A dictionary of probability distributions, where each key
            is an integer that contains its probability of getting.
        :rtype: dict
        """

        dist_vals = super().probability_dist(self)

        for key in dist_vals:
            if key < self.min_value:
                dist_value[self.min_value] += dist_value[key]
            elif key > self.max_value:
                dist_value[self.max_value] += dist_value[key]

        return dist_vals
