import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    authors = Author.query.all()
    f = open("books.csv")
    reader = csv.reader(f)

    for isbn, title, author, year in reader:

        author_id=Author.query.filter_by(name=author).first().id
        book = Book(isbn=isbn, title=title, author_id=author_id, year=year)
        db.session.add(book)
        print(f"Added {book.title}.")

    db.session.commit()



if __name__ == "__main__":
    with app.app_context():
        main()
