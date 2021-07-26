import json
from prod.db_models.project_db_model import ProjectDBModel
from dev.aux_test import recreate_db

def test_add_rating_to_project(test_app, test_database):
    session = recreate_db(test_database)
    session.add(ProjectDBModel(name='Project Rated', description='description', hashtags='#prueba',
                               type='art', goal=1000, endDate='12/02/2021', location='Buenos Aires',
                               image='www.an_image_url.com',
                               createdOn='12/02/2021', path='a', lat=50, lon=20.5))
    session.commit()
    client = test_app.test_client()
    response = client.post("/projects/1/rate", json={"rating": 5, "id_user": 1})
    assert response.status_code == 200
    response = client.get("/projects/1")
    project = json.loads(response.data.decode())
    assert project['rating'] == 5

def test_change_rating_in_project(test_app, test_database):
    session = recreate_db(test_database)
    session.add(ProjectDBModel(name='Project Rated', description='description', hashtags='#prueba',
                               type='art', goal=1000, endDate='12/02/2021', location='Buenos Aires',
                               image='www.an_image_url.com',
                               createdOn='12/02/2021', path='a', lat=50, lon=20.5))
    session.commit()
    client = test_app.test_client()
    response = client.post("/projects/1/rate", json={"rating": 5, "id_user": 1})
    response = client.post("/projects/1/rate", json={"rating": 1, "id_user": 1})
    assert response.status_code == 200
    response = client.get("/projects/1")
    project = json.loads(response.data.decode())
    assert project['rating'] == 1

def test_add_second_rating_in_project_give_average(test_app, test_database):
    session = recreate_db(test_database)
    session.add(ProjectDBModel(name='Project Rated', description='description', hashtags='#prueba',
                               type='art', goal=1000, endDate='12/02/2021', location='Buenos Aires',
                               image='www.an_image_url.com',
                               createdOn='12/02/2021', path='a', lat=50, lon=20.5))
    session.commit()
    client = test_app.test_client()
    response = client.post("/projects/1/rate", json={"rating": 5, "id_user": 1})
    response = client.post("/projects/1/rate", json={"rating": 1, "id_user": 2})
    assert response.status_code == 200
    response = client.get("/projects/1")
    project = json.loads(response.data.decode())
    assert project['rating'] == 3

