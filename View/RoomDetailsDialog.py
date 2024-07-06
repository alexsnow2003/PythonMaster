from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
import mysql.connector
from mysql.connector import Error

class RoomDetailsDialog(QDialog):
    def __init__(self, parent, ma_phong):
        super().__init__(parent)
        self.ma_phong = ma_phong
        self.setWindowTitle("Chi tiết phòng")
        self.setLayout(QVBoxLayout())

        self.info_label = QLabel()
        self.layout().addWidget(self.info_label)

        self.close_button = QPushButton("Đóng")
        self.close_button.clicked.connect(self.accept)
        self.layout().addWidget(self.close_button)

        self.load_room_details()

    def load_room_details(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                database='QLKS',
                user='root',
                password='123456'
            )
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                cursor.execute(
                    "SELECT Phong.MaPhong, LoaiPhong.TenLP, LoaiPhong.Gia, Phong.TinhTrangPhong, Phong.NgayDatPhong, Phong.NgayTraPhong, Phong.TenKhachHang "
                    "FROM Phong INNER JOIN LoaiPhong ON Phong.MaLP = LoaiPhong.MaLP WHERE Phong.MaPhong = %s",
                    (self.ma_phong,)
                )
                room = cursor.fetchone()
                if room:
                    self.info_label.setText(
                        f"Phòng {room['MaPhong']}\n"
                        f"Loại phòng: {room['TenLP']}\n"
                        f"Giá: {room['Gia']} VND\n"
                        f"Tình trạng: {room['TinhTrangPhong']}\n"
                        f"Ngày đặt phòng: {room['NgayDatPhong']}\n"
                        f"Ngày trả phòng: {room['NgayTraPhong']}\n"
                        f"Tên khách hàng: {room['TenKhachHang']}"
                    )
                else:
                    self.info_label.setText("Không tìm thấy thông tin phòng.")
                cursor.close()
        except Error as e:
            print(f"Error loading room details: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
