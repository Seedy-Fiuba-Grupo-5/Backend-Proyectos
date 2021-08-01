from flask_restx import Model, fields

metrics_representation = Model('ProjectMetrics', {
        'most_popular_type': fields.String(description='Most popular type of project'),
        'avg_goal': fields.Integer(description='Average project goal'),
        'avg_duration': fields.Integer(description='Average project duration in months')
    })
