import datetime
from prod import db
import flask
import jwt


# Clase representativa del schema que almacena a cada uno de los
# usuarios en el sistema. Cada entrada consta de un id, name, lastname, email
# y un estado activo que por defecto es True
class CommentaryDBModel(db.Model):
    __tablename__ = "commentary"
    EXPIRATION_TIME = 86400  # 1 dia = 86400 segundos
    column_not_exist_in_db = db.Column(db.Integer,
                                       primary_key=True)
    id_1 = db.Column(db.Integer)

    text = db.Column(db.String(280),
                     nullable=False)

    date = db.Column(db.DateTime,
                     nullable=False)

    # Constructor de la clase.
    # PRE: Name tiene que ser un string de a lo sumo 128 caracteres, al igual
    # que password, lastname y email.
    def __init__(self,
                 id_1,
                 text):
        self.id_1 = id_1
        self.text = text
        self.date = datetime.datetime.now()

    def serialize(self):
        return {
            "id_1": self.id_1,
            "text": self.text,
            "date": self.date.strftime("%m/%d/%Y, %H:%M:%S")
        }

    @staticmethod
    def get_messages_from_project(requested_id):
        query = CommentaryDBModel.query.filter_by(id_1=requested_id)
        if len(query.all()) == 0:
            return {}
        response_object = \
            [message.serialize() for message in query.all()]
        return response_object, 200

    @classmethod
    def add_message(cls,
                    id_1,
                    message):
        db.session.add(CommentaryDBModel(id_1=id_1,
                                         text=message))
        db.session.commit()

    @classmethod
    def encode_auth_token(cls, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        payload = {
            'exp': datetime.datetime.utcnow() +
            datetime.timedelta(days=0,
                               seconds=cls.EXPIRATION_TIME),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            flask.current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        ).decode("utf-8")

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, flask.current_app.config.get(
                'SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
