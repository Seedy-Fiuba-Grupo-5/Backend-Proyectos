from prod.db_models.favorites_db_model import FavoritesProjectDBModel
from dev.aux_test import recreate_db


def test_favoritesdbmodel_get_favorites_projects_of_project_id_devuelve_lista_vacia_cuando_no_se_ha_agregado_a_favoritos(
        test_app,
        test_database):
    """
    Dada una base de datos vacia
    Cuando invoco get_favorites_of_project_id(<id project>)
    Obtengo:
        []
    """
    session = recreate_db(test_database)
    id_project_list = FavoritesProjectDBModel.get_favorites_of_project_id(11)
    assert len(id_project_list) == 0


def test_favoritesdbmodel_get_projects_of_user_id_devuelve_lista_de_ids_de_usuarios_que_han_fav_el_proyecto(
        test_app,
        test_database):
    """
    Dada una base de datos
    Tras invocar a add_project_to_favorites_of_user_id(1, 19)
    Cuando invoco get_favorites_of_project_id(<id proyecto>)
    Obtengo:
        [1]
    """
    session = recreate_db(test_database)
    user_id = 1
    project_id = 19
    id_projects_list = FavoritesProjectDBModel.add_project_to_favorites_of_user_id(
        user_id, project_id)
    assert len(id_projects_list) == 1
    assert id_projects_list[0] == user_id
    id_projects_list = FavoritesProjectDBModel.get_favorites_of_project_id(
        project_id)
    assert len(id_projects_list) == 1
    assert id_projects_list[0] == user_id
