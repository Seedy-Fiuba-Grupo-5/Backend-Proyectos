from flask import Blueprint, request
from flask_restful import Api, Resource
from prod import db
from prod.db_models.project_db_model import ProjectDBModel

projects_list_api = Blueprint("projects_list_api", __name__)
api = Api(projects_list_api)


class ProjectsListResource(Resource):
    def get(self):
        response_object =\
            [project.serialize() for project in ProjectDBModel.query.all()]
        return response_object, 200

    def post(self):
        name = request.get_json()['name']
        project_model = ProjectDBModel(name=name)
        db.session.add(project_model)
        db.session.commit()
        db.session.refresh(project_model)
        response_object = project_model.serialize()
        return response_object, 201


api.add_resource(ProjectsListResource, "/projects")
