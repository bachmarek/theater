from common import output
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///theater_db"

# db = SQLAlchemy(app)

# data = output.webscraped()


# class Theaters(db.Model):
#     __tablename__ = "theaters"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     theater = db.Column(db.String(1000))
#     date = db.Column(db.DateTime)
#     title = db.Column(db.String(1000))
#     info = db.Column(db.String(1000))


# # sync models -> db tables
# db.create_all()

# # first object
# fp = data[0]

# # create instance of Theaters class
# test_play = Theaters(
#     theater=fp["theater"], date=fp["date"], title=fp["title"], info=fp["info"])

# # save to db
# db.session.add(test_play)
# db.session.commit()

# # get all Theaters from db
# plays = Theaters.query.all()

# print(len(plays))


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@app.route("/data")
def data():
    return "data route"
