import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, \
    QLineEdit, QHBoxLayout, QTableWidget, QTableWidgetItem, QFormLayout, QComboBox, QDateEdit
from PyQt6.QtCore import Qt, QDate

from Entity.NhanVien import fetch_all_employees, fetch_employee_by_id, add_employee, update_employee, delete_employee, \
    search_employees


class EmployeeManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý nhân viên")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.employee_table = QTableWidget()
        self.employee_table.setColumnCount(7)
        self.employee_table.setHorizontalHeaderLabels(
            ["Mã NV", "Tên NV", "Ngày sinh", "Giới tính", "Quốc tịch", "CCCD", "SĐT"])
        self.load_data()
        self.layout.addWidget(self.employee_table)

        self.search_label = QLabel("Tìm kiếm:")
        self.search_entry = QLineEdit()
        self.search_button = QPushButton("Tìm")
        self.search_button.clicked.connect(self.search_employee)

        self.search_layout = QHBoxLayout()
        self.search_layout.addWidget(self.search_label)
        self.search_layout.addWidget(self.search_entry)
        self.search_layout.addWidget(self.search_button)
        self.layout.addLayout(self.search_layout)

        self.form_layout = QFormLayout()
        self.name_entry = QLineEdit()
        self.birthdate_entry = QDateEdit()
        self.birthdate_entry.setCalendarPopup(True)
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Nam", "Nữ", "Khác"])
        self.nationality_entry = QLineEdit()
        self.cccd_entry = QLineEdit()
        self.address_entry = QLineEdit()
        self.phone_entry = QLineEdit()
        self.position_entry = QLineEdit()
        self.salary_entry = QLineEdit()

        self.form_layout.addRow("Tên nhân viên:", self.name_entry)
        self.form_layout.addRow("Ngày sinh:", self.birthdate_entry)
        self.form_layout.addRow("Giới tính:", self.gender_combo)
        self.form_layout.addRow("Quốc tịch:", self.nationality_entry)
        self.form_layout.addRow("CCCD:", self.cccd_entry)
        self.form_layout.addRow("Địa chỉ:", self.address_entry)
        self.form_layout.addRow("SĐT:", self.phone_entry)
        self.form_layout.addRow("Chức vụ:", self.position_entry)
        self.form_layout.addRow("Lương:", self.salary_entry)

        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Thêm")
        self.add_button.clicked.connect(self.add_employee)
        self.update_button = QPushButton("Cập nhật")
        self.update_button.clicked.connect(self.update_employee)
        self.delete_button = QPushButton("Xóa")
        self.delete_button.clicked.connect(self.delete_employee)
        self.clear_button = QPushButton("Xóa trắng")
        self.clear_button.clicked.connect(self.clear_fields)

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.delete_button)
        self.button_layout.addWidget(self.clear_button)

        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.button_layout)

        self.central_widget.setLayout(self.layout)

        self.populate_table()

    def populate_table(self):
        employees = fetch_all_employees()
        self.employee_table.setRowCount(len(employees))
        row = 0
        for employee in employees:
            self.employee_table.setItem(row, 0, QTableWidgetItem(str(employee['MaNV'])))
            self.employee_table.setItem(row, 1, QTableWidgetItem(employee['TenNV']))
            self.employee_table.setItem(row, 2, QTableWidgetItem(employee['NgaySinh'].strftime('%Y-%m-%d')))
            self.employee_table.setItem(row, 3, QTableWidgetItem(employee['GioiTinh']))
            self.employee_table.setItem(row, 4, QTableWidgetItem(employee['QuocTich']))
            self.employee_table.setItem(row, 5, QTableWidgetItem(employee['CCCD']))
            self.employee_table.setItem(row, 6, QTableWidgetItem(employee['SDT']))
            row += 1

    def load_data(self):
        employees = fetch_all_employees()
        self.employee_table.setRowCount(len(employees))
        for idx, employee in enumerate(employees):
            self.employee_table.setItem(idx, 0, QTableWidgetItem(str(employee['MaNV'])))
            self.employee_table.setItem(idx, 1, QTableWidgetItem(employee['TenNV']))
            self.employee_table.setItem(idx, 2, QTableWidgetItem(employee['NgaySinh'].strftime("%Y-%m-%d")))
            self.employee_table.setItem(idx, 3, QTableWidgetItem(employee['GioiTinh']))
            self.employee_table.setItem(idx, 4, QTableWidgetItem(employee['QuocTich']))
            self.employee_table.setItem(idx, 5, QTableWidgetItem(employee['CCCD']))
            self.employee_table.setItem(idx, 6, QTableWidgetItem(employee['SDT']))

    def search_employee(self):
        keyword = self.search_entry.text()
        if keyword.strip() != "":
            employees = search_employees(keyword)
            self.employee_table.setRowCount(len(employees))
            for idx, employee in enumerate(employees):
                self.employee_table.setItem(idx, 0, QTableWidgetItem(str(employee['MaNV'])))
                self.employee_table.setItem(idx, 1, QTableWidgetItem(employee['TenNV']))
                self.employee_table.setItem(idx, 2, QTableWidgetItem(employee['NgaySinh'].strftime("%Y-%m-%d")))
                self.employee_table.setItem(idx, 3, QTableWidgetItem(employee['GioiTinh']))
                self.employee_table.setItem(idx, 4, QTableWidgetItem(employee['QuocTich']))
                self.employee_table.setItem(idx, 5, QTableWidgetItem(employee['CCCD']))
                self.employee_table.setItem(idx, 6, QTableWidgetItem(employee['SDT']))

    def add_employee(self):
        name = self.name_entry.text()
        birthdate = self.birthdate_entry.date().toString("yyyy-MM-dd")
        gender = self.gender_combo.currentText()
        nationality = self.nationality_entry.text()
        cccd = self.cccd_entry.text()
        address = self.address_entry.text()
        phone = self.phone_entry.text()
        position = self.position_entry.text()
        salary = self.salary_entry.text()
        department_id = 1  # Thay bằng MaPB thực tế nếu có

        if all([name, birthdate, gender, nationality, cccd, address, phone, position, salary]):
            add_employee(name, birthdate, gender, nationality, cccd, address, phone, position, salary, department_id)
            QMessageBox.information(self, "Thành công", "Thêm nhân viên thành công")
            self.populate_table()
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")

    def update_employee(self):
        selected_items = self.employee_table.selectedItems()
        if selected_items:
            employee_id = int(selected_items[0].text())
            name = self.name_entry.text()
            birthdate = self.birthdate_entry.date().toString("yyyy-MM-dd")
            gender = self.gender_combo.currentText()
            nationality = self.nationality_entry.text()
            cccd = self.cccd_entry.text()
            address = self.address_entry.text()
            phone = self.phone_entry.text()
            position = self.position_entry.text()
            salary = self.salary_entry.text()
            department_id = 1  # Thay bằng MaPB thực tế nếu có

            if all([name, birthdate, gender, nationality, cccd, address, phone, position, salary]):
                update_employee(employee_id, name, birthdate, gender, nationality, cccd, address, phone, position,
                                salary, department_id)
                QMessageBox.information(self, "Thành công", "Cập nhật nhân viên thành công")
                self.populate_table()
                self.clear_fields()
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin")

    def delete_employee(self):
        selected_items = self.employee_table.selectedItems()
        if selected_items:
            employee_id = int(selected_items[0].text())
            delete_employee(employee_id)
            QMessageBox.information(self, "Thành công", "Xóa nhân viên thành công")
            self.populate_table()
            self.clear_fields()
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một nhân viên để xóa")

    def clear_fields(self):
        self.name_entry.clear()
        self.birthdate_entry.setDate(QDate.currentDate())
        self.gender_combo.setCurrentIndex(0)
        self.nationality_entry.clear()
        self.cccd_entry.clear()
        self.address_entry.clear()
        self.phone_entry.clear()
        self.position_entry.clear()
        self.salary_entry.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeManagementWindow()
    window.show()
    sys.exit(app.exec())
