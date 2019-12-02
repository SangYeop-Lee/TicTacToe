import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    counter = 0

    db.execute("CREATE TABLE authors (id SERIAL PRIMARY KEY, author VARCHAR NOT NULL);")

    authors = set()
    for row in reader:
        authors.add(row[2])
        counter += 1
        print(counter)

    counter = 0

    for author in authors:
        db.execute("INSERT INTO authors (author) VALUES (:author)", {"author": author})
        counter += 1
        print(counter)

    db.commit()

if __name__ == "__main__":
    main()