from typing import List

from .roller_packet import RollerPacket
from .roller import Roller
from .dicer import Dicer
from .modifier import Modifier


class RollerFactory():

    @staticmethod
    def create_packets_by_string(in_rp_str: str=None) -> List[RollerPacket]:
        """
        Factory method takes a shorthand string and creates new RollerPackets

        :param str in_rp_str: A list of Rollers, segmented into RP's using ';'
        :return: The newly created list of RollerPacket objects, which contains
            The corresponding Rollers within each one.
        :rtype: List[RollerPacket]

        :example:

        x = RollerFactory()
        y = Board()

        y.roller_packets = x.create_packets_by_string("1d20+5; 2d6+4")
        """
        new_rps = list()

        for x in in_rp_str.split(';'):
            new_rps.append(RollerPacket(RollerFactory.create_roller_by_string(x)))

        return new_rps

    @staticmethod
    def create_roller_by_string(in_roll_str: str="2d8 - 3d6 + 7 + 2d4 - 6") -> List[Roller]:
        """
        1. Remove all whitespace
        2. Split along '-'
        3. For each '-' string, split along '+'
        4. Add a '-' sign to the first element of each '-' list except all[0]
        5. Add a '+' sign to all other elements of each '-' list
        6. Create dice using 'd' or modifier if not using 'd'

        :param str in_roll_str: A shorthand list used to declare Roller objects
        :return: A list of newly created Roller objects
        :rtype: List[Roller]
        """
        new_rolls = list()
        raw_rolls = list()
        sign_sequence = list() # list of either '-' or '+' corresponding to roll

        in_roll_str = "".join(in_roll_str.split()) # Removes all whitespace
        minus_split = in_roll_str.split("-")
        sign_sequence = ['+'] + ['-'] * (len(minus_split) - 1)

        if minus_split[0] == '': # If first char is '-', we can ignore [0]
            minus_split.pop(0)
            sign_sequence.pop(0)

        sign_sentinel = 1
        # Go through each minus split and getting every + term; add it in
        for _ in minus_split:
            plus_split = _.split("+")
            raw_rolls += plus_split

            # Splice in our additional '+' signs into the sequence
            sign_sequence = \
                    sign_sequence[:sign_sentinel] + \
                    (["+"] * (len(plus_split) - 1)) + \
                    sign_sequence[sign_sentinel:]

            sign_sentinel += 1 + (len(plus_split) - 1)

        # We have a 2 lists of equal length - signs and rolls. Now we create obj
        for _ in raw_rolls:
            roll_di = _.split("d")

            # We use the roll str piece to determine which Roller obj to make
            if len(roll_di) < 2:
                new_rolls.append(Modifier(int(roll_di[0]), sign=sign_sequence[0]))
            else:
                for x in range(int(roll_di[0])):
                    new_rolls.append(Dicer(int(roll_di[1]), sign=sign_sequence[0]))
            sign_sequence.pop(0)

        return new_rolls 


if __name__ == '__main__':
    x = RollerFactory()

    y = RollerFactory.create_roller_by_string()

    for i in y:
        print(type(i),"\t", vars(i))

    y = RollerFactory.create_roller_by_string("-1 + 2 + 3 -4 -5 -6 + 7 + 8 -9")

    for i in y:
        print(type(i),"\t", vars(i))
