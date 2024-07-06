import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QMessageBox, QGridLayout, QSizePolicy, QListWidget, QListWidgetItem, QAction, QMenuBar, QMenu
from PyQt6.QtCore import Qt, pyqtSignal, QTimer, QDateTime
from PyQt6.QtGui import QIcon, QFont

# Assuming you have these window classes defined elsewhere
from customer_management import CustomerManagementWindow
from employee_management import EmployeeManagementWindow
from RoomManagement import RoomManagementWindow
from ChangePass import ChangePasswordWidget  # Import ChangePasswordWidget
from ServiceManagementWindow import ServiceManagementWindow  # Import new ServiceManagementWindow

class MainWindow(QMainWindow):
    logout_signal = pyqtSignal()  # Signal để thông báo đăng xuất

    def __init__(self, role):
        super().__init__()
        self.setWindowTitle("Hotel Management System - Main")
        self.setGeometry(100, 100, 1200, 800)  # Tăng kích thước cửa sổ

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QHBoxLayout()
        self.central_widget.setLayout(main_layout)

        # Sidebar
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/password.png"), "Đổi mật khẩu"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/logout.png"), "Thoát"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/customer.png"), "Quản lý khách hàng"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/room.png"), "Quản lý phòng"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/service.png"), "Quản lý dịch vụ"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/device.png"), "Quản lý thiết bị"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/staff.png"), "Quản lý nhân viên"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/revenue.png"), "Thống kê doanh thu"))

        self.sidebar.itemClicked.connect(self.on_sidebar_item_clicked)

        main_layout.addWidget(self.sidebar)

        # Room status grid
        self.room_status_grid = QWidget()
        self.grid_layout = QGridLayout(self.room_status_grid)
        self.load_rooms_from_database()

        main_layout.addWidget(self.room_status_grid)

        # Header (logo, role, and real-time clock)
        header_layout = QVBoxLayout()
        self.logo_label = QLabel("Hotel Management System")
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.logo_label.setStyleSheet("color: #444; margin-bottom: 30px;")
        header_layout.addWidget(self.logo_label)

        self.role_label = QLabel(f"Logged in as: {role}")
        self.role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.role_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")
        header_layout.addWidget(self.role_label)

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 18px; color: #333;")
        header_layout.addWidget(self.time_label)

        main_layout.addLayout(header_layout)

        # Timer to update time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        self.update_time()  # Initialize with current time

        # Menu Bar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("Tệp")

        # Tạo các hành động cho menu
        self.change_password_action = QAction(QIcon("../Icon/password.png"), "Đổi mật khẩu", self)
        self.change_password_action.triggered.connect(self.change_password)
        self.file_menu.addAction(self.change_password_action)

        self.logout_action = QAction(QIcon("../Icon/logout.png"), "Đăng xuất", self)
        self.logout_action.triggered.connect(self.confirm_logout)
        self.file_menu.addAction(self.logout_action)

        self.view_menu = self.menu_bar.addMenu("Xem")
        self.view_customers_action = QAction(QIcon("../Icon/customer.png"), "Quản lý khách hàng", self)
        self.view_customers_action.triggered.connect(self.show_customer_management_window)
        self.view_menu.addAction(self.view_customers_action)

        self.view_rooms_action = QAction(QIcon("../Icon/room.png"), "Quản lý phòng", self)
        self.view_rooms_action.triggered.connect(self.show_room_management_window)
        self.view_menu.addAction(self.view_rooms_action)

        self.view_services_action = QAction(QIcon("../Icon/service.png"), "Quản lý dịch vụ", self)
        self.view_services_action.triggered.connect(self.show_service_management_window)
        self.view_menu.addAction(self.view_services_action)

        self.view_equipment_action = QAction(QIcon("../Icon/device.png"), "Quản lý thiết bị", self)
        self.view_equipment_action.triggered.connect(self.show_equipment_management_window)
        self.view_menu.addAction(self.view_equipment_action)

        self.view_employees_action = QAction(QIcon("../Icon/staff.png"), "Quản lý nhân viên", self)
        self.view_employees_action.triggered.connect(self.show_employee_management_window)
        self.view_menu.addAction(self.view_employees_action)

        self.view_revenue_action = QAction(QIcon("../Icon/revenue.png"), "Thống kê doanh thu", self)
        self.view_revenue_action.triggered.connect(self.show_revenue_statistics_window)
        self.view_menu.addAction(self.view_revenue_action)

        # StyleSheet
        self.setStyleSheet("""
            QListWidget {
                font-size: 18px;
                background-color: #333;
                color: white;
                border: none;
            }
            QListWidgetItem {
                padding: 10px;
                background-color: #333;
                color: white;
            }
            QListWidget::item:hover {
                background-color: #555;
            }
            QListWidget::item:selected {
                background-color: #0275d8;
                color: white;
            }
            QLabel {
                font-size: 18px;
                margin-bottom: 16px;
            }
            QPushButton {
                font-size: 18px;
                padding: 15px;
                background-color: #0275d8;
                color: white;
                border: none;
                border-radius: 5px;
                margin-bottom: 10px;
                min-width: 200px;
                text-align: left;
                padding-left: 20px;
            }
            QPushButton:hover {
                background-color: #025aa5;
            }
            QPushButton:pressed {
                background-color: #014682;
            }
        """)

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        self.time_label.setText(current_time)

    def load_rooms_from_database(self):
        # Your database loading logic here
        pass

    def on_sidebar_item_clicked(self, item):
        text = item.text()
        if text == "Đổi mật khẩu":
            self.change_password()
        elif text == "Thoát":
            self.confirm_logout()
        elif text == "Quản lý khách hàng":
            self.show_customer_management_window()
        elif text == "Quản lý phòng":
            self.show_room_management_window()
        elif text == "Quản lý dịch vụ":
            self.show_service_management_window()
        elif text == "Quản lý thiết bị":
            self.show_equipment_management_window()
        elif text == "Quản lý nhân viên":
            self.show_employee_management_window()
        elif text == "Thống kê doanh thu":
            self.show_revenue_statistics_window()

    def change_password(self):
        change_password_widget = ChangePasswordWidget()
        change_password_widget.show()

    def confirm_logout(self):
        reply = QMessageBox.question(self, 'Xác nhận đăng xuất', 'Bạn có chắc chắn muốn đăng xuất?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.logout_signal.emit()
            self.close()

    def show_customer_management_window(self):
        self.customer_management_window = CustomerManagementWindow()
        self.customer_management_window.show()

    def show_room_management_window(self):
        self.room_management_window = RoomManagementWindow()
        self.room_management_window.show()

    def show_service_management_window(self):
        self.service_management_window = ServiceManagementWindow()
        self.service_management_window.show()

    def show_equipment_management_window(self):
        # Add your equipment management window
        pass

    def show_employee_management_window(self):
        self.employee_management_window = EmployeeManagementWindow()
        self.employee_management_window.show()

    def show_revenue_statistics_window(self):
        # Add your revenue statistics window
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(role="Admin")  # Example role
    window.show()
    sys.exit(app.exec())
