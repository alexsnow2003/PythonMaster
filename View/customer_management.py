import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QFormLayout, QDateEdit
from PyQt6.QtCore import Qt, QDate
from Entity.Database import *


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
        self.edit_button.clicked.connect(self.edit_customer_dialog)
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
        dialog = QDialog(self)
        dialog.setWindowTitle("Thêm Khách Hàng")
        dialog.setStyleSheet("""
            background-color: #f0f0f0;
            font-size: 14px;
            padding: 20px;
            border: 2px solid #ccc;
            border-radius: 10px;
        """)

        layout = QVBoxLayout(dialog)

        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.apply_style(self.name_input)
        form_layout.addRow("Tên KH:", self.name_input)

        self.birthdate_input = QLineEdit()
        self.birthdate_input.setPlaceholderText("DD/MM/YYYY or DD-MM-YYYY")
        self.apply_style(self.birthdate_input)
        form_layout.addRow("Ngày Sinh:", self.birthdate_input)

        self.gender_input = QLineEdit()
        self.apply_style(self.gender_input)
        form_layout.addRow("Giới Tính:", self.gender_input)

        self.nationality_input = QLineEdit()
        self.apply_style(self.nationality_input)
        form_layout.addRow("Quốc Tịch:", self.nationality_input)

        self.cccd_input = QLineEdit()
        self.apply_style(self.cccd_input)
        form_layout.addRow("CCCD:", self.cccd_input)

        self.phone_input = QLineEdit()
        self.apply_style(self.phone_input)
        form_layout.addRow("SĐT:", self.phone_input)

        self.email_input = QLineEdit()
        self.apply_style(self.email_input)
        form_layout.addRow("Email:", self.email_input)

        save_button = QPushButton("Lưu")
        save_button.clicked.connect(lambda: self.save_customer(dialog))
        self.apply_style(save_button)
        form_layout.addRow(save_button)

        layout.addLayout(form_layout)

        dialog.exec()

    def save_customer(self, dialog):
        name = self.name_input.text()
        birthdate = self.birthdate_input.text()  # Getting text directly
        gender = self.gender_input.text()
        nationality = self.nationality_input.text()
        cccd = self.cccd_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()

        if name and cccd and phone:
            customer_id = add_customer(name, birthdate, gender, nationality, cccd, phone, email)
            if customer_id:
                QMessageBox.information(self, "Thành công", "Thêm khách hàng thành công.")
                self.load_customers()
                dialog.accept()
            else:
                QMessageBox.critical(self, "Lỗi", "Thêm khách hàng thất bại.")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")

    def edit_customer_dialog(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để chỉnh sửa.")
            return

        row = selected_rows[0].row()
        customer_id_item = self.table.item(row, 0)
        if customer_id_item is None:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy thông tin khách hàng.")
            return

        customer_id = int(customer_id_item.text())
        customer = fetch_customer_by_id(customer_id)
        if not customer:
            QMessageBox.warning(self, "Lỗi", "Không thể tải thông tin khách hàng.")
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Sửa Khách Hàng")
        dialog.setStyleSheet("""
            background-color: #f0f0f0;
            font-size: 14px;
            padding: 20px;
            border: 2px solid #ccc;
            border-radius: 10px;
        """)

        layout = QVBoxLayout(dialog)

        form_layout = QFormLayout()

        self.name_input_edit = QLineEdit(customer.get('TenKH', ''))
        self.apply_style(self.name_input_edit)
        form_layout.addRow("Tên KH:", self.name_input_edit)

        self.birthdate_input_edit = QLineEdit(customer.get('NgaySinh', ''))
        self.birthdate_input_edit.setPlaceholderText("DD/MM/YYYY or DD-MM-YYYY")
        self.apply_style(self.birthdate_input_edit)
        form_layout.addRow("Ngày Sinh:", self.birthdate_input_edit)

        self.gender_input_edit = QLineEdit(customer.get('GioiTinh', ''))
        self.apply_style(self.gender_input_edit)
        form_layout.addRow("Giới Tính:", self.gender_input_edit)

        self.nationality_input_edit = QLineEdit(customer.get('QuocTich', ''))
        self.apply_style(self.nationality_input_edit)
        form_layout.addRow("Quốc Tịch:", self.nationality_input_edit)

        self.cccd_input_edit = QLineEdit(customer.get('CCCD', ''))
        self.apply_style(self.cccd_input_edit)
        form_layout.addRow("CCCD:", self.cccd_input_edit)

        self.phone_input_edit = QLineEdit(customer.get('SDT', ''))
        self.apply_style(self.phone_input_edit)
        form_layout.addRow("SĐT:", self.phone_input_edit)

        self.email_input_edit = QLineEdit(customer.get('Email', ''))
        self.apply_style(self.email_input_edit)
        form_layout.addRow("Email:", self.email_input_edit)

        save_button = QPushButton("Lưu")
        save_button.clicked.connect(lambda: self.save_customer_edit(customer_id, dialog))
        self.apply_style(save_button)
        form_layout.addRow(save_button)

        layout.addLayout(form_layout)

        dialog.exec()

    def save_customer_edit(self, customer_id, dialog):
        name = self.name_input_edit.text()
        birthdate = self.birthdate_input_edit.text()  # Getting text directly
        gender = self.gender_input_edit.text()
        nationality = self.nationality_input_edit.text()
        cccd = self.cccd_input_edit.text()
        phone = self.phone_input_edit.text()
        email = self.email_input_edit.text()

        if name and cccd and phone:
            if update_customer(customer_id, name, birthdate, gender, nationality, cccd, phone, email):
                QMessageBox.information(self, "Thành công", "Sửa thông tin khách hàng thành công.")
                self.load_customers()
                dialog.accept()
            else:
                QMessageBox.critical(self, "Lỗi", "Sửa thông tin khách hàng thất bại.")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")

    def delete_customer(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            confirm = QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xóa khách hàng này?",
                                           QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if confirm == QMessageBox.StandardButton.Yes:
                row = selected_rows[0].row()
                customer_id = int(self.table.item(row, 0).text())
                success = self.soft_delete_customer(customer_id)
                if success:
                    QMessageBox.information(self, "Thành công", "Xóa khách hàng thành công.")
                    self.load_customers()
                else:
                    QMessageBox.critical(self, "Lỗi", "Xóa khách hàng thất bại.")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để xóa.")

    def soft_delete_customer(self, customer_id):
        success = delete_customer(customer_id)
        return success

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

    def apply_style(self, widget):
        widget.setStyleSheet("""
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomerManagementWindow()
    window.show()
    sys.exit(app.exec())
