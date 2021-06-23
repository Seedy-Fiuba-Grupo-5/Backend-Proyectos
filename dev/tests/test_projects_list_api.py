import json
from dev.aux_test import recreate_db


def test_db_empty_POST_projects_name_test_project_should_return_that_with_id_1(test_app, test_database):
    session = recreate_db(test_database)
    project = {'name': 'test project', 'description': 'description', 'hashtags': '#prueba',
               'type': 'Comics', 'goal': 1000, 'endDate': '12/02/2021', 'location': 'Buenos Aires',
               'image': 'www.an_image_url.com'}
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
               'image': 'www.an_image_url.com'}
    client = test_app.test_client()
    client.post("/projects", json=project)
    response = client.get("/projects")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert len(data) == 1
    project = data[0]
    assert project['name'] == 'test project'
