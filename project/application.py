from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/diary")
def diary():
    return render_template("diary.html")
