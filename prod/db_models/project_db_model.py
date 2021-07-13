from prod import db
from prod.schemas.project_options import ProjectTypeEnum


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
    type = db.Column(db.Enum(ProjectTypeEnum),
                     nullable=False)
    goal = db.Column(db.Integer,
                     nullable=False)
    endDate = db.Column(db.String(128),
                        nullable=False)
    location = db.Column(db.String(128),
                         nullable=False)
    path = db.Column(db.Text,
                     nullable=False,
                     default='')
    image = db.Column(db.Text,
                      nullable=False,
                      default='')
    video = db.Column(db.Text,
                      nullable=True,
                      default='')

    def __init__(self,
                 name, description, hashtags, type, goal,
                 endDate, location, image):
        self.name = name
        self.description = description
        self.hashtags = hashtags
        self.type = type
        self.goal = goal
        self.endDate = endDate
        self.location = location
        self.image = image

    @classmethod
    def create(cls,
               name, description, hashtags, type, goal,
               endDate, location, image):
        enumType = None
        for item in ProjectTypeEnum:
            if item.value == type:
                enumType = item
        if not enumType:
            raise TypeError("invalid enum")
        project_model = ProjectDBModel(name, description, hashtags, enumType,
                                       goal, endDate, location, image)
        db.session.add(project_model)
        db.session.commit()
        db.session.refresh(project_model)
        return project_model

    def update(self,
               name, description, hashtags, type, goal,
               endDate, location, image):
        enumType = None
        for item in ProjectTypeEnum:
            if item.value == type:
                enumType = item
        if not enumType:
            raise TypeError("invalid enum")
        self.__init__(name, description, hashtags, enumType, goal,
                      endDate, location, image)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'hashtags': self.hashtags,
            'type': self.type.value,
            'goal': self.goal,
            'endDate': self.endDate,
            'location': self.location,
            'image': self.image
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
