from flask import Blueprint  # , request
from flask_restful import Api, Resource
from prod.db_models.project_db_model import ProjectDBModel

project_api = Blueprint("project_api", __name__)
api = Api(project_api)


class ProjectResource(Resource):
    def get(self, project_id):
        response = ProjectDBModel.query.get(project_id)
        if response:
            return jsonify(response), 201
        return 'The project requested could not be found', 404


api.add_resource(ProjectResource, "/projects/<project_id>")
