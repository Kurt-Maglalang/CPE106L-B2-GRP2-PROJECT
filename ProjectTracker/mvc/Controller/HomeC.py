from flet_mvc import FletController
from mvc.Model.HomeM import HomeModel
from mvc.View.HomeV import HomeView

class HomeController(FletController):
    def __init__(self):
        self.model = HomeModel()
        self.view = HomeView(self)
    
    def main(user_id):
        from mvc.Model.HomeM import HomeModel as HomeM
        projects = HomeM.fetch_user_projects(user_id)
        username = HomeM.get_username(user_id)
        HomeM.view.main(HomeM.view.page, user_id, username, projects)

    
    def fetch_project_tasks(project_id):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.fetch_project_tasks(project_id)

    def fetch_task_state(task_id):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.fetch_task_state(task_id)

    def get_username(self, user_id):
        return self.fetch_user_username(user_id)

    def create_project(user_id, project_name):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.create_project(user_id, project_name)
    
    def create_task(project_id, task_name):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.create_task(project_id, task_name)

    def get_project_id_by_name(project_name):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.get_project_id_by_name(project_name)
    
    def get_task_id_by_name(task_name):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.get_task_id_by_name(task_name)

    def add_task_to_project(self, project_id, task_name):
        return self.model.add_task_to_project(project_id, task_name)

    def toggle_task_status(task_id):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.toggle_task_status(task_id)

    def fetch_user_projects(user_id):
        from mvc.Model.HomeM import HomeModel as HomeM
        return HomeM.fetch_user_projects(user_id) 