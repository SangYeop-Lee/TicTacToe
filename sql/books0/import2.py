import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():

    # Save authors list in authors
    reader = db.execute("SELECT author FROM authors").fetchall()

    authors = []
    for author in reader:
        authors.append(author.author)

    # Save books in books
    f = open("books.csv")
    reader = csv.reader(f)

    counter =0
    for row in reader:
        db.execute("INSERT INTO books (isbn, book, author_id, year) VALUES (:isbn, :book, :author_id, :year)", {"isbn": row[0], "book": row[1], "author_id": authors.index(row[2]), "year": row[3]})
        counter += 1
        print(counter)

    db.commit()

if __name__ == "__main__":
    main()