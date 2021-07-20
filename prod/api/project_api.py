from flask import request
from flask_restx import Namespace, Resource
from prod.db_models.project_db_model import ProjectDBModel
from prod.schemas.project_body import project_body
from prod.schemas.project_representation import project_representation
from prod.schemas.project_not_found import project_not_found,\
    PROJECT_NOT_FOUND_ERROR
from prod.schemas.constants import PROJECT_DELETED

ns = Namespace(
    'projects/<int:project_id>',
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
        response_object = project_model.serialize()
        return response_object, 200

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    def patch(self, project_id):
        json = request.get_json()
        project_model = ProjectDBModel.query.get(project_id)
        try:
            project_model.update(
                name=json.get('name', project_model.name),
                description=json.get('description', project_model.description),
                hashtags=json.get('hashtags', project_model.hashtags),
                type=json.get('type', project_model.type.value),
                goal=json.get('goal', project_model.goal),
                endDate=json.get('endDate', project_model.endDate),
                location=json.get('location', project_model.location),
                image=json.get('image', project_model.image),
                video=json.get('video', project_model.video)
            )
        except TypeError:
            ns.abort(400, status="The type selected in not a valid one")
        # Refresh project
        project_model = ProjectDBModel.query.get(project_id)
        response_object = project_model.serialize()
        return response_object, 200

    @ns.response(204, PROJECT_DELETED)
    @ns.response(404, PROJECT_NOT_FOUND_ERROR, code_404_swg)
    def delete(self, project_id):
        value = ProjectDBModel.delete(project_id)
        if value == 1:
            ns.abort(404, status=PROJECT_NOT_FOUND_ERROR)
        return '', 204
