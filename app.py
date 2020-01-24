from boggle import Boggle
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def index():
    """ """

    board_list = boggle_game.make_board()

    return render_template("board.html", board_list=board_list)