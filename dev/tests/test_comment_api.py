import json

from dev.aux_test import recreate_db
from prod.db_models.commentary_db_model import CommentaryDBModel


def test_post_commentary(test_app,
                         test_database):
    """Este test muestra como se crea un comentario asociado un proyecto"""
    session = recreate_db(test_database)
    client = test_app.test_client()
    body = {
        "id_project": 1,
        "user_id": 1,
        "message": "Di Maria",
        "token": CommentaryDBModel.encode_auth_token(1),
    }
    response = client.post(
        "/commentary/1",
        data=json.dumps(body),
        content_type="application/json"
    )
    assert response.status_code == 201


def test_get_commentary(test_app,
                        test_database):
    """Este test muestra como se obtienen los comentarios asociados a un
    proyecto"""
    session = recreate_db(test_database)
    client = test_app.test_client()
    body = {
        "id_project": 1,
        "user_id": 1,
        "message": "Di Maria",
        "token": CommentaryDBModel.encode_auth_token(1)
    }
    response = client.post(
        "/commentary/1",
        data=json.dumps(body),
        content_type="application/json"
    )
    assert response.status_code == 201
    body = {
        "id_project": 1,
        "user_id": 1,
        "message": "Di Maria",
        "token": CommentaryDBModel.encode_auth_token(1)
    }
    response = client.post(
        "/commentary/1",
        data=json.dumps(body),
        content_type="application/json"
    )
    assert response.status_code == 201
    body = {
        "user_id": 1,
        "token": CommentaryDBModel.encode_auth_token(1),
    }
    response = client.get(
        "/commentary/1",
        data=json.dumps(body),
        content_type="application/json"
    )
    assert response.status_code == 200
    patch_data = json.loads(response.data.decode())
    assert len(patch_data) == 2
