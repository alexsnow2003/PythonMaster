import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Thay bằng username của bạn
            password='phuc123'  # Thay bằng password của bạn
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
            print("Cơ sở dữ liệu 'test_db' đã được tạo hoặc đã tồn tại.")

    except Error as e:
        print("Lỗi khi tạo cơ sở dữ liệu", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def create_table_and_insert_data():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Thay bằng username của bạn
            password='phuc123',  # Thay bằng password của bạn
            database='test_db'  # Tên cơ sở dữ liệu đã tạo
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Tạo bảng DichVu
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS DichVu (
                    MaDV INT PRIMARY KEY AUTO_INCREMENT,
                    TenDV VARCHAR(255) NOT NULL,
                    DonGia DECIMAL(10, 2) NOT NULL,
                    Dvt VARCHAR(50) NOT NULL,
                    MoTa VARCHAR(200) NOT NULL
                )
            """)

            # Chèn dữ liệu mẫu vào bảng DichVu
            cursor.execute("""
                INSERT INTO DichVu (MaDV, TenDV, DonGia, Dvt, MoTa) VALUES
                    ('01', 'Dịch vụ vệ sinh', 150000, 'Lần', 'Dọn dẹp phòng khách đang sử dụng' ),
                    ('02', 'Dịch vụ bảo dưỡng máy tính', 300000, 'Lần', 'Sửa chữa,vệ sinh'),
                    ('03', 'Dịch vụ sửa chữa điện tử', 250000, 'Lần', 'Sửa chữa, thay thế'),
                    ('04', 'Dịch vụ in ấn', 50000, 'Trang', 'in màu')
            """)

            connection.commit()
            print("Bảng DichVu và dữ liệu mẫu đã được tạo và chèn thành công.")

    except Error as e:
        print("Lỗi khi tạo bảng hoặc chèn dữ liệu", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def display_data():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Thay bằng username của bạn
            password='phuc123',  # Thay bằng password của bạn
            database='test_db'  # Tên cơ sở dữ liệu đã tạo
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM DichVu")
            rows = cursor.fetchall()

            print("Dữ liệu trong bảng DichVu:")
            for row in rows:
                print(row)

    except Error as e:
        print("Lỗi khi hiển thị dữ liệu", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == "__main__":
    create_database()
    create_table_and_insert_data()
    display_data()