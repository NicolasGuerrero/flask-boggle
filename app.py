from boggle import Boggle
from flask import Flask, render_template, session, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route("/")
def index():
    """ """

    board_list = boggle_game.make_board()
    session["board_list"] = board_list
    return render_template("board.html", board_list=board_list)


@app.route("/test-word", methods=["POST"])
def test_word():
    """ """
    # import pdb; pdb.set_trace()
    word = request.json["word"].lower()
    board = session["board_list"]
    result = boggle_game.check_valid_word(board, word)
   
    return jsonify(response=result)