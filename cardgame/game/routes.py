from flask import Blueprint
from flask import render_template
from cardgame.game.logic.game import Game
from cardgame.game.logic.components.adts import Queue

game = Blueprint("game", __name__)


@game.route("/game/<start>")
def play(start):

    if start == "True":
        results = Queue(start=[result for result in Game()][::-1])
        print(results.reveal())
        Game.store_game(results)
    return render_template("game.html", title="Card Game")


@game.route("/roundend")
def round_results():
    results = Game.get_game()
    print(f"Before Results: {results.reveal()}")
    result = results.pop_item()
    print(f"After Results: {results.reveal()}\n\nResult: {result}\n\n")
    Game.store_game(results)
    return render_template('roundend.html', title="Round Results", result=result)
