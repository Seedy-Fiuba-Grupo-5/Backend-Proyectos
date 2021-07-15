from prod.db_models.project_db_model import ProjectDBModel
from dev.aux_test import recreate_db


def test_delete_element_from_db(test_app, test_database):
    session = recreate_db(test_database)
    session.add(ProjectDBModel.create("hola",
                                      'a description',
                                      '#someHashtags',
                                      'Comics',
                                      111,
                                      '2022/06/07',
                                      'a location',
                                      'www.an-image.com'))
    session.commit()
    associated_id = ProjectDBModel.query.filter_by(name="hola")
    assert associated_id.count() == 1
    ProjectDBModel.delete(1)
    associated_id = ProjectDBModel.query.filter_by(name="hola")
    assert associated_id.count() == 0


def test_add_seer(test_app, test_database):
    session = recreate_db(test_database)
    session.add(ProjectDBModel.create("hola",
                                      'a description',
                                      '#someHashtags',
                                      'Comics',
                                      111,
                                      '2022/06/07',
                                      'a location',
                                      'www.an-image.com'))
    session.commit()
    user_model = ProjectDBModel.query.filter_by(id=1).first()
    assert user_model.seer == ""
    ProjectDBModel.add_seer("Brian",
                            1)
    user_model = ProjectDBModel.query.filter_by(id=1).first()
    assert user_model.seer == "Brian"

