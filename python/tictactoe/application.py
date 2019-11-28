from flask import Flask, render_template, session
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():

    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):

    session["board"][row][col] = session["turn"]

    # check
    winner = check(session["board"])
    if winner:
        return render_template("game.html", game=session["board"], turn=session["turn"], winner = winner)

    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"] = "X"


    return render_template("game.html", game=session["board"], turn=session["turn"], winner = winner)

@app.route("/clear")
def clear():

    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"

    return render_template("game.html", game=session["board"], turn=session["turn"])

def check(board):

    # row
    for i in range(3):
        tmp = None
        for j in range(3):
            if not board[i][j]:
                break
            elif not tmp:
                tmp = board[i][j]
            else:
                if tmp != board[i][j]:
                    break
                elif j == 2:
                    return True

    # col
    for j in range(3):
        tmp = None
        for i in range(3):
            if not board[i][j]:
                break
            if not tmp:
                tmp = board[i][j]
            else:
                if tmp != board[i][j]:
                    break
                elif i == 2:
                    return True

    # diagonal
    if board[1][1]:

        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            return True

        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            return True

    return False
