from flask import Blueprint, request
from flask_restful import Api, Resource
from prod import db
from prod.db_models.project_db_model import ProjectDBModel

projects_list_api = Blueprint("projects_list_api", __name__)
api = Api(projects_list_api)


class ProjectsListResource(Resource):
    PJT_FIELDS = ['name', 'description', 'hashtags',
                  'type', 'goal', 'endDate', 'location']

    def get(self):
        response_object =\
            [project.serialize() for project in ProjectDBModel.query.all()]
        return response_object, 200

    @staticmethod
    def check_values(json, list):
        for value in list:
            if value not in json:
                return False
        return True

    def post(self):
        json = request.get_json()
        if not self.check_values(json, self.PJT_FIELDS):
            return 'insufficient information for Project creation', 500
        project_model = ProjectDBModel(name=json['name'],
                                       description=json['description'],
                                       hashtags=json['hashtags'],
                                       type=json['type'],
                                       goal=json['goal'],
                                       endDate=json['endDate'],
                                       location=json['location'])
        db.session.add(project_model)
        db.session.commit()
        db.session.refresh(project_model)
        response_object = project_model.serialize()
        return response_object, 201


api.add_resource(ProjectsListResource, "/projects")
