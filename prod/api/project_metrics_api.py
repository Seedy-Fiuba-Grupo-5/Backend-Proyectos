from flask import request
from flask_restx import Namespace, Resource, fields
from flask_restx import Model, fields

from prod.db_models.project_db_model import ProjectDBModel
from prod.schemas.project_options import ProjectTypeEnum

ns = Namespace(
    'projects/metrics',
    description='All projects metrics'
)

@ns.route('')
class ProjectsListResource(Resource):
    metrics_representation = Model('ProjectMetrics', {
        'most_popular_type': fields.Integer(description='Most popular type of project'),
        'avg_duration': fields.Integer(description='Average project duration')
    })
    code_20x_swg = ns.model(metrics_representation.name,
                            metrics_representation)

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    def get(self):
        response_body = {}
        response_body["most_popular_type"] = self.get_most_popular_type()
        return response_body, 200

    def get_most_popular_type(self):
        maximo = 0
        type_actual = "None"
        for item in ProjectTypeEnum:
            cant = len([project.id for project in ProjectDBModel.query.filter_by(type=item)])
            if cant > maximo:
                maximo = cant
                type_actual = item.value
        return type_actual
