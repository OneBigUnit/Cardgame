from flask import Blueprint
from flask import render_template
from flask_login import login_required

from cardgame.game.logic.components.adts import Queue
from cardgame.game.logic.game import Game

game = Blueprint("game", __name__)


@game.route("/game/<start>")
@login_required
def play(start):
    if start == "True":
        results = Queue(start=[result for result in Game()][::-1])
        Game.store_game(results)
    return render_template("game.html", title="Card Game")


@game.route("/roundend")
@login_required
def round_results():
    results = Game.get_game()
    result = results.pop_item()
    Game.store_game(results)
    return render_template('roundend.html', title="Round Results", result=result)
