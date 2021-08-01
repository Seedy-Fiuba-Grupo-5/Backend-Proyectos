from flask_restx import Model, fields
from .constants import DESCRIPTIONS

project_representation = Model('ProjectRepresentation', {
    'id': fields.Integer(description=DESCRIPTIONS['id']),
    'name': fields.String(description=DESCRIPTIONS['name']),
    'description': fields.String(description=DESCRIPTIONS['description']),
    'hashtags': fields.String(description=DESCRIPTIONS['hashtags']),
    'type': fields.String(description=DESCRIPTIONS['type']),
    'goal': fields.Float(description=DESCRIPTIONS['goal']),
    'endDate': fields.String(description=DESCRIPTIONS['endDate']),
    'createdOn': fields.String(description=DESCRIPTIONS['createdOn']),
    'location': fields.String(description=DESCRIPTIONS['location']),
    'image': fields.String(description=DESCRIPTIONS['image']),
    'video': fields.String(description=DESCRIPTIONS['video']),
    'path': fields.String(description=DESCRIPTIONS['path']),
    'seer': fields.String(description=DESCRIPTIONS['seer']),
    'lat': fields.Float(description=DESCRIPTIONS['lat']),
    'lon': fields.Float(description=DESCRIPTIONS['lon'])
})
