from common import output
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater_db"

db = SQLAlchemy(app)


class Theaters(db.Model):
    theater = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.DateTime)
    title = db.Column(db.String(100))
    info = db.Column(db.String(100))


@app.route("/<theater>/<date>/<title>/<info>")
def index(theater, date, title, info):
    play = Theaters(theater=theater, date=date, title=title, info=info)
    db.session.add(play)
    db.session.commit()

    return "added play"


# print(output.output_func())
