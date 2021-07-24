from flask import request
from flask_restx import Namespace, Resource
from prod.db_models.project_db_model import ProjectDBModel
from prod.schemas.project_body import project_body
from prod.schemas.project_representation import project_representation
from prod.schemas.project_not_found import project_not_found,\
    PROJECT_NOT_FOUND_ERROR

ns = Namespace(
    'projects/<int:project_id>/rate',
    description='Project related operations'
)


@ns.route('')
@ns.param('project_id', description='The project identifier')
class ProjectResource(Resource):
    body_swg = ns.model(project_body.name, project_body)
    code_200_swg = ns.model(project_representation.name,
                            project_representation)
    code_404_swg = ns.model(project_not_found.name, project_not_found)

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    def post(self, project_id):
        json = request.get_json()
        project_model = ProjectDBModel.query.get(project_id)
        if not project_model:
            ns.abort(404, status=PROJECT_NOT_FOUND_ERROR)
        try:
            project_model.add_rating(rating=json.get('rating', -1))
        except TypeError:
            ns.abort(400, status="The rating is not valid")
        # Refresh project
        project_model = ProjectDBModel.query.get(project_id)
        response_object = project_model.serialize()
        return response_object, 200
