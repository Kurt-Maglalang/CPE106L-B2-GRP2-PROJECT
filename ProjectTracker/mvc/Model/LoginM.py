from flet_mvc import FletModel
import sqlite3 as sq

# Model
class LoginModel(FletModel):
    def __init__(self):
        # Connect to SQLite DB
        self.connection = sq.connect('ProjectTracker_UserData.db')
        self.cursor = self.connection.cursor()        

    @staticmethod
    def authenticate_user(username, password):
        """
        Checks if user is valid; i.e. is in db
        
        Parameters: username, password
        Returns: True if successful, otherwise False
        """
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()
            return user is not None
        except sq.Error as error:
            print("Error authenticating user:", error)
            return False
        finally:
            if connection:
                connection.close()
        