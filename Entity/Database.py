import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Create a connection to MySQL database. """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3307,
            database='QLKS',
            user='root',  # Thay đổi nếu cần
            password='123456'  # Thay đổi nếu cần
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def close_connection(connection):
    """ Close MySQL database connection. """
    if connection:
        connection.close()

def fetch_all_customers():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM KhachHang")
            customers = cursor.fetchall()
            return customers
        except Error as e:
            print(f"Error fetching customers: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    return []

def fetch_customer_by_id(customer_id):
    """ Retrieve a customer by ID from the database. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM KhachHang WHERE MaKH = %s", (customer_id,))
            customer = cursor.fetchone()
            return customer
        except Error as e:
            print(f"Error fetching customer: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    return None

def add_customer(name, birthdate, gender, nationality, cccd, phone, email):
    """ Add a new customer to the database. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO KhachHang (TenKH, NgaySinh, GioiTinh, QuocTich, CCCD, SDT, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (name, birthdate, gender, nationality, cccd, phone, email))
            connection.commit()
            return cursor.lastrowid  # Return the ID of the newly inserted customer
        except Error as e:
            print(f"Error adding customer: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    return None

def update_customer(customer_id, name, birthdate, gender, nationality, cccd, phone, email):
    """ Update an existing customer in the database. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE KhachHang SET TenKH = %s, NgaySinh = %s, GioiTinh = %s, QuocTich = %s, CCCD = %s, SDT = %s, Email = %s WHERE MaKH = %s",
                           (name, birthdate, gender, nationality, cccd, phone, email, customer_id))
            connection.commit()
            return True
        except Error as e:
            print(f"Error updating customer: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    return False

def delete_customer(customer_id):
    """ Delete a customer from the database. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM KhachHang WHERE MaKH = %s", (customer_id,))
            connection.commit()
            return True
        except Error as e:
            print(f"Error deleting customer: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    return False

def search_customers(keyword):
    """ Search for customers in the database by name or email. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM KhachHang WHERE TenKH LIKE %s OR Email LIKE %s"
            cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
            customers = cursor.fetchall()
            return customers
        except Error as e:
            print(f"Error searching customers: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    return []
