class Project:
    def __init__(self, name):
        self.name = name
        self.isActive = False

    def get_name(self):
        return self.name

    def activate_project(self):
        self.isActive = True
