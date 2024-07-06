from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QDialogButtonBox, QMessageBox
import mysql.connector
from mysql.connector import Error

class PaymentDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Thanh toán")
        self.setLayout(QVBoxLayout())

        self.form_layout = QFormLayout()
        self.layout().addLayout(self.form_layout)

        self.ma_phong_input = QLineEdit()
        self.form_layout.addRow(QLabel("Mã phòng:"), self.ma_phong_input)

        self.payment_button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.payment_button.accepted.connect(self.process_payment)
        self.payment_button.rejected.connect(self.reject)
        self.layout().addWidget(self.payment_button)

    def process_payment(self):
        ma_phong = self.ma_phong_input.text()

        if not ma_phong:
            QMessageBox.warning(self, "Dữ liệu không hợp lệ", "Vui lòng nhập mã phòng.")
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
                    "SELECT TinhTrangPhong, Gia FROM Phong INNER JOIN LoaiPhong ON Phong.MaLP = LoaiPhong.MaLP WHERE Phong.MaPhong = %s",
                    (ma_phong,)
                )
                result = cursor.fetchone()
                if result and result[0] == 'Đã đặt':
                    gia = result[1]
                    QMessageBox.information(self, "Thanh toán", f"Thanh toán thành công! Số tiền cần thanh toán là {gia} VND.")
                    cursor.execute(
                        "UPDATE Phong SET TinhTrangPhong = 'Trống', NgayDatPhong = NULL, NgayTraPhong = NULL, TenKhachHang = NULL WHERE MaPhong = %s",
                        (ma_phong,)
                    )
                    connection.commit()
                    self.accept()
                else:
                    QMessageBox.warning(self, "Lỗi", "Phòng không có đặt phòng hoặc không tồn tại.")
                cursor.close()
        except Error as e:
            print(f"Error processing payment: {e}")
            QMessageBox.critical(self, "Lỗi", "Có lỗi xảy ra khi thanh toán.")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()
