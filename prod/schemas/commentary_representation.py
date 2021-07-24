from flask_restx import Model, fields
from .constants import DESCRIPTIONS

commentary_representation = Model('CommentaryRepresentation', {
    'owner_id': fields.Integer(description=DESCRIPTIONS['owner_id']),
    'project_id': fields.Integer(description=DESCRIPTIONS['project_id']),
    'message': fields.String(description=DESCRIPTIONS['message']),
    'token': fields.String(description=DESCRIPTIONS['token']),
})
