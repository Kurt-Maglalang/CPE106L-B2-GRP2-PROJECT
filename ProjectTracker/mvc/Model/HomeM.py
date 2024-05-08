from flet_mvc import FletModel
import sqlite3 as sq

# Model
class HomeModel(FletModel):
    def __init__(self):
        # Connect to SQLite DB
        self.connection = sq.connect('ProjectTracker_UserData.db')
        self.cursor = self.connection.cursor()       
        
    @staticmethod
    def fetch_user_projects(user_id):
        """
        Fetches projects associated with user_id
        
        Parameters: user_ID
        Returns: List of projects
        """
        
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM project WHERE user_id = ?", (user_id,))
            projects = cursor.fetchall()
            return projects
        except sq.Error as error:
            print("Error fetching user projects:", error)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def fetch_project_tasks(project_id):
        """
        Fetches tasks associated with project_id

        Parameters: project_id
        Returns: List of tasks
        """
        
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM task WHERE project_id = ?", (project_id,))
            tasks = cursor.fetchall()
            return tasks
        except sq.Error as error:
            print("Error fetching project tasks:", error)
        finally:
            if connection:
                connection.close()