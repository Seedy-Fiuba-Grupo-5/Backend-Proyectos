from flask import Blueprint, jsonify  # , request
from flask_restful import Api, Resource
from prod.db_models.project_db_model import ProjectDBModel

project_api = Blueprint("project_api", __name__)
api = Api(project_api)


class ProjectResource(Resource):
    def get(self, project_id):
        project_model = ProjectDBModel.query.get(project_id)
        if not project_model:
            return 'The project requested could not be found', 404
        response_object = project_model.serialize()
        return response_object, 200


api.add_resource(ProjectResource, "/projects/<project_id>")
