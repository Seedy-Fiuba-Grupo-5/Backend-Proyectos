from flask_restx import Model, fields
from .constants import MISSING_VALUES_ERROR

missing_values = Model('MissingValues', {
    'status': fields.String(example=MISSING_VALUES_ERROR)
})
