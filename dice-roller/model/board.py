from typing import List

from .roller_packet import RollerPacket


class Board():


    def __init__(self):
        self.roller_packets = list()

    def add_packets(self, in_packet_data: str, in_seg_fact) -> List[RollerPacket]:
        """
        Adds newly created RollerPackets to the board object and returns these
            newly created objects in a list.
        """
        new_packs = in_seg_fact.create_packets_by_string(in_packet_data)
        self.roller_packets += new_packs
        return new_packs

    def add_a_packet(self, in_roll_data: str, in_seg_fact) -> RollerPacket:
        """ Use the RollerFactory to create a new RollerPacket containing Rollers

        :return: The newly created RollerPacket, listed inside of Board object
        :rtype: RollerPacket
        """

        # New Rolls are a RollerPacket object of Roller objects
        new_rpack = RollerPacket()
        new_rpack.add_rollers(in_roll_data, in_seg_fact)
        # Board's self.roller_packets now contains the new RollerPacket item
        self.roller_packets.append(new_rpack)

        return new_rpack

    def roll_all(self):
        all_packet_rolls = list()

        for x in self.roller_packets:
            all_packet_rolls.append(x.roll_all())

        return all_packet_rolls


if __name__ == '__main__':
    b = Board()

    # b.add_rollers("2d6 + 4d8 - 3")
    # b.add_rollers("-5")
    # b.add_rollers("3")
    # b.add_rollers("1d20 + 1d4")

    print("Choose the dice to roll: ")
    b.add_rollers(input("\n>"))

    print("----------------------------------------")
    print("self.roller_packets: ")
    print("\tlen: ", len(b.roller_packets))
    print("----------------------------------------")

    y = b.roll_all()

    for i in y:
        print(type(i), "\t", i, end="\n\n")
