from flask import (Blueprint,
        render_template,
        )
from urllib.parse import unquote


dice_bp = Blueprint('dice', __name__, url_prefix="/dice-roller")

@dice_bp.route('/<json_roller_packets>')
def dice_packets(json_roller_packets):
    # decode the percent-encoded json into regular json
    decoded_json = unquote(json_roller_packets)
    # decode the json roller packets into roller packet objects
    #   rollers = factory.create_roller_by_json(decoded_json)
    # add the roller packets into the board object
    #   board.append(RollerPacket(rollers))
    # return render_template(dice_board.html, board=board)
    pass

@dice_bp.route('/')
def dice_base():
    # return render_template('dice.html')
    pass
