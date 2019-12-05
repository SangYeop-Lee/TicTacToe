# TODO
# books.csv = {ispn, name, year}
# create heroku database
# decide schemas (authors, books, etc..)
# import data into database
# write python program that queries the database for book by its (partial) title or author

import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():

    books = Book.query.all()
    authors = Author.query.all()

    partialName = request.form.get("name")
    lower = partialName.lower()

    booksContainingPartialName = []
    authorsContainingPartialName = []

    for book in books:
        if lower in book.title.lower():
            booksContainingPartialName += [book.title]

    for author in authors:
        if lower in author.name.lower():
            authorsContainingPartialName += [author.name]

    return render_template("search.html", keyword=partialName, books=booksContainingPartialName, authors=authorsContainingPartialName)

@app.route("/book/<string:title>")
def book(title):

    book = Book.query.filter_by(title=title).first()
    author = Author.query.get(book.author_id).name

    return render_template("book.html", book=book, author=author)

@app.route("/author/<string:name>")
def author(name):

    author_id = Author.query.filter_by(name=name).first().id
    books = Book.query.filter_by(author_id=author_id)

    return render_template("author.html", author=name, books=books)