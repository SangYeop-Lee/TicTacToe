from forms import PasswordForm, DdayForm
import datetime
from classes import DaysLeft

from flask import Flask, render_template, request, redirect, url_for, session
from models import *
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rllsampaizaayp:d43f3bdcded9b90ae41b69f13770eb99214b0fcc84f9679d8b77100794a5b017@ec2-23-21-70-39.compute-1.amazonaws.com:5432/d1974dq36r5jhs"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.config["SECRET_KEY"] = os.urandom(24)

# login https://github.com/mcchae/Flask-Login

@app.route("/", methods=["GET", "POST"])
def index():
    form = PasswordForm()

    if form.validate_on_submit():

        print(form.password.data)

        if form.password.data == "password":
            return redirect(url_for("home"))

        else:
            message = "wrong password"
            return render_template("password.html", form=form, message=message)

    return render_template("password.html", form=form)


@app.route("/home", methods=["GET", "POST"])
def home():
    ddays = Dday.query.all()
    ddayslist = []
    for dday in ddays:
        ddayslist.append(DaysLeft(dday.name, dday.date))

    form = DdayForm()

    if form.validate_on_submit():

        dday = Dday(name=form.name.data, date=form.date.data)
        db.session.add(dday)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('index.html', ddays=ddayslist)


@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/diary") # match with real url
def diary(): # match with url_for in index.html
    return render_template("diary.html") # template

if __name__ == '__main__':
    app.run(debug=True)