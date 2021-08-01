from flask_restx import Model, fields

commentary_representation = Model('CommentaryRepresentation', {
    'owner_id': fields.Integer(description='owner_id'),
    'project_id': fields.Integer(description='project_id'),
    'message': fields.String(description='message'),
    'token': fields.String(description='token'),
})
