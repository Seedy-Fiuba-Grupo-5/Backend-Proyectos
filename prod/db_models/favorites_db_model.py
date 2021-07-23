from prod import db
from sqlalchemy import Column
from sqlalchemy import exc


class FavoritesProjectDBModel(db.Model):
    __tablename__ = "user_favorite_projects2"

    user_id = Column(db.Integer,
                     primary_key=True)
    project_id = db.Column(db.Integer,
                           primary_key=True)

    # Constructor de la clase.
    # PRE: Ambos id deben corresponderse con los creados en sus respectivas
    # bases de datos
    def __init__(self,
                 user_id, project_id):
        self.user_id = user_id
        self.project_id = project_id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "project_id": self.project_id
        }

    @classmethod
    def add_project_to_favorites_of_user_id(cls,
                                            user_id,
                                            project_id):
        try:
            db.session.add(FavoritesProjectDBModel(user_id, project_id))
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            # TODO: Considerar levantar un excepcion.
        return FavoritesProjectDBModel.get_favorites_of_project_id(project_id)

    def update(self):
        try:
            self.__init__(self.user_id, self.project_id)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()

    @staticmethod
    def get_favorites_of_project_id(project_id):
        projects_query = FavoritesProjectDBModel.query.filter_by(
            project_id=project_id)
        id_projects_list = \
            [user_project.user_id for user_project in projects_query.all()]
        return id_projects_list

    @staticmethod
    def delete(user_id, project_id):
        entry = FavoritesProjectDBModel.query.filter_by(
            user_id=user_id, project_id=project_id).first()
        deleted = False
        if entry:
            db.session.delete(entry)
            db.session.commit()
            deleted = True
        return deleted
