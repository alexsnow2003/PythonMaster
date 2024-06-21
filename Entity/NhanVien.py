import mysql.connector
from datetime import date

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",  # Thay đổi nếu cần
        port=3307,
        user="root",       # Thay đổi nếu cần
        password="123456",  # Thay đổi nếu cần
        database="QLKS"
    )
    return connection

def fetch_all_employees():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM NhanVien")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees

def fetch_employee_by_id(employee_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM NhanVien WHERE MaNV = %s", (employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee

def add_employee(name, birthdate, gender, nationality, cccd, address, phone, position, salary, department_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO NhanVien (TenNV, NgaySinh, GioiTinh, QuocTich, CCCD, DiaChi, SDT, ChucVu, Luong, MaPB)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, birthdate, gender, nationality, cccd, address, phone, position, salary, department_id))
        connection.commit()
        new_employee_id = cursor.lastrowid  # Get the ID of the last inserted row
        cursor.close()
        connection.close()
        return new_employee_id
    except Exception as e:
        print(f"Error adding employee: {e}")
        return None



def update_employee(employee_id, name, birthdate, gender, nationality, cccd, address, phone, position, salary, department_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        UPDATE NhanVien
        SET TenNV = %s, NgaySinh = %s, GioiTinh = %s, QuocTich = %s, CCCD = %s, DiaChi = %s, SDT = %s, ChucVu = %s, Luong = %s, MaPB = %s
        WHERE MaNV = %s
    """
    cursor.execute(query, (name, birthdate, gender, nationality, cccd, address, phone, position, salary, department_id, employee_id))
    connection.commit()
    cursor.close()
    connection.close()
    return cursor.rowcount > 0

def delete_employee(employee_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM NhanVien WHERE MaNV = %s", (employee_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return cursor.rowcount > 0

def search_employees(keyword):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT * FROM NhanVien
        WHERE TenNV LIKE %s OR CCCD LIKE %s OR SDT LIKE %s
    """
    like_keyword = f"%{keyword}%"
    cursor.execute(query, (like_keyword, like_keyword, like_keyword))
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees


