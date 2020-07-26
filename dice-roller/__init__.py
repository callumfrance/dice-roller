from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def base():
        from .model.board import Board
        from .model.roller_factory import RollerFactory

        r_str = ""

        b = Board()
        rf = RollerFactory()

        rp_str = "2d5 + 1d20 - 17 - 2d2 + 1"

        b.add_packet(rp_str, rf)

        r_str += "----------------------------------------\n"
        r_str += "self.roller_packets: \n"
        r_str += "\tlen: " + str(len(b.roller_packets)) + "\n"
        r_str += "----------------------------------------\n\n"

        y = b.roll_all()

        for i in y:
            r_str += str(type(i)) + "\t" + str(i) + "\n\n"

        return r_str

    return app

if __name__ == '__main__':
    print(__name__, __package__)
    from .model.board import Board
    from .model.roller_factory import RollerFactory

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
