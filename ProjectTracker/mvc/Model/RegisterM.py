from flet_mvc import FletModel
import sqlite3 as sq

# Model
class RegisterModel(FletModel):
    def __init__(self):
        self.connection = sq.connect('ProjectTracker_UserData.db')
        self.cursor = self.connection.cursor()
        
    @staticmethod
    def create_user(username, password):
        """
        Creates a new user in the db
        
        Parameters: username, password
        returns: n/a
        """
        try:
            connection = sq.connect('ProjectTracker_UserData.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
            connection.commit()
            print("User created successfully")
        except sq.Error as error:
            print("Error creating user:", error)
        finally:
            if connection:
                connection.close()