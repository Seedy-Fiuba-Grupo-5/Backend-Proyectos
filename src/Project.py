class Projects:

    def __init__(self):
        self.projects = {}
        self.id = 0

    def add_project(self, project_name):
        self.projects[self.id] = project_name
        self.id = self.id + 1


class Project:
    def __init__(self, name):
        self.name = name