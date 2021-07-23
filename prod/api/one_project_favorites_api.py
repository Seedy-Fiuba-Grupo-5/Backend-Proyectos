from flask import request
from flask_restx import Namespace, Resource
from prod.db_models.favorites_db_model import FavoritesProjectDBModel
from prod.schemas.project_body import project_body
from prod.schemas.project_representation import project_representation
from prod.schemas.project_not_found import project_not_found, \
    PROJECT_NOT_FOUND_ERROR
from prod.db_models.project_db_model import ProjectDBModel

ns = Namespace(
    'projects/<int:project_id>/favorites',
    description='Project related operations'
)


@ns.route('')
@ns.param('project_id', description='The project identifier')
class ProjectResource(Resource):
    body_swg = ns.model(project_body.name, project_body)
    code_200_swg = ns.model(project_representation.name,
                            project_representation)
    code_404_swg = ns.model(project_not_found.name, project_not_found)

    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, PROJECT_NOT_FOUND_ERROR, code_404_swg)
    def get(self, project_id):
        project_model = ProjectDBModel.query.get(project_id)
        if not project_model:
            ns.abort(404, status=PROJECT_NOT_FOUND_ERROR)
        users = FavoritesProjectDBModel.get_favorites_of_project_id(project_id)
        response_object = {
            "project_id": project_id,
            "users_id": users,
        }
        return response_object, 200

    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, PROJECT_NOT_FOUND_ERROR, code_404_swg)
    def post(self, project_id):
        """Add project to user favorites"""
        project_model = ProjectDBModel.query.get(project_id)
        if not project_model:
            ns.abort(404, status=PROJECT_NOT_FOUND_ERROR)
        try:
            data = request.get_json()
            users = FavoritesProjectDBModel.add_project_to_favorites_of_user_id(
                data['user_id'], project_id)
            response_object = {
                "project_id": project_id,
                "users_id": users,
            }
            return response_object, 201
        except KeyError:
            ns.abort(404, status='faltan valores')

    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, PROJECT_NOT_FOUND_ERROR, code_404_swg)
    def delete(self, project_id):
        """Remove project to user favorites"""
        project_model = ProjectDBModel.query.get(project_id)
        if not project_model:
            ns.abort(404, status=PROJECT_NOT_FOUND_ERROR)
        try:
            data = request.get_json()
            # cambiarlo cuando se vuelva a tener dos PKs
            deleted = FavoritesProjectDBModel.delete(
                data['user_id'], project_id)
            if deleted:
                users = \
                    FavoritesProjectDBModel.get_favorites_of_project_id(
                        project_id)
                response_object = {
                    "project_id": project_id,
                    "users_id": users,
                }
                return response_object, 200
            else:
                ns.abort(404, status='PROJECT_NOT_FOUND')  # MEJORAR ESTE ERROR
        except KeyError:
            ns.abort(404, status='MISSING_VALUES_ERROR')  # MEJORAR ESTE ERROR
