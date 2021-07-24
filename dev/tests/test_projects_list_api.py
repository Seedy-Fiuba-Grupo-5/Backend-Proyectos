import json
from dev.aux_test import recreate_db
from prod.db_models.project_db_model import ProjectDBModel


def test_db_empty_POST_projects_name_test_project_should_return_that_with_id_1(test_app, test_database):
    session = recreate_db(test_database)
    project = {'name': 'test project', 'description': 'description', 'hashtags': '#prueba',
               'type': 'Comics', 'goal': 1000, 'endDate': '12/02/2021', 'location': 'Buenos Aires',
               'image': 'www.an_image_url.com', 'path': 'a', 'lat': 50, "lon": 20.5}
    client = test_app.test_client()
    response = client.post("/projects", json=project)
    assert response.status_code == 201
    project = json.loads(response.data.decode())
    assert project['id'] == 1
    assert project['name'] == 'test project'
    assert project['image'] == 'www.an_image_url.com'


def test_db_empty_POST_projects_name_test_project_GET_projects_should_return_just_that(test_app, test_database):
    session = test_database.session
    session.remove()
    test_database.drop_all()
    test_database.create_all()
    project = {'name': 'test project', 'description': 'description', 'hashtags': '#prueba',
               'type': 'Comics', 'goal': 1000, 'endDate': '12/02/2021', 'location': 'Buenos Aires',
               'image': 'www.an_image_url.com', 'path': 'a', 'lat': 50, "lon": 20.5}
    client = test_app.test_client()
    client.post("/projects", json=project)
    response = client.get("/projects")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert len(data) == 1
    project = data[0]
    assert project['name'] == 'test project'


def test_get_project_con_filtro_devuelve_solo_los_con_ese_tipo(
        test_app,
        test_database):
    """
    Dada una base de datos con dos proyectos con dos tipos distintos.
    Cuando GET 'projects' con filtro
    Entonces obtengo un solo proyecto
    """
    session = recreate_db(test_database)
    client = test_app.test_client()
    session.add(ProjectDBModel(name='Project X', description='description', hashtags='#prueba',
                               type='art', goal=1000, endDate='12/02/2021', location='Buenos Aires',
                               image='www.an_image_url.com',
                               createdOn='12/02/2021', path='a', lat=50, lon=20.5))
    session.add(ProjectDBModel(name='Project X', description='description', hashtags='#prueba',
                               type='comics', goal=1000, endDate='12/02/2021', location='Buenos Aires',
                               image='www.an_image_url.com',
                               createdOn='12/02/2021', path='a', lat=50, lon=20.5))
    response = client.get("/projects?type")
    projects = json.loads(response.data.decode())
    assert len(projects) == 2
    response = client.get("/projects?type=Comics")
    projects = json.loads(response.data.decode())
    assert len(projects) == 1 and projects[0]["type"] == "Comics"


def test_post_project_con_tipo_no_valido(
        test_app,
        test_database):
    """
    Dada una base de datos con dos proyectos con dos tipos distintos.
    Cuando POST 'projects' con tipo invalido
    Entonces obtengo status code 400
    Con cuerpo:
        "status": 'The type selected in not a valid one'
    """
    session = recreate_db(test_database)
    client = test_app.test_client()
    project = {'name': 'a name', 'description': 'a description', 'hashtags': '#someHashtags',
               'type': 'tipo invalido', 'goal': 111, 'endDate': '2022/06/07', 'location': 'a location',
               'image': 'www.an-image-url.com', 'path': 'a', 'lat': 50, "lon": 20.5}
    response = client.post("/projects", json=project)
    assert response.status_code == 400
    data = json.loads(response.data.decode())
    assert data['status'] == 'The type selected in not a valid one'
