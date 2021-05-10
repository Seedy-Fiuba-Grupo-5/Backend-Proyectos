from flask import request, jsonify, Response
from flask_cors import CORS

from App.src.Project import *
from App import app

cors = CORS(app)
projects = Projects()

@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify(projects.get_projects())

@app.route("/projects", methods=["POST"])
def create_project():
    projects.add_project(request.get_json()['name'])
    return Response(request.get_json(), status=201)

@app.route("/projects/<project_id>", methods=["GET"])
def get_project_by_id(project_id):
    return jsonify(projects.get_project_by_id(project_id))
