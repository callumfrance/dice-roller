from flask import (Flask, 
        redirect,
        render_template,
        request,
        url_for,)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/quick/')
    def dice_quick_empty():
        return redirect(url_for('dice_build'))

    @app.route('/quick/<roll_str>')
    def dice_quick_roll(roll_str):
        from .model.board import Board
        from .model.roller_factory import RollerFactory

        b = Board()
        rf = RollerFactory()
        b.add_packets(roll_str, rf)

        roll = b.roll_all()

        # return str(b.roll_all())
        return render_template('rolled.html', \
                whole_hog=roll, \
            )

    @app.route('/build', methods=['GET', 'POST'])
    def dice_build():
        if request.method == 'POST':
            mystr = ''
            mystr_counter = 0
            for n, key in enumerate(request.form):
                if request.form[key]:

                    if request.form[key] == '':
                        continue
                    elif key == 'dXX':
                        pass
                    elif (request.form[key][0] != '-') and (mystr_counter != 0):
                        mystr += ' + '

                    mystr_counter += 1

                    if key == "m":
                        mystr += request.form[key]
                    elif key == 'dX':
                        mystr += request.form[key] + 'd'
                    elif key == 'dXX':
                        mystr += request.form[key]
                    else:
                        mystr += request.form[key] + key
            print("---------------------------------------------------")
            print(mystr)
            print("---------------------------------------------------")
            return redirect(url_for('dice_quick_roll', roll_str=mystr))

        dice = {'d4': 'LimeGreen', 
                'd6': 'LightCoral', 
                'd8': 'DodgerBlue',
                'd10': 'DarkOrange',
                'd12': 'PeachPuff',
                'd20': 'Plum',}
        return render_template('dice_build.html', dice_types=dice)

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

        b.add_a_packet(rp_str, rf)

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

    b.add_a_packet(rp_str, rf)

    print("----------------------------------------")
    print("self.roller_packets: ")
    print("\tlen: ", len(b.roller_packets))
    print("----------------------------------------")

    y = b.roll_all()

    for i in y:
        print(type(i), "\t", i, end="\n\n")
