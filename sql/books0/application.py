# TODO
# books.csv = {ispn, name, year}
# create heroku database
# decide schemas (authors, books, etc..)
# import data into database
# write python program that queries the database for book by its (partial) title or author

import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

books = db.execute("SELECT isbn, book, author, year FROM books INNER JOIN authors ON books.author_id=authors.id").fetchall()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    partialName = request.form.get("name")
    booksContainingPartialName = []
    print(partialName)


    for book in books:
        if partialName in book[1] or partialName in book[2]:
            booksContainingPartialName += [book]

    if booksContainingPartialName:
        return render_template("search.html", books=booksContainingPartialName)

    return render_template("search.html", books=None)