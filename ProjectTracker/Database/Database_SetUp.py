import sqlite3 as sq

# Database Name: ProjectTracker_UserData.db

# TABLES: 
    # user:
        # user_id = Primary Key Integer
        # username = Unique Text
        # password = Text
    # project:
        # project_id = Primary Key Integer
        # user_id = Foreign Key Integer REFERENCING user(user_id)
        # project_name = Text
    # task:
        # task_id = Primary Key Integer
        # project_id = Foreign Key Integer REFERENCING project(project_id)
        # task_name = Text
        # is_done = Integer 

class databaseSetup:
    @staticmethod
    def create_database():
        # Connect to SQLite database (creates new file if it doesn't exist)
        connection = sq.connect('ProjectTracker_UserData.db')
        # For some REALLY odd reason, this creates the database OUTSIDE of the current directory? It places it in the repo folder
        # when is used to place it inside the correct folder? Really Odd.
        cursor = connection.cursor()

        # Create Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
        """)
        
        # Create Projects table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS project (
            project_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            project_name TEXT,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
        )
        """)

        # Create Tasks table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS task (
            task_id INTEGER PRIMARY KEY,
            project_id INTEGER,
            task_name TEXT,
            is_done INTEGER,
            FOREIGN KEY (project_id) REFERENCES project(project_id)
        )
        """)

        connection.commit()
        connection.close()
