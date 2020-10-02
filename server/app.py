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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    theater = db.Column(db.String(1000))
    date = db.Column(db.DateTime)
    title = db.Column(db.String(1000))
    info = db.Column(db.String(1000))


# sync models -> db tables
db.create_all()
Theaters.query.delete()
play_list = []
# create instance of Theaters class
for play in data:
    test_play = Theaters(
        theater=play["theater"],
        date=play["date"],
        title=play["title"],
        info=play["info"],
    )
    play_list.append(test_play)

# save to db
db.session.bulk_save_objects(play_list)
db.session.commit()

# get all Theaters from db
plays = Theaters.query.all()

print(len(plays))
if __name__ == "__main__":
    app.run(debug=True)


@app.route("/data/")
def plays():
    return "<h1>data</h1>"