from flet_mvc import FletController
from mvc.Model.HomeM import HomeModel
from mvc.View.HomeV import HomeView

class HomeController(FletController):
    def __init__(self):
        self.model = HomeModel()
        self.view = HomeView(self)
    
    def main(self, user_id):
        projects = self.model.fetch_user_projects(user_id)
        username = self.model.fetch_user_username(user_id)
        self.view.main(projects, user_id, username) 
    
    def fetch_project_tasks(self, project_id):
        return self.model.fetch_project_tasks(project_id)

    def get_username(self, user_id):
        return self.fetch_user_username(user_id)
