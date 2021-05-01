from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def Main():
    return jsonify(hello="project")