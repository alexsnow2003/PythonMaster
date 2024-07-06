from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QDialogButtonBox, QComboBox, QMessageBox
import mysql.connector
from mysql.connector import Error

class AddRoomDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Thêm phòng")
        self.setLayout(QVBoxLayout())

        self.form_layout = QFormLayout()
        self.layout().addLayout(self.form_layout)

        self.ma_phong_input = QLineEdit()
        self.form_layout.addRow(QLabel("Mã phòng:"), self.ma_phong_input)

        self.ma_lp_input = QComboBox()
        self.form_layout.addRow(QLabel("Loại phòng:"), self.ma_lp_input)
        self.load_room_types()

        self.add_button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.add_button.accepted.connect(self.add_room)
        self.add_button.rejected.connect(self.reject)
        self.layout().addWidget(self.add_button)

    def load_room_types(self):
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
                cursor.execute("SELECT MaLP, TenLP FROM LoaiPhong")
                room_types = cursor.fetchall()
                for room_type in room_types:
                    self.ma_lp_input.addItem(room_type['TenLP'], room_type['MaLP'])
                cursor.close()
        except Error as e:
            print(f"Error loading room types: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

    def add_room(self):
        ma_phong = self.ma_phong_input.text()
        ma_lp = self.ma_lp_input.currentData()
        if not ma_phong or not ma_lp:
            QMessageBox.warning(self, "Dữ liệu không hợp lệ", "Vui lòng nhập đầy đủ thông tin phòng.")
            return
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                database='QLKS',
                user='root',
                password='123456'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO Phong (MaPhong, MaLP, TinhTrangPhong) VALUES (%s, %s, 'Trống')",
                    (ma_phong, ma_lp)
                )
                connection.commit()
                QMessageBox.information(self, "Thành công", "Thêm phòng thành công.")
                self.accept()
                cursor.close()
        except Error as e:
            print(f"Error adding room: {e}")
            QMessageBox.critical(self, "Lỗi", "Có lỗi xảy ra khi thêm phòng.")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
