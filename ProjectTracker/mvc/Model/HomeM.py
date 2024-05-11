import stat
from flet_mvc import FletModel
import sqlite3 as sq

# Model
class HomeModel(FletModel):
    def __init__(self):
        # Connect to SQLite DB
        self.connection = sq.connect('ProjectTracker_UserData.db')
        self.cursor = self.connection.cursor()       
        
    def fetch_user_username(self, user_id):
        """
        Fetches username associated with user_id
        
        Parameters: user_id
        Returns: Username if found, else None
        """
        try:
            self.cursor.execute("SELECT username FROM user WHERE id = ?", (user_id,))
            username = self.cursor.fetchone()
            if username:
                return username[0]
            else:
                return None
        except sq.Error as error:
            print("Error fetching user username:", error)
            return None
        
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
            cursor.execute("SELECT project_name FROM project WHERE user_id = ?", (user_id,))
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
        Fetches projects associated with user_id
    
        Parameters:
            user_id: The ID of the user
    
        Returns:
            List of tuples containing project details
        """
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("SELECT task_name FROM task WHERE project_id = ?", (project_id,))
            projects = cursor.fetchall()
            return projects
        except sq.Error as error:
            print("Error fetching user projects:", error)
        finally:
            if connection:
                connection.close()
                
    @staticmethod
    def fetch_task_state(task_id):
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("SELECT is_done FROM task WHERE task_id = ?", (task_id,))
            projects = cursor.fetchall()
            return projects
        except sq.Error as error:
            print("Error fetching task states:", error)
        finally:
            if connection:
                connection.close()

    @staticmethod
    def get_project_id_by_name(project_name):
        """
        Retrieves the project ID by searching for the project name in the database.
        
        Parameters:
            project_name (str): The name of the project to search for.
        
        Returns:
            int: The ID of the project if found, None otherwise.
        """
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            # Search for the project ID using the project name
            cursor.execute("SELECT project_id FROM project WHERE project_name = ?", (project_name,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the project ID
            else:
                return None  # Project not found
        except sq.Error as error:
            print("Error fetching project ID by name:", error)
        finally:
            if connection:
                connection.close()
                
    @staticmethod
    def get_task_id_by_name(task_name):
        """
        Retrieves the task ID by searching for the task name in the database.
        
        Parameters:
            task_name (str): The name of the project to search for.
        
        Returns:
            int: The ID of the task if found, None otherwise.
        """
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            # Search for the task ID using the project name
            cursor.execute("SELECT task_id FROM task WHERE task_name = ?", (task_name,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the task ID
            else:
                return None  # Task not found
        except sq.Error as error:
            print("Error fetching task ID by name:", error)
        finally:
            if connection:
                connection.close()

                
    @staticmethod
    def create_project(user_id, project_name):
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO project (user_id, project_name) VALUES (?, ?)", (user_id, project_name))
            connection.commit()
            return True
        except sq.Error as error:
            print("Error creating project:", error)
            return False
        
    @staticmethod
    def create_task(project_id, task_name):
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO task (project_id, task_name, is_done) VALUES (?, ?, ?)", (project_id, task_name, 0))
            connection.commit()
            return True
        except sq.Error as error:
            print("Error creating task:", error)
            return False

    @staticmethod
    def add_task_to_project(self, project_id, task_name):
        try:
            self.cursor.execute("INSERT INTO task (project_id, task_name, is_done) VALUES (?, ?, 0)", (project_id, task_name))
            self.connection.commit()
            return True
        except sq.Error as error:
            print("Error adding task to project:", error)
            return False

    @staticmethod
    def toggle_task_status(task_id):
        try:
            print("Toggling task with ID:", task_id)
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            # Print the SQL query before execution
            sql_query = "UPDATE task SET is_done = CASE is_done WHEN 1 THEN 0 ELSE 1 END WHERE task_id = ?"
            print("Executing SQL query:", sql_query, "with task_id =", task_id)
            cursor.execute(sql_query, (task_id,))
            connection.commit()
            return True
        except sq.Error as error:
            print("Error toggling task status:", error)
            return False
        finally:
            if connection:
                connection.close()

