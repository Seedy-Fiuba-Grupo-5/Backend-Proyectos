# from flask import request
from flask_restx import Namespace, Resource, fields
from prod.db_models.project_db_model import ProjectDBModel

ns = Namespace(
    'projects/<int:project_id>',
    description='Project related operations'
)


@ns.route('')
@ns.param('project_id', description='The project identifier')
class ProjectResource(Resource):
    PROJECT_NOT_FOUND_ERROR = 'The project requested could not be found'

    code_200_swg = ns.model('Project 200', {
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })

    code_404_swg = ns.model('Project 404', {
        'status': fields.String(example=PROJECT_NOT_FOUND_ERROR)
    })

    @ns.marshal_with(code_200_swg, code=200)
    @ns.response(404, description=PROJECT_NOT_FOUND_ERROR, model=code_404_swg)
    def get(self, project_id):
        project_model = ProjectDBModel.query.get(project_id)
        if not project_model:
            ns.abort(404, status=self.PROJECT_NOT_FOUND_ERROR)
        response_object = project_model.serialize()
        return response_object, 200
