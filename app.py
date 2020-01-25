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
    
    word = request.json["word"].lower()
    board = session["board_list"]
    result = boggle_game.check_valid_word(board, word)
    
    return jsonify(result=result)


@app.route("/add-score", methods=["POST"])
def add_score():
    """ """

    score = int(request.json["score"])
    if session.get("attempts", -1) == -1:
        session["attempts"] = 1
        session["high_score"] = score
    else: 
        attempts = session["attempts"] 
        attempts += 1
        session["attempts"] = attempts
        if score > session["high_score"]:
            session["high_score"] = score
    
    return jsonify(highScore=session["high_score"], attempts=session["attempts"])

