import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    authors = set()
    for isbn, title, author, year in reader:
        authors.add(author)

    for author in authors:
        tmp = Author(name=author)
        db.session.add(tmp)
        print(f"Added {tmp.name}.")

    db.session.commit()



if __name__ == "__main__":
    with app.app_context():
        main()
