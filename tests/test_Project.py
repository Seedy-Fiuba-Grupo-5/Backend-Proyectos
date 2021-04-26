from src.Project import *


def test_get_name():
    project = Project("prueba")
    assert (project.name == "prueba")


def test_activate_project():
    project = Project("prueba")
    project.activate_project()
    assert project.isActive


def test_deactivate_project():
    project = Project("prueba")
    project.activate_project()
    assert not project.isActive
