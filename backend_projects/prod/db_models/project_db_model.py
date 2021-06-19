from prod import db


class ProjectDBModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(128),
                     nullable=False)
    description = db.Column(db.String(128),
                            nullable=False)
    hashtags = db.Column(db.String(1000),
                         nullable=False)
    type = db.Column(db.String(128),
                     nullable=False)
    goal = db.Column(db.Integer,
                     nullable=False)
    endDate = db.Column(db.String(128),
                        nullable=False)
    location = db.Column(db.String(128),
                         nullable=False)

    def __init__(self,
                 name, description, hashtags, type, goal,
                 endDate, location):
        self.name = name
        self.description = description
        self.hashtags = hashtags
        self.type = type
        self.goal = goal
        self.endDate = endDate
        self.location = location

    @classmethod
    def create(cls,
               name, description, hashtags, type, goal,
               endDate, location):
        project_model = ProjectDBModel(name, description, hashtags,
                                       type, goal, endDate, location)
        db.session.add(project_model)
        db.session.commit()
        db.session.refresh(project_model)
        return project_model

    def update(self,
               name, description, hashtags, type, goal,
               endDate, location):
        self.__init__(name, description, hashtags, type, goal,
                      endDate, location)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'hashtags': self.hashtags,
            'type': self.type,
            'goal': self.goal,
            'endDate': self.endDate,
            'location': self.location
        }

    @staticmethod
    def delete(deleted_id):
        projects_query = ProjectDBModel.query.filter_by(id=deleted_id)
        if projects_query.count() == 0:
            return 1
        deleted_objects = ProjectDBModel.__table__.delete().where(
            ProjectDBModel.id == deleted_id)
        db.session.execute(deleted_objects)
        db.session.commit()
        return 0
