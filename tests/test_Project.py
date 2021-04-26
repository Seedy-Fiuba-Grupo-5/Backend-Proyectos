from src.Project import *


def test_get_name():
    project = Project("prueba")
    assert (project.get_name() == "prueba")
