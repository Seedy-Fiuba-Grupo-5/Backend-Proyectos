from App import db


# Clase que modela la base de datos user. Consta de un id, email y
# si esta activa
class ProjectsEntry(db.Model):
    __tablename__ = "ProjectsEntry"

    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(128),
                      unique=True,
                      nullable=False)

    # Creacion de la tabla
    def __init__(self,
                 name):
        self.name = name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
