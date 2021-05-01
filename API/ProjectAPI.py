import json

from flask import Flask, request
from flask_cors import CORS

from src.Project import *

app = Flask(__name__)
cors = CORS(app)
projects = Projects()

@app.route("/projects", methods=["GET"])
def get_projects():
    return json.dumps(projects.projects)

@app.route("/projects", methods=["POST"])
def create_project():
    project_name = request.get_json()
    projects.add_project(project_name)
