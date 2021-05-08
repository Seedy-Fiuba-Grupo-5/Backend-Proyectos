from App import db
from App.BDD.projects_entry import ProjectsEntry

class Projects:

    def add_project(self, project_name):
        db.session.add(
            ProjectsEntry(name=project_name))
        db.session.commit()

    def get_projects(self):
        return [i.serialize for i in ProjectsEntry.query.all()]