from flask import Flask, request, jsonify
from flask_cors import CORS

from App.src.Project import *
from App import app

cors = CORS(app)
projects = Projects()

@app.route("/projects", methods=["GET"])
def get_projects():
    return jsonify(list(projects.projects.values()))

@app.route("/projects", methods=["POST"])
def create_project():
    project_name = request.get_json()['name']
    projects.add_project(project_name)
