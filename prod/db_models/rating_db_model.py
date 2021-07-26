from prod import db


# Clase representativa del schema que almacena a cada uno de los
# ratings de los proyectos en el sistema. Cada entrada consta de un
# id de usuario, rating, id de proyecto
class RatingDBModel(db.Model):
    __tablename__ = "rating"

    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    id_project = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __init__(self, id_user, id_project, rating):
        self.id_user = id_user
        self.id_project = id_project
        self.rating = rating

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_project": self.id_project,
            "rating": self.rating
        }

    @staticmethod
    def get_rating_from_project_user(id_user, id_project):
        query = RatingDBModel.query.filter_by(id_user=id_user, id_project=id_project)
        if len(query.all()) == 0:
            return {}
        response_object = \
            [rating.serialize() for rating in query.all()]
        return response_object, 200

    @classmethod
    def add_rating(cls, id_user, id_project, rating):
        if rating < 1 or rating > 5:
            raise TypeError("invalid rating")
        query = RatingDBModel.query.filter_by(id_user=id_user, id_project=id_project)
        if len(query.all()) != 0:
            item = query.first()
            item.__init__(id_user=item.id_user, id_project=item.id_project, rating=rating)
        else:
            db.session.add(RatingDBModel(id_user, id_project, rating))
        db.session.commit()

    @classmethod
    def get_average_for_project(cls, id_project):
        query = RatingDBModel.query.filter_by(id_project=id_project)
        if len(query.all()) == 0:
            return 0
        total = 0
        for item in query.all():
            total += item.rating
        return total/len(query.all())
