from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, nullable=False)
    # author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)
    year = db.Column(db.String, nullable=False)

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)