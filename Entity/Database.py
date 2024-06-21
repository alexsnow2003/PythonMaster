import mysql.connector
from mysql.connector import Error

def create_connection():
    """ Create a connection to MySQL database. """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3307,
            database='QLKS',  # Make sure this matches your actual database name
            user='root',      # Adjust username as necessary
            password='123456'  # Adjust password as necessary
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
    """ Retrieve all customers from the database. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM KhachHang")
            customers = cursor.fetchall()
            print("Fetched customers:", customers)  # Add debug print
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

def add_customer(name, email, phone, address):
    """ Add a new customer to the database. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO KhachHang (TenKH, Email, SDT, DiaChi) VALUES (%s, %s, %s, %s)",
                           (name, email, phone, address))
            connection.commit()
            return cursor.lastrowid  # Return the ID of the newly inserted customer
        except Error as e:
            print(f"Error adding customer: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    return None

def update_customer(customer_id, name, email, phone, address):
    """ Update an existing customer in the database. """
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE KhachHang SET TenKH = %s, Email = %s, SDT = %s, DiaChi = %s WHERE MaKH = %s",
                           (name, email, phone, address, customer_id))
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

# Test the functions if needed
if __name__ == "__main__":
    print(fetch_all_customers())
    print(fetch_customer_by_id(1))
    # Add more test cases as needed
