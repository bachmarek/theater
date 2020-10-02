from common import output
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater_db"

db = SQLAlchemy(app)

data = output.webscraped()


class Theaters(db.Model):
    __tablename__ = "theaters"
    theater = db.Column(db.String(100), primary_key=True)
    date = db.Column(db.DateTime)
    title = db.Column(db.String(100))
    info = db.Column(db.String(100))

    ## wrong
    def __init__(self, theater, date, title, info):
        for i in data:
            self.theater = theater
            self.date = date
            self.title = title
            self.info = info
            play = Theaters(data[i])
            db.session.add(play)
            db.session.commit()


# print(data)
