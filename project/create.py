from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rllsampaizaayp:d43f3bdcded9b90ae41b69f13770eb99214b0fcc84f9679d8b77100794a5b017@ec2-23-21-70-39.compute-1.amazonaws.com:5432/d1974dq36r5jhs"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()