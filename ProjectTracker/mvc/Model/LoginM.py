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
        
    def get_user_id(self, username):
        """
        Gets the user_id based on the provided username
        
        Parameters: username
        Returns: user_id if found, else None
        """
        try:
            self.cursor.execute("SELECT user_id FROM user WHERE username = ?", (username,))
            user_id = self.cursor.fetchone()
            if user_id:
                return user_id[0]  # Return the user_id if found
            else:
                return None
        except sq.Error as error:
            print("Error fetching user_id:", error)
            return None
        finally:
            if self.connection:
                self.connection.close()