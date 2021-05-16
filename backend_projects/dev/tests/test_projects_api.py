import json
from prod.db_models.project_db_model import ProjectDBModel

def test_db_empty_POST_projects_name_test_project_GET_projects_should_return_just_that(test_app, test_database):
    session = test_database.session
    session.remove()
    test_database.drop_all()
    test_database.create_all()
    project = {'name': 'test project'}
    client = test_app.test_client()
    client.post("/projects", json=project)
    response = client.get("/projects")
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert len(data) == 1
    project = data[0]
    assert project['name'] == 'test project'
