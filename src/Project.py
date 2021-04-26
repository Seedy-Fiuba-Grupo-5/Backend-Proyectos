class Project:
    def __init__(self, name):
        self.name = name
        self.isActive = False

    def activate_project(self):
        self.isActive = True
