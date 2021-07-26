from flask import request
from flask_restx import Namespace, Resource
from prod.db_models.rating_db_model import RatingDBModel
from prod.schemas.project_body import project_body
from prod.schemas.project_representation import project_representation
from prod.schemas.missing_values import MISSING_VALUES_ERROR

ns = Namespace(
    'projects/<int:project_id>/rate',
    description='Project rating related operations'
)


@ns.route('')
@ns.param('project_id', description='The project identifier')
class ProjectResource(Resource):
    body_swg = ns.model(project_body.name, project_body)
    code_200_swg = ns.model(project_representation.name,
                            project_representation)

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    def post(self, project_id):
        json = request.get_json()
        if not json["id_user"] or not json["rating"]:
            ns.abort(404, status=MISSING_VALUES_ERROR)
        try:
            RatingDBModel.add_rating(json["id_user"], project_id, json["rating"])
        except TypeError:
            ns.abort(400, status="The rating is not valid")
        return RatingDBModel.get_rating_from_project_user(json["id_user"], project_id)

    @ns.response(200, 'Success', code_200_swg)
    def get(self, project_id):
        if not request.args.get('id_user'):
            ns.abort(404, status=MISSING_VALUES_ERROR)
        return RatingDBModel.get_rating_from_project_user(id_user=request.args.get('id_user'),
                                                          id_project=project_id)
