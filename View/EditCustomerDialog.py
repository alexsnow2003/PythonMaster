import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QMessageBox, QTableWidget, QTableWidgetItem,
                             QHeaderView, QDialog, QFormLayout, QDateEdit)
from PyQt6.QtCore import Qt, QDate
from Entity.Database import *


class EditCustomerDialog(QDialog):
    def __init__(self, customer=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sửa Khách Hàng" if customer else "Thêm Khách Hàng")
        self.customer = customer
        self.init_ui()

    def init_ui(self):
        layout = QFormLayout()

        self.name_input = QLineEdit(self.customer['TenKH'] if self.customer else "")
        layout.addRow("Tên KH:", self.name_input)

        self.birthdate_input = QDateEdit()
        self.birthdate_input.setDisplayFormat("yyyy-MM-dd")
        if self.customer and self.customer['NgaySinh']:
            self.birthdate_input.setDate(QDate.fromString(self.customer['NgaySinh'], "yyyy-MM-dd"))
        layout.addRow("Ngày Sinh:", self.birthdate_input)

        self.gender_input = QLineEdit(self.customer['GioiTinh'] if self.customer else "")
        layout.addRow("Giới Tính:", self.gender_input)

        self.nationality_input = QLineEdit(self.customer['QuocTich'] if self.customer else "")
        layout.addRow("Quốc Tịch:", self.nationality_input)

        self.cccd_input = QLineEdit(self.customer['CCCD'] if self.customer else "")
        layout.addRow("CCCD:", self.cccd_input)

        self.phone_input = QLineEdit(self.customer['SDT'] if self.customer else "")
        layout.addRow("SĐT:", self.phone_input)

        self.email_input = QLineEdit(self.customer['Email'] if self.customer else "")
        layout.addRow("Email:", self.email_input)

        self.save_button = QPushButton("Lưu")
        self.save_button.clicked.connect(self.save_customer)
        layout.addRow(self.save_button)

        self.setLayout(layout)

    def save_customer(self):
        name = self.name_input.text()
        birthdate = self.birthdate_input.date().toString("yyyy-MM-dd")
        gender = self.gender_input.text()
        nationality = self.nationality_input.text()
        cccd = self.cccd_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()

        if not name or not cccd or not phone:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return

        if self.customer:
            customer_id = self.customer['MaKH']
            success = update_customer(customer_id, name, birthdate, gender, nationality, cccd, phone, email)
            if success:
                QMessageBox.information(self, "Thành công", "Sửa thông tin khách hàng thành công.")
            else:
                QMessageBox.critical(self, "Lỗi", "Sửa thông tin khách hàng thất bại.")
        else:
            customer_id = add_customer(name, birthdate, gender, nationality, cccd, phone, email)
            if customer_id:
                QMessageBox.information(self, "Thành công", "Thêm khách hàng thành công.")
            else:
                QMessageBox.critical(self, "Lỗi", "Thêm khách hàng thất bại.")

        self.accept()


class CustomerManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Customer Management")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.create_buttons()

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Tên KH", "Ngày Sinh", "Giới Tính", "Quốc Tịch", "CCCD", "SĐT", "Email"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.cellDoubleClicked.connect(self.edit_customer_dialog)  # Connect double-click to edit dialog
        self.layout.addWidget(self.table)

        self.central_widget.setLayout(self.layout)

        self.load_customers()

    def create_buttons(self):
        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton("Thêm KH")
        self.add_button.clicked.connect(self.add_customer_dialog)
        buttons_layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Sửa KH")
        self.edit_button.clicked.connect(self.edit_customer_button_clicked)  # Connect to button clicked
        buttons_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Xóa KH")
        self.delete_button.clicked.connect(self.delete_customer)
        buttons_layout.addWidget(self.delete_button)

        self.search_label = QLabel("Tìm kiếm:")
        buttons_layout.addWidget(self.search_label)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Nhập tên hoặc email")
        self.search_input.textChanged.connect(self.search_customers)
        buttons_layout.addWidget(self.search_input)

        self.layout.addLayout(buttons_layout)

    def load_customers(self):
        self.table.setRowCount(0)
        customers = fetch_all_customers()
        for row, customer in enumerate(customers):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(customer['MaKH'])))
            self.table.setItem(row, 1, QTableWidgetItem(customer['TenKH']))
            self.table.setItem(row, 2, QTableWidgetItem(
                customer['NgaySinh'].strftime('%Y-%m-%d') if customer['NgaySinh'] else ''))
            self.table.setItem(row, 3, QTableWidgetItem(customer['GioiTinh']))
            self.table.setItem(row, 4, QTableWidgetItem(customer['QuocTich']))
            self.table.setItem(row, 5, QTableWidgetItem(customer['CCCD']))
            self.table.setItem(row, 6, QTableWidgetItem(customer['SDT']))
            self.table.setItem(row, 7, QTableWidgetItem(customer['Email']))

    def add_customer_dialog(self):
        dialog = EditCustomerDialog()
        if dialog.exec():
            self.load_customers()

    def edit_customer_button_clicked(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            row = selected_rows[0].row()
            self.edit_customer_dialog(row)
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để chỉnh sửa.")

    def edit_customer_dialog(self, row):
        customer_id = int(self.table.item(row, 0).text())
        customer = fetch_customer_by_id(customer_id)
        if customer:
            dialog = EditCustomerDialog(customer, self)
            if dialog.exec():
                self.load_customers()
        else:
            QMessageBox.warning(self, "Lỗi", "Không thể tải thông tin khách hàng.")

    def delete_customer(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            confirm = QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xóa khách hàng này?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                row = selected_rows[0].row()
                customer_id = int(self.table.item(row, 0).text())
                if delete_customer(customer_id):
                    QMessageBox.information(self, "Thành công", "Xóa khách hàng thành công.")
                    self.load_customers()
                else:
                    QMessageBox.critical(self, "Lỗi", "Xóa khách hàng thất bại.")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để xóa.")

    def search_customers(self, keyword):
        if keyword:
            customers = search_customers(keyword)
            self.table.setRowCount(0)
            for row, customer in enumerate(customers):
                self.table.insertRow(row)
                self.table.setItem(row, 0, QTableWidgetItem(str(customer['MaKH'])))
                self.table.setItem(row, 1, QTableWidgetItem(customer['TenKH']))
                self.table.setItem(row, 2, QTableWidgetItem(
                    customer['NgaySinh'].strftime('%Y-%m-%d') if customer['NgaySinh'] else ''))
                self.table.setItem(row, 3, QTableWidgetItem(customer['GioiTinh']))
                self.table.setItem(row, 4, QTableWidgetItem(customer['QuocTich']))
                self.table.setItem(row, 5, QTableWidgetItem(customer['CCCD']))
                self.table.setItem(row, 6, QTableWidgetItem(customer['SDT']))
                self.table.setItem(row, 7, QTableWidgetItem(customer['Email']))
        else:
            self.load_customers()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomerManagementWindow()
    window.show()
    sys.exit(app.exec())
