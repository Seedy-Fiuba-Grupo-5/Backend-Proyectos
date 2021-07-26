from prod import db
from prod.db_models.rating_db_model import RatingDBModel
from prod.schemas.project_options import ProjectTypeEnum
from prod.db_models.favorites_db_model import FavoritesProjectDBModel


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
                     nullable=True,
                     default='')
    image = db.Column(db.Text,
                      nullable=False,
                      default='')
    video = db.Column(db.Text,
                      nullable=True,
                      default='')
    seer = db.Column(db.String(128),
                     nullable=True)
    createdOn = db.Column(db.String(128),
                          nullable=True)
    lat = db.Column(db.Float,
                    nullable=False)
    lon = db.Column(db.Float,
                    nullable=False)

    def __init__(self,
                 name, description, hashtags, type, goal,
                 endDate, location, image, createdOn, path, lat, lon):
        self.name = name
        self.description = description
        self.hashtags = hashtags
        self.type = type
        self.goal = goal
        self.endDate = endDate
        self.location = location
        self.image = image
        self.seer = ""
        self.createdOn = createdOn
        self.path = path
        self.lat = lat
        self.lon = lon

    @staticmethod
    def add_seer(string,
                 id_project):
        user_model = ProjectDBModel.query.filter_by(id=id_project).first()
        user_model.seer = string
        db.session.commit()

    @classmethod
    def create(cls,
               name, description, hashtags, type, goal,
               endDate, location, image, createdOn, path, lat, lon):
        enumType = None
        for item in ProjectTypeEnum:
            if item.value == type:
                enumType = item
        if not enumType:
            raise TypeError("invalid enum")
        project_model = ProjectDBModel(name, description, hashtags, enumType,
                                       goal, endDate, location, image,
                                       createdOn, path, lat, lon)
        db.session.add(project_model)
        db.session.commit()
        db.session.refresh(project_model)
        return project_model

    def update(self,
               name, description, hashtags, type, goal,
               endDate, location, image, video, path, lat, lon):
        enumType = None
        for item in ProjectTypeEnum:
            if item.value == type:
                enumType = item
        if not enumType:
            raise TypeError("invalid enum")
        self.__init__(name, description, hashtags, enumType, goal,
                      endDate, location, image, self.createdOn, path,
                      lat, lon)
        self.video = video  # Agregar un test para esto
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
            'image': self.image,
            'video': self.video,
            'path': self.path,
            'seer': self.seer,
            'createdOn': self.createdOn,
            'lat': self.lat,
            'lon': self.lon,
            'favorites': FavoritesProjectDBModel.get_favorites_of_project_id(self.id),
            'rating': RatingDBModel.get_average_for_project(self.id)
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
