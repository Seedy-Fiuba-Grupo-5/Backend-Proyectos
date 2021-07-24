from prod.db_models.commentary_db_model import CommentaryDBModel
from dev.aux_test import recreate_db


def test_get_messages_form_user_1_to_user_2(test_app,
                                            test_database):
    """Este tests muestra como se obtienen los mensajes entre dos usuarios
    """
    session = recreate_db(test_database)
    session.add(CommentaryDBModel(id_1=1,
                                  text="fdimaria@fi.uba.ar"))
    session.commit()
    session.add(CommentaryDBModel(id_1=1,
                                  text="fdimaria@fi.uba.ar"))
    session.commit()
    messages = CommentaryDBModel.get_messages_from_project(1)
    assert len(messages) == 2


def test_get_messages_form_user_1_to_user_2_and_user_2_to_user_1(test_app,
                                                                 test_database):
    """Este tests prueba que se puedan obtener los mensajes asociados a los
    dos users independientemente de que usuario es el dueño del mensaje
    """
    session = recreate_db(test_database)
    session.add(CommentaryDBModel(id_1=1,
                                  text="fdimaria@fi.uba.ar"))
    session.commit()
    session.add(CommentaryDBModel(id_1=2,
                                  text="fdimaria@fi.uba.ar"))
    session.commit()
    messages = CommentaryDBModel.get_messages_from_project(1)
    assert len(messages) == 2
