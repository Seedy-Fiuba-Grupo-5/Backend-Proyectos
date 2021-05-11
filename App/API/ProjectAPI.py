from flask import request, jsonify, Response, json
from flask_cors import CORS

from App.src.Project import *
from App import app

cors = CORS(app)
projects = Projects()

@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify(projects.get_projects()), 201

@app.route("/projects", methods=["POST"])
def create_project():
    projects.add_project(request.get_json()['name'])
    return request.get_json(), 201

@app.route("/projects/<project_id>", methods=["GET"])
def get_project_by_id(project_id):
    response = projects.get_project_by_id(project_id)
    if response:
        return jsonify(response), 201
    return 'The project requested could not be found', 404
