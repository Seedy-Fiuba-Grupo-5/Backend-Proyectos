from flask import Blueprint, request
from flask_restful import Api, Resource
from prod.db_models.project_db_model import ProjectDBModel

projects_api = Blueprint("projects_api", __name__)
api = Api(projects_api)


class ProjectsResource(Resource):
    def get(self):
        response_object =\
            [project.serialize() for project in ProjectDBModel.query.all()]
        return response_object, 200

    def post(self):
        name = request.get_json()['name']
        db.session.add(ProjectDBModel(name=name))
        db.session.commit()
        return request.get_json(), 201

api.add_resource(ProjectsResource, "/projects")
