from flask import (Flask, render_template, request)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/quick/<roll_str>')
    def dice_quick_roll(roll_str):
        from .model.board import Board
        from .model.roller_factory import RollerFactory

        b = Board()
        rf = RollerFactory()
        b.add_packet(roll_str, rf)

        roll = b.roll_all()

        # return str(b.roll_all())
        return render_template('rolled.html', \
                result=roll[0][0], \
                roll_results=roll[0][1], \
            )

    @app.route('/build')
    def dice_build():
        return render_template('dice_build.html')

    @app.route('/sc', methods=['GET'])
    def dice_form_built():
        # text = request.form['text']
        # text = request.args['text']
        a = request.args
        a_i = ''
        text = request.args.get('text')
        for i in a:
            a_i += i + ': '
            a_i += a.get(i) + "   "

        return str((str(a), "---------", str(a_i)))

    @app.route('/')
    def base():
        from .model.board import Board
        from .model.roller_factory import RollerFactory

        r_out = list()

        b = Board()
        rf = RollerFactory()

        rp_str = "2d5 + 1d20 - 17 - 2d2 + 1"

        b.add_packet(rp_str, rf)

        r_out.append(str("----------------------------------------\n"))
        r_out.append(str("self.roller_packets: \n"))
        r_out.append(str("\tlen: " + str(len(b.roller_packets)) + "\n"))
        r_out.append(str("----------------------------------------\n\n"))

        y = b.roll_all()

        for i in y:
            r_out.append(str(str(type(i)) + "\t" + str(i) + "\n\n"))

        return render_template('main.html', r_out=r_out)

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
