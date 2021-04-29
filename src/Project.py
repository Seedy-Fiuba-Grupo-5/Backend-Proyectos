class Projects:

    def __init__(self):
        self.projects = []

    def add_project(self, project_name):
        self.projects.append(project_name)


class Project:
    def __init__(self, name):
        self.name = name