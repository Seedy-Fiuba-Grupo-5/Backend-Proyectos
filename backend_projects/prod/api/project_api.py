from flask import request
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
    PROJECT_DELETED = 'The project was deleted'

    body_swg = ns.model('ProjectInput', {
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })

    code_200_swg = ns.model('ProjectOutput200', {
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })

    code_404_swg = ns.model('ProjectOutput404', {
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

    @ns.response(204, description=PROJECT_DELETED)
    @ns.response(404, description=PROJECT_DELETED, model=code_404_swg)
    def delete(self, project_id):
        value = ProjectDBModel.delete(project_id)
        if value == 1:
            ns.abort(404, status=self.PROJECT_DELETED)
        return '', 204

    @ns.expect(body_swg)
    @ns.marshal_with(code_200_swg, code=200)
    def patch(self, project_id):
        json = request.get_json()
        project_model = ProjectDBModel.query.get(project_id)
        project_model.update(
            name=json.get('name', project_model.name),
            description=json.get('description', project_model.description),
            hashtags=json.get('hashtags', project_model.hashtags),
            type=json.get('type', project_model.type),
            goal=json.get('goal', project_model.goal),
            endDate=json.get('endDate', project_model.endDate),
            location=json.get('location', project_model.location)
        )
        # Refresh project
        project_model = ProjectDBModel.query.get(project_id)
        response_object = project_model.serialize()
        return response_object, 200
