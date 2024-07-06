from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QDateEdit, QDialogButtonBox, QMessageBox
from PyQt6.QtCore import QDate
import mysql.connector
from mysql.connector import Error

class BookRoomDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Đặt phòng")
        self.setLayout(QVBoxLayout())

        self.form_layout = QFormLayout()
        self.layout().addLayout(self.form_layout)

        self.ma_phong_input = QLineEdit()
        self.form_layout.addRow(QLabel("Mã phòng:"), self.ma_phong_input)

        self.ten_khach_hang_input = QLineEdit()
        self.form_layout.addRow(QLabel("Tên khách hàng:"), self.ten_khach_hang_input)

        self.ngay_dat_phong_input = QDateEdit(calendarPopup=True)
        self.ngay_dat_phong_input.setDate(QDate.currentDate())
        self.form_layout.addRow(QLabel("Ngày đặt phòng:"), self.ngay_dat_phong_input)

        self.ngay_tra_phong_input = QDateEdit(calendarPopup=True)
        self.ngay_tra_phong_input.setDate(QDate.currentDate().addDays(1))
        self.form_layout.addRow(QLabel("Ngày trả phòng:"), self.ngay_tra_phong_input)

        self.book_button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.book_button.accepted.connect(self.book_room)
        self.book_button.rejected.connect(self.reject)
        self.layout().addWidget(self.book_button)

    def book_room(self):
        ma_phong = self.ma_phong_input.text()
        ten_khach_hang = self.ten_khach_hang_input.text()
        ngay_dat_phong = self.ngay_dat_phong_input.date().toPyDate()
        ngay_tra_phong = self.ngay_tra_phong_input.date().toPyDate()

        if not ma_phong or not ten_khach_hang or ngay_tra_phong <= ngay_dat_phong:
            QMessageBox.warning(self, "Dữ liệu không hợp lệ", "Vui lòng kiểm tra lại thông tin đặt phòng.")
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
                    "SELECT TinhTrangPhong FROM Phong WHERE MaPhong = %s",
                    (ma_phong,)
                )
                result = cursor.fetchone()
                if result and result[0] == 'Trống':
                    cursor.execute(
                        "UPDATE Phong SET TinhTrangPhong = 'Đã đặt', NgayDatPhong = %s, NgayTraPhong = %s, TenKhachHang = %s WHERE MaPhong = %s",
                        (ngay_dat_phong, ngay_tra_phong, ten_khach_hang, ma_phong)
                    )
                    connection.commit()
                    QMessageBox.information(self, "Thành công", "Đặt phòng thành công.")
                    self.accept()
                else:
                    QMessageBox.warning(self, "Lỗi", "Phòng đã được đặt hoặc không tồn tại.")
                cursor.close()
        except Error as e:
            print(f"Error booking room: {e}")
            QMessageBox.critical(self, "Lỗi", "Có lỗi xảy ra khi đặt phòng.")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
