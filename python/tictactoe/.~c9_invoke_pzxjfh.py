from flask import Flask
from flask_session import Session
import datetime

app = Flask(__name__)

@app.route("/<string:name>")
def index(name):
    now = datetime.datetime.now()
    is_new_years = now.month == 1 and now.day == 1
    return render_template("index.html", is_new_years=is_new_years)
