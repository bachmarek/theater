from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import flask_sqlalchemy
import os

import output
'''
app = Flask(__name__) 
 if __name__ == "__main__":
  app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Data(db.Model):
  theater = db.Column(db.String, nullable=False)
  ##date = db.Column(db.DateTime, nullable=False)
  date = db.Column(db.String, nullable=False)
  title = db.Column(db.String, nullable=False)
  info = db.Column(db.String, nullable=False)

  def __repr__(self):
    return f"post('{self.theater}', '{self.date}', '{self.title}', '{self.info}')" '''