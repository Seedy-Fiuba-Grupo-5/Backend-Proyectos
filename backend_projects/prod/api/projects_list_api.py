from flask import request
from flask_restx import Namespace, Resource, fields
from prod.db_models.project_db_model import ProjectDBModel

ns = Namespace(
    'projects',
    description='All projects related operations'
)


@ns.route('')
class ProjectsListResource(Resource):
    PJT_FIELDS = ['name', 'description', 'hashtags',
                  'type', 'goal', 'endDate', 'location']

    MISSING_VALUES_ERROR = 'Missing values'

    body_swg = ns.model('ProjectInput', {
        'name': fields.String(required=True, description='The project name'),
        'description': fields.String(
            required=True, description='The project description'),
        'hashtags': fields.String(
            required=True, description='The project hashtags'),
        'type': fields.String(required=True, description='The project types'),
        'goal': fields.Integer(required=True, description='The project goal'),
        'endDate': fields.String(
            required=True, description='The project end date'),
        'location': fields.String(
            required=True, description='The project location')
    })

    code_20x_swg = ns.model('ProjectOutput20x', {
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })

    code_400_swg = ns.model('ProjectOutput400', {
        'status': fields.String(example=MISSING_VALUES_ERROR)
    })

    @ns.marshal_with(code_20x_swg, as_list=True, code=200)
    def get(self):
        response_object =\
            [project.serialize() for project in ProjectDBModel.query.all()]
        return response_object, 200

    @ns.expect(body_swg)
    @ns.marshal_with(code_20x_swg, as_list=False, code=201)
    @ns.response(400, description=MISSING_VALUES_ERROR, model=code_400_swg)
    def post(self):
        json = request.get_json()
        if not self.check_values(json, self.PJT_FIELDS):
            ns.abort(400, self.MISSING_VALUES_ERROR)
        project_model = ProjectDBModel.create(
            name=json['name'],
            description=json['description'],
            hashtags=json['hashtags'],
            type=json['type'],
            goal=json['goal'],
            endDate=json['endDate'],
            location=json['location']
        )
        response_object = project_model.serialize()
        return response_object, 201

    @staticmethod
    def check_values(json, list):
        for value in list:
            if value not in json:
                return False
        return True
