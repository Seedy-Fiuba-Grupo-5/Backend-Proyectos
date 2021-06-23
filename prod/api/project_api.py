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

    body_swg = ns.model('ProjectInput', {
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location'),
        'image': fields.String(description='The project image url')
    })

    code_200_swg = ns.model('ProjectOutput200', {
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location'),
        'image': fields.String(description='The project image url')
    })

    code_404_swg = ns.model('ProjectOutput404', {
        'status': fields.String(example=PROJECT_NOT_FOUND_ERROR)
    })

    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, PROJECT_NOT_FOUND_ERROR, code_404_swg)
    def get(self, project_id):
        project_model = ProjectDBModel.query.get(project_id)
        if not project_model:
            ns.abort(404, status=self.PROJECT_NOT_FOUND_ERROR)
        response_object = project_model.serialize()
        return response_object, 200

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
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
            location=json.get('location', project_model.location),
            image=json.get('image', project_model.image)
        )
        # Refresh project
        project_model = ProjectDBModel.query.get(project_id)
        response_object = project_model.serialize()
        return response_object, 200
