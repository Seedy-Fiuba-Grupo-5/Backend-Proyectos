from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
from App.API import *

db.create_all()
db.session.commit()

@app.route("/")
def Main():
    return jsonify(hello="project")