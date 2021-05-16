from App import db
from App.BDD.projects_entry import ProjectsEntry

class Projects:

    def add_project(self, project_name):
        db.session.add(ProjectsEntry(name=project_name))
        db.session.commit()

    @staticmethod
    def get_projects():
        return [i.serialize for i in ProjectsEntry.query.all()]

    @staticmethod
    def get_project_by_id(project_id):
        project = ProjectsEntry.query.get(project_id)
        if not project:
            return None
        return project.serialize