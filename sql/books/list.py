import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    authors = db.execute("SELECT author FROM authors").fetchall()

    authorsl = []
    for author in authors:
        print(author.author)
        authorsl.append(author.author)

    print(authorsl)

if __name__ == "__main__":
    main()
