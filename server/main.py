import os

import flask_sqlalchemy
from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

import output

print(output.output)
"""
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
    return f"post('{self.theater}', '{self.date}', '{self.title}', '{self.info}')" """
