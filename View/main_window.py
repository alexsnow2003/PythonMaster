import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from customer_management import CustomerManagementWindow  # Import CustomerManagementWindow
from employee_management import EmployeeManagementWindow


class MainWindow(QMainWindow):
    logout_signal = pyqtSignal()  # Signal to notify logout

    def __init__(self, role):
        super().__init__()
        self.setWindowTitle("Hotel Management System - Main")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.role_label = QLabel(f"Logged in as: {role}")
        layout.addWidget(self.role_label)

        self.manage_rooms_button = QPushButton("Quản lý phòng")
        self.manage_rooms_button.clicked.connect(self.manage_rooms)
        layout.addWidget(self.manage_rooms_button)

        self.manage_customers_button = QPushButton("Quản lý khách hàng")
        self.manage_customers_button.clicked.connect(self.manage_customers)  # Connect to manage_customers method
        layout.addWidget(self.manage_customers_button)

        self.manage_services_button = QPushButton("Quản lý dịch vụ")
        self.manage_services_button.clicked.connect(self.manage_services)
        layout.addWidget(self.manage_services_button)

        self.manage_revenue_button = QPushButton("Quản lý doanh thu")
        self.manage_revenue_button.clicked.connect(self.manage_revenue)
        layout.addWidget(self.manage_revenue_button)

        if role == 'admin':
            self.manage_staff_button = QPushButton("Quản lý nhân viên")
            self.manage_staff_button.clicked.connect(self.manage_staff)
            layout.addWidget(self.manage_staff_button)

        self.logout_button = QPushButton("Đăng xuất")
        self.logout_button.clicked.connect(self.confirm_logout)
        layout.addWidget(self.logout_button)

        self.central_widget.setLayout(layout)

        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                margin-bottom: 16px;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px;
                background-color: #0275d8;
                color: white;
                border: none;
                border-radius: 5px;
                margin-bottom: 8px;
            }
            QPushButton:hover {
                background-color: #025aa5;
            }
        """)

    def manage_rooms(self):
        QMessageBox.information(self, "Quản lý phòng", "Manage Rooms button clicked.")

    def manage_customers(self):
        self.customer_management_window = CustomerManagementWindow()  # Create an instance of CustomerManagementWindow
        self.customer_management_window.show()  # Show the CustomerManagementWindow

    def manage_services(self):
        QMessageBox.information(self, "Quản lý dịch vụ", "Manage Services button clicked.")

    def manage_revenue(self):
        QMessageBox.information(self, "Quản lý doanh thu", "Manage Revenue button clicked.")

    def manage_staff(self):
        self.employee_management_window = EmployeeManagementWindow()  # Create an instance of EmployeeManagementWindow
        self.employee_management_window.show()  # Show the EmployeeManagementWindow

    def confirm_logout(self):
        reply = QMessageBox.question(
            self, 'Xác nhận đăng xuất',
            'Bạn có chắc chắn muốn đăng xuất không?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.logout()

    def logout(self):
        self.close()  # Close the main window
        self.logout_signal.emit()  # Emit logout signal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow("admin")
    main_window.show()
    sys.exit(app.exec())
