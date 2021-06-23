from flask_restx import Model, fields
from .constants import DESCRIPTIONS

project_body = Model('ProjectBody', {
    'name': fields.String(description=DESCRIPTIONS['name']),
    'description': fields.String(description=DESCRIPTIONS['description']),
    'hashtags': fields.String(description=DESCRIPTIONS['hashtags']),
    'type': fields.String(description=DESCRIPTIONS['type']),
    'goal': fields.Integer(description=DESCRIPTIONS['goal']),
    'endDate': fields.String(description=DESCRIPTIONS['endDate']),
    'location': fields.String(description=DESCRIPTIONS['location']),
    'image': fields.String(description=DESCRIPTIONS['image'])
})
