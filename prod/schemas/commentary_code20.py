from flask_restx import Model, fields

commentary_code20 = Model('Commentary output 20x', {
    "id": fields.Integer(description='One user id'),
    'id_project': fields.Integer(description='One project id'),
    "token": fields.String(description='Token associated')
})
