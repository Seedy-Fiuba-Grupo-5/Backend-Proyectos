from flask_restx import Model, fields
from .constants import DESCRIPTIONS

project_required_body = Model('ProjectRequiredBody', {
    'name': fields.String(description=DESCRIPTIONS['name'],
                          required=True),
    'description': fields.String(description=DESCRIPTIONS['description'],
                                 required=True),
    'hashtags': fields.String(description=DESCRIPTIONS['hashtags'],
                              required=True),
    'type': fields.String(description=DESCRIPTIONS['type'],
                          required=True),
    'goal': fields.Float(description=DESCRIPTIONS['goal'],
                         required=True),
    'endDate': fields.String(description=DESCRIPTIONS['endDate'],
                             required=True),
    'location': fields.String(description=DESCRIPTIONS['location'],
                              required=True),
    'image': fields.String(description=DESCRIPTIONS['image'],
                           required=True),
    'video': fields.String(description=DESCRIPTIONS['video'],
                           required=False),
    'lat': fields.Float(description=DESCRIPTIONS['lat'],
                        required=True),
    'lon': fields.Float(description=DESCRIPTIONS['lon'],
                        required=True)
})
