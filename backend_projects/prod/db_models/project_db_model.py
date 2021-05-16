from prod import db


class ProjectDBModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(128),
                     unique=True,
                     nullable=False)

    def __init__(self,
                 name):
        self.name = name

    # @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
