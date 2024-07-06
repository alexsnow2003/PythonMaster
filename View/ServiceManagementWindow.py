import mysql.connector
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, \
    QMessageBox, QFormLayout, QLineEdit, QLabel, QComboBox
from PyQt6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout


class ServiceManagementWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý dịch vụ")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.service_table = QTableWidget()
        self.service_table.setColumnCount(4)
        self.service_table.setHorizontalHeaderLabels(['Mã DV', 'Tên dịch vụ', 'Giá', 'Loại'])
        self.service_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.layout.addWidget(self.service_table)

        self.load_services()

        self.button_layout = QVBoxLayout()
        self.add_service_button = QPushButton("Thêm dịch vụ")
        self.add_service_button.clicked.connect(self.add_service)
        self.button_layout.addWidget(self.add_service_button)

        self.update_service_button = QPushButton("Sửa dịch vụ")
        self.update_service_button.clicked.connect(self.update_service)
        self.button_layout.addWidget(self.update_service_button)

        self.delete_service_button = QPushButton("Xóa dịch vụ")
        self.delete_service_button.clicked.connect(self.delete_service)
        self.button_layout.addWidget(self.delete_service_button)

        self.view_invoice_button = QPushButton("Xem hóa đơn dịch vụ")
        self.view_invoice_button.clicked.connect(self.view_invoice)
        self.button_layout.addWidget(self.view_invoice_button)

        self.print_report_button = QPushButton("In báo cáo dịch vụ")
        self.print_report_button.clicked.connect(self.print_report)
        self.button_layout.addWidget(self.print_report_button)

        self.layout.addLayout(self.button_layout)

    def load_services(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                user='root',
                password='123456',  # Thay bằng mật khẩu của bạn
                database='QLKS'
            )
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM DICHVU")
            services = cursor.fetchall()

            self.service_table.setRowCount(len(services))
            for row, service in enumerate(services):
                self.service_table.setItem(row, 0, QTableWidgetItem(service['MaDV']))
                self.service_table.setItem(row, 1, QTableWidgetItem(service['TenDV']))
                self.service_table.setItem(row, 2, QTableWidgetItem(f"{service['Gia']:.0f} VND"))
                self.service_table.setItem(row, 3, QTableWidgetItem(service['Loai']))

            connection.close()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def add_service(self):
        dialog = ServiceDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_services()

    def update_service(self):
        current_row = self.service_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn dịch vụ để sửa.")
            return

        ma_dv = self.service_table.item(current_row, 0).text()
        dialog = ServiceDialog(ma_dv=ma_dv)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_services()

    def delete_service(self):
        current_row = self.service_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Warning", "Vui lòng chọn dịch vụ để xóa.")
            return

        ma_dv = self.service_table.item(current_row, 0).text()
        reply = QMessageBox.question(
            self, 'Xác nhận xóa dịch vụ',
            f'Bạn có chắc chắn muốn xóa dịch vụ với mã {ma_dv} không?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    port=3307,
                    user='root',
                    password='123456',  # Thay bằng mật khẩu của bạn
                    database='QLKS'
                )
                cursor = connection.cursor()
                cursor.execute(f"DELETE FROM DICHVU WHERE MaDV = '{ma_dv}'")
                connection.commit()
                connection.close()
                self.load_services()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def view_invoice(self):
        # Implement view invoice functionality
        QMessageBox.information(self, "Xem hóa đơn", "View Invoice button clicked.")

    def print_report(self):
        # Implement print report functionality
        QMessageBox.information(self, "In báo cáo", "Print Report button clicked.")

class ServiceDialog(QDialog):
    def __init__(self, ma_dv=None):
        super().__init__()
        self.setWindowTitle("Thêm/Sửa dịch vụ")
        self.setGeometry(100, 100, 400, 300)

        self.form_layout = QFormLayout()
        self.setLayout(self.form_layout)

        self.ten_dv_input = QLineEdit()
        self.form_layout.addRow(QLabel("Tên dịch vụ:"), self.ten_dv_input)

        self.gia_input = QLineEdit()
        self.form_layout.addRow(QLabel("Giá (VND):"), self.gia_input)

        self.loai_combo = QComboBox()
        self.loai_combo.addItems(['Nhà hàng', 'Giặt ủi', 'Mát-xa', 'Khác'])
        self.form_layout.addRow(QLabel("Loại dịch vụ:"), self.loai_combo)

        if ma_dv:
            self.ma_dv = ma_dv
            self.load_service_details()
        else:
            self.ma_dv = None
            self.setWindowTitle("Thêm dịch vụ")

        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Lưu")
        self.save_button.clicked.connect(self.save_service)
        self.button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton("Hủy")
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout.addWidget(self.cancel_button)

        self.form_layout.addRow(self.button_layout)

    def load_service_details(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                user='root',
                password='123456',  # Thay bằng mật khẩu của bạn
                database='QLKS'
            )
            cursor = connection.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM DICHVU WHERE MaDV = '{self.ma_dv}'")
            service = cursor.fetchone()
            self.ten_dv_input.setText(service['TenDV'])
            self.gia_input.setText(f"{service['Gia']:.0f}")
            self.loai_combo.setCurrentText(service['Loai'])
            connection.close()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def save_service(self):
        ten_dv = self.ten_dv_input.text()
        gia = self.gia_input.text()
        loai = self.loai_combo.currentText()

        if not ten_dv or not gia or not loai:
            QMessageBox.warning(self, "Warning", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                user='root',
                password='123456',  # Thay bằng mật khẩu của bạn
                database='QLKS'
            )
            cursor = connection.cursor()

            if self.ma_dv:
                cursor.execute(f"""
                    UPDATE DICHVU
                    SET TenDV = %s, Gia = %s, Loai = %s
                    WHERE MaDV = %s
                """, (ten_dv, gia, loai, self.ma_dv))
            else:
                cursor.execute(f"""
                    INSERT INTO DICHVU (TenDV, Gia, Loai)
                    VALUES (%s, %s, %s)
                """, (ten_dv, gia, loai))

            connection.commit()
            connection.close()
            self.accept()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")
