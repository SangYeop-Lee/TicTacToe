from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dday(db.Model):

    __tablename__ = "ddays"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)

class Schedule(db.Model):

    __tablename__ = "schedules"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    beginning = db.Column(db.Date, nullable=False)
    end = db.Column(db.Date)
    todo = db.Column(db.Boolean, default=False)
    tag = db.Column(db.String)

class Diary:

    __tablename__ = "diaries"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)