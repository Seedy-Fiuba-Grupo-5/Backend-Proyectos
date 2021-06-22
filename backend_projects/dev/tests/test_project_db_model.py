from prod.db_models.project_db_model import ProjectDBModel
from dev.aux_test import recreate_db


def test_delete_element_from_db(test_app, test_database):
    session = recreate_db(test_database)
    session.add(ProjectDBModel.create("hola",
                                      'a description',
                                      '#someHashtags',
                                      'a type',
                                      111,
                                      '2022/06/07',
                                      'a location'))
    session.commit()
    associated_id = ProjectDBModel.query.filter_by(name="hola")
    assert associated_id.count() == 1
    ProjectDBModel.delete(1)
    associated_id = ProjectDBModel.query.filter_by(name="hola")
    assert associated_id.count() == 0
