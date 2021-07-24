from flask_restx import Namespace, fields
from flask import request
from prod.api.base_resource import BaseResource
from prod.db_models.commentary_db_model import CommentaryDBModel
from prod.db_models.user_db_model import UserDBModel
from prod.exceptions import BusinessError, RepeatedEmailError, UserBlockedError
from prod.schemas.commentary_representation import commentary_representation
from prod.schemas.constants import MISSING_VALUES_ERROR, REPEATED_USER_ERROR
from prod.schemas.constants import USER_NOT_FOUND_ERROR, MISSING_ARGS_ERROR
from prod.schemas.commentary_code20 import commentary_code20

ns = Namespace(
    name='messages/<int:project_id>',
    description='All commentaries of projects related operations'
)


@ns.route('')
class UsersListResource(BaseResource):
    REGISTER_FIELDS = ("id_project", "id_user", "message", "token")
    GET_FIELDS = ('id', 'token')

    code_status = {
        RepeatedEmailError: (409, REPEATED_USER_ERROR),
        UserBlockedError: (406, 'user_blocked')
    }

    body_swg = ns.model(commentary_representation.name,
                        commentary_representation)

    code_20x_swg = ns.model(commentary_code20.name, commentary_code20)

    code_400_swg = ns.model('CommentaryOutput400', {
        'status': fields.String(example=MISSING_ARGS_ERROR),
        'missing_args': fields.List(fields.String())
    })

    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    def get(self, project_id):
        """Get all messages data"""
        try:
            json = request.get_json()
            token_decoded = UserDBModel.decode_auth_token(json['token'])
            if token_decoded != json['user_id']:
                ns.abort(404, status=USER_NOT_FOUND_ERROR)
            response_object = CommentaryDBModel.get_messages_from_project(
                project_id)
            return response_object, 200
        except KeyError:
            ns.abort(400, status=MISSING_VALUES_ERROR)

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    def post(self, project_id):
        """Adds a new message a new user"""
        try:
            data = request.get_json()
            missing_args = self.missing_values(data, self.REGISTER_FIELDS)
            if missing_args:
                ns.abort(400, status=MISSING_VALUES_ERROR,
                         missing_args=missing_args)
            token_decoded = UserDBModel.decode_auth_token(data['token'])
            id_user = data['id_user']
            if token_decoded != id_user:
                ns.abort(404, status=USER_NOT_FOUND_ERROR)
            CommentaryDBModel.add_message(data['id_project'],
                                          data['message'])
            response_object = {'id_user': data['id_user'],
                               'token': UserDBModel.encode_auth_token(
                                   data['id_user'])}
            return response_object, 201
        except BusinessError as e:
            code, status = self.code_status[e.__class__]
            ns.abort(code, status=status)
