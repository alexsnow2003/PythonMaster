import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QFormLayout, QDateEdit
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
        self.table.setHorizontalHeaderLabels(["ID", "Tên KH", "Ngày Sinh", "Giới Tính", "Quốc Tịch", "CCCD", "SĐT", "Email"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
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
            self.table.setItem(row, 2, QTableWidgetItem(customer['NgaySinh'].strftime('%Y-%m-%d') if customer['NgaySinh'] else ''))
            self.table.setItem(row, 3, QTableWidgetItem(customer['GioiTinh']))
            self.table.setItem(row, 4, QTableWidgetItem(customer['QuocTich']))
            self.table.setItem(row, 5, QTableWidgetItem(customer['CCCD']))
            self.table.setItem(row, 6, QTableWidgetItem(customer['SDT']))
            self.table.setItem(row, 7, QTableWidgetItem(customer['Email']))

    def add_customer_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Thêm Khách Hàng")
        layout = QFormLayout()

        self.name_input = QLineEdit()
        layout.addRow("Tên KH:", self.name_input)

        self.birthdate_input = QDateEdit()
        self.birthdate_input.setDisplayFormat("yyyy-MM-dd")
        layout.addRow("Ngày Sinh:", self.birthdate_input)

        self.gender_input = QLineEdit()
        layout.addRow("Giới Tính:", self.gender_input)

        self.nationality_input = QLineEdit()
        layout.addRow("Quốc Tịch:", self.nationality_input)

        self.cccd_input = QLineEdit()
        layout.addRow("CCCD:", self.cccd_input)

        self.phone_input = QLineEdit()
        layout.addRow("SĐT:", self.phone_input)

        self.email_input = QLineEdit()
        layout.addRow("Email:", self.email_input)

        save_button = QPushButton("Lưu")
        save_button.clicked.connect(self.save_customer)
        layout.addRow(save_button)

        dialog.setLayout(layout)
        dialog.exec()

    def save_customer(self):
        name = self.name_input.text()
        birthdate = self.birthdate_input.date().toString(Qt.DateFormat.ISODate)
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
            else:
                QMessageBox.critical(self, "Lỗi", "Thêm khách hàng thất bại.")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")

    def edit_customer_dialog(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            row = selected_rows[0].row()
            customer_id = int(self.table.item(row, 0).text())
            customer = fetch_customer_by_id(customer_id)
            if customer:
                dialog = QDialog(self)
                dialog.setWindowTitle("Sửa Khách Hàng")
                layout = QFormLayout()

                self.name_input_edit = QLineEdit(customer['TenKH'])
                layout.addRow("Tên KH:", self.name_input_edit)

                self.birthdate_input_edit = QDateEdit()
                self.birthdate_input_edit.setDate(QDate.fromString(customer['NgaySinh'], Qt.DateFormat.ISODate) if customer['NgaySinh'] else QDate())
                self.birthdate_input_edit.setDisplayFormat("yyyy-MM-dd")
                layout.addRow("Ngày Sinh:", self.birthdate_input_edit)

                self.gender_input_edit = QLineEdit(customer['GioiTinh'])
                layout.addRow("Giới Tính:", self.gender_input_edit)

                self.nationality_input_edit = QLineEdit(customer['QuocTich'])
                layout.addRow("Quốc Tịch:", self.nationality_input_edit)

                self.cccd_input_edit = QLineEdit(customer['CCCD'])
                layout.addRow("CCCD:", self.cccd_input_edit)

                self.phone_input_edit = QLineEdit(customer['SDT'])
                layout.addRow("SĐT:", self.phone_input_edit)

                self.email_input_edit = QLineEdit(customer['Email'])
                layout.addRow("Email:", self.email_input_edit)

                save_button = QPushButton("Lưu")
                save_button.clicked.connect(lambda: self.save_customer_edit(customer_id))
                layout.addRow(save_button)

                dialog.setLayout(layout)
                dialog.exec()
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để chỉnh sửa.")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để chỉnh sửa.")

    def save_customer_edit(self, customer_id):
        name = self.name_input_edit.text()
        birthdate = self.birthdate_input_edit.date().toString(Qt.DateFormat.ISODate)
        gender = self.gender_input_edit.text()
        nationality = self.nationality_input_edit.text()
        cccd = self.cccd_input_edit.text()
        phone = self.phone_input_edit.text()
        email = self.email_input_edit.text()

        if name and cccd and phone:
            if update_customer(customer_id, name, birthdate, gender, nationality, cccd, phone, email):
                QMessageBox.information(self, "Thành công", "Sửa thông tin khách hàng thành công.")
                self.load_customers()
            else:
                QMessageBox.critical(self, "Lỗi", "Sửa thông tin khách hàng thất bại.")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")

    def delete_customer(self):
        selected_rows = self.table.selectionModel().selectedRows()
        if selected_rows:
            confirm = QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xóa khách hàng này?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
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
                self.table.setItem(row, 2, QTableWidgetItem(customer['NgaySinh'].strftime('%Y-%m-%d') if customer['NgaySinh'] else ''))
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
