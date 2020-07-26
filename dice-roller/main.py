if __name__ == '__main__':
    print(__name__, __package__)
    from model.board import Board
    from model.roller_factory import RollerFactory

    b = Board()
    rf = RollerFactory()

    rp_str = input("\n>")

    b.add_packet(rp_str, rf)

    print("----------------------------------------")
    print("self.roller_packets: ")
    print("\tlen: ", len(b.roller_packets))
    print("----------------------------------------")

    y = b.roll_all()

    for i in y:
        print(type(i), "\t", i, end="\n\n")
