from flask import Blueprint  # , request
from flask_restful import Api, Resource
from prod.db_models.project_db_model import ProjectUserDBModel

projects_api = Blueprint("projects_api", __name__)
api = Api(projects_api)


class ProjectsResource(Resource):
    def get(self):
        response_object =\
            [project.serialize() for project in ProjectDBModel.query.all()]
        return response_object, 200


api.add_resource(ProjectsResource, "/projects")
