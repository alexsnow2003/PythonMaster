import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection_status = None
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                database='QLKS',
                user='root',
                password='123456'
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                self.connection_status = "Successfully connected to the database."
        except Error as e:
            self.connection_status = f"Error: {e}"

    def register_user(self, username, password, first_name, last_name, role_id):
        try:
            self.cursor.execute(
                "INSERT INTO User (username, password, first_name, last_name, role_id) VALUES (%s, %s, %s, %s, %s)",
                (username, password, first_name, last_name, role_id))
            self.connection.commit()
            return True  # Return True when registration is successful
        except Error as e:
            print(f"Error: {e}")
            return False  # Return False when registration fails

    def login_user(self, username, password):
        try:
            self.cursor.execute("SELECT r.role_name FROM User u JOIN Role r ON u.role_id = r.role_id WHERE u.username = %s AND u.password = %s", (username, password))
            result = self.cursor.fetchone()
            return result[0] if result else None
        except Error as e:
            print(f"Error: {e}")
            return None

    def __del__(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
