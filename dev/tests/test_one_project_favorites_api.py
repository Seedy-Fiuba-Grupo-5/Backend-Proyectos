import json
from dev.aux_test import recreate_db


def test_dada_una_db_vacia_get_a_users_barra_id_1_barra_favorites_devuelve_project_not_found(test_app,
                                                                                             test_database):
    """
    Dada una base de datos vacia
    Cuando GET "/users/1/favorites"
    Entonces obtengo status 404
    Y obtengo el cuerpo:
        "status": "The project requested could not be found",
        "message": <mensaje de error>
    """
    session = recreate_db(test_database)
    client = test_app.test_client()
    response = client.get("/projects/1/favorites")
    assert response is not None
    assert response.status_code == 404
    user = json.loads(response.data.decode())
    assert user['status'] == "The project requested could not be found"


def test_dada_una_db_con_projecto_de_id_1_sin_usuarios_que_lo_hayan_faveado__get_a_projects_barra_id_1_barra_favorites_devuelve_una_lista_vacia(
        test_app,
        test_database):
    """
    Dada una base de datos con un proyecto
    que no tiene usuarios que lo hayan faveado
    Cuando GET "/projects/1/favorites"
    Entonces obtengo status 200
    Y obtengo el cuerpo:
        "project_id": 1,
        "users_id": []
    """
    session = recreate_db(test_database)
    client = test_app.test_client()
    body = {
        "name": "Colombia",
        "description": "string",
        "hashtags": "#pruebaaaa #adeu",
        "type": "Art",
        "goal": 0,
        "path": "",
        "endDate": "string",
        "location": "string",
        "image": "string",
        "lat": 80.60971,
        "lon": -74.08175
    }
    client.post(
        "/projects",
        data=json.dumps(body),
        content_type="application/json"
    )
    response = client.get("/projects/1/favorites")
    assert response is not None
    assert response.status_code == 200
    user = json.loads(response.data.decode())
    assert user['project_id'] == 1
    assert len(user['users_id']) == 0


def test_dada_una_db_con_usuario_de_id_1_post_a_users_barra_id_1_barra_favorites_con_el_cuerpo_correcto_entonces_obtengo(
        test_app,
        test_database):
    """
    Dada una base de datos con un proyecto
    Cuando Post "/projects/1/favorites" con user_id = 1
    Entonces obtengo status 201
    Y obtengo el cuerpo:
        "project_id": 1,
        "users_id": [
            1
        ],
    """
    session = recreate_db(test_database)
    client = test_app.test_client()
    body = {
        "name": "Colombia",
        "description": "string",
        "hashtags": "#pruebaaaa #adeu",
        "type": "Art",
        "goal": 0,
        "path": "",
        "endDate": "string",
        "location": "string",
        "image": "string",
        "lat": 80.60971,
        "lon": -74.08175
    }
    client.post(
        "/projects",
        data=json.dumps(body),
        content_type="application/json"
    )
    body = {
        "user_id": 1
    }
    post_response = client.post("/projects/1/favorites",
                                data=json.dumps(body),
                                content_type="application/json")
    assert post_response is not None
    assert post_response.status_code == 201
    user = json.loads(post_response.data.decode())
    assert user['project_id'] == 1
    assert user["users_id"][0] == 1

    old_response = json.loads(post_response.data.decode())
    get_response = client.get("/projects/1/favorites")
    assert get_response.status_code == 200
    new_response = json.loads(get_response.data.decode())
    for field in old_response.keys():
        assert old_response[field] == new_response[field]


def test_dada_una_db_con_proyecto_de_id_1_con_un_usuario_que_lo_faveo_id_1_al_hacer_un_delete_de_dicho_id_el_usuario_ya_no_esta_en_la_lista_de_faveados(
        test_app,
        test_database):
    """
    Dada una base de datos con un proyecto
    Cuando Delete "/projects/1/favorites" con user_id = 1
    Entonces obtengo status 201
    Y obtengo el cuerpo:
        "project_id": 1,
        "users_id": [],
    """

    session = recreate_db(test_database)
    client = test_app.test_client()
    body = {
        "name": "Colombia",
        "description": "string",
        "hashtags": "#pruebaaaa #adeu",
        "type": "Art",
        "goal": 0,
        "path": "",
        "endDate": "string",
        "location": "string",
        "image": "string",
        "lat": 80.60971,
        "lon": -74.08175
    }
    client.post(
        "/projects",
        data=json.dumps(body),
        content_type="application/json"
    )
    body = {
        "user_id": 1
    }
    client.post("/projects/1/favorites",
                data=json.dumps(body),
                content_type="application/json")
    body_delete = {
        "user_id": 1,
    }
    delete_response = client.delete("/projects/1/favorites",
                                    data=json.dumps(body_delete),
                                    content_type="application/json")

    assert delete_response is not None
    assert delete_response.status_code == 200
    user = json.loads(delete_response.data.decode())
    assert user['project_id'] == 1
    assert user["users_id"] == []
