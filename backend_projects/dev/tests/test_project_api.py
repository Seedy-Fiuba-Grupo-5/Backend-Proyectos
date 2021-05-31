import json
from prod.db_models.project_db_model import ProjectDBModel

def test_db_with_only_project_id_1_name_Project_X_GET_id_1_should_return_just_that(test_app, test_database):
    session = test_database.session
    session.remove()
    test_database.drop_all()
    test_database.create_all()
    session.add(ProjectDBModel(name='Project X', description='description', hashtags='#prueba',
        type='tipo',goal=1000,endDate='12/02/2021', location= 'Buenos Aires'))
    session.commit()
    client = test_app.test_client()
    response = client.get("/projects/1")
    assert response.status_code == 200
    project = json.loads(response.data.decode())
    assert project['name'] == 'Project X'
