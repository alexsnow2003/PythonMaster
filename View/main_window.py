# main.py

import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QMessageBox, QGridLayout, QSizePolicy, QListWidget, QListWidgetItem
from PyQt6.QtCore import Qt, pyqtSignal, QTimer, QDateTime
from PyQt6.QtGui import QIcon, QFont

# Assuming you have these window classes defined elsewhere
from customer_management import CustomerManagementWindow
from employee_management import EmployeeManagementWindow
from RoomManagement import RoomManagementWindow
from ChangePass import ChangePasswordWidget  # Import ChangePasswordWidget
from invoice_management import InvoiceManagementWindow  # Import InvoiceManagementWindow

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
        self.sidebar.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)  # Kéo dài xuống hết cửa sổ

        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/customer.png"), "Quản lý khách hàng"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/room.png"), "Quản lý phòng"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/service.png"), "Quản lý dịch vụ"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/device.png"), "Quản lý thiết bị"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/staff.png"), "Quản lý nhân viên"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/invoice.png"), "Quản lý hóa đơn"))  # Thêm mục hóa đơn
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/revenue.png"), "Thống kê doanh thu"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/password.png"), "Đổi mật khẩu"))
        self.sidebar.addItem(QListWidgetItem(QIcon("../Icon/logout.png"), "Thoát"))
        self.sidebar.itemClicked.connect(self.on_sidebar_item_clicked)

        main_layout.addWidget(self.sidebar)

        # Room status grid
        self.room_status_grid = QWidget()
        self.grid_layout = QGridLayout(self.room_status_grid)
        self.load_rooms_from_database()

        # Header (logo, role, and real-time clock)
        header_layout = QVBoxLayout()
        self.logo_label = QLabel("Hotel Management System")
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.logo_label.setStyleSheet("color: #444; margin-bottom: 20px;")  # Tăng khoảng cách dưới logo
        header_layout.addWidget(self.logo_label)

        self.role_label = QLabel(f"Logged in as: {role}")
        self.role_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.role_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #333; margin-bottom: 10px;")
        header_layout.addWidget(self.role_label)

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("font-size: 18px; color: #333; margin-bottom: 20px;")  # Tăng khoảng cách dưới thời gian
        header_layout.addWidget(self.time_label)

        # Thêm header_layout vào một QWidget
        header_widget = QWidget()
        header_widget.setLayout(header_layout)
        header_widget.setStyleSheet("background-color: #f0f0f0; padding: 20px;")  # Màu nền cho header và padding
        header_widget.setFixedHeight(150)  # Tăng chiều cao cho header

        # Tạo layout cho room_status_grid để chứa header_widget và grid_layout
        room_layout = QVBoxLayout()
        room_layout.addWidget(header_widget)
        room_layout.addWidget(self.room_status_grid)

        # Thêm room_layout vào main_layout
        main_layout.addLayout(room_layout)

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

        # Timer to update time
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second

        self.update_time()  # Initialize with current time

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        self.time_label.setText(current_time)

    def load_rooms_from_database(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                user='root',
                password='123456',  # Thay bằng mật khẩu của bạn
                database='QLKS'
            )

            cursor = connection.cursor()
            cursor.execute("SELECT MaPhong, TinhTrangPhong FROM Phong")
            rooms = cursor.fetchall()

            for i, (ma_phong, tinh_trang) in enumerate(rooms):
                color = "green" if tinh_trang == "Trống" else "red" if tinh_trang == "Đã đặt" else "yellow"
                btn = QPushButton(f"{ma_phong}\n{tinh_trang}")
                btn.setStyleSheet(f"background-color: {color};")
                btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                self.grid_layout.addWidget(btn, i // 4, i % 4)

            connection.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")

    def on_sidebar_item_clicked(self, item):
        if item.text() == "Đổi mật khẩu":
            self.change_password()
        elif item.text() == "Thoát":
            self.confirm_logout()
        elif item.text() == "Quản lý khách hàng":
            self.manage_customers()
        elif item.text() == "Quản lý phòng":
            self.manage_rooms()
        elif item.text() == "Quản lý dịch vụ":
            self.manage_services()
        elif item.text() == "Quản lý thiết bị":
            self.manage_devices()
        elif item.text() == "Quản lý nhân viên":
            self.manage_staff()
        elif item.text() == "Quản lý hóa đơn":
            self.manage_invoices()  # Thêm vào đây
        elif item.text() == "Thống kê doanh thu":
            self.manage_revenue()

    def change_password(self):
        print("Change password button clicked")  # Debug: Xem liệu phương thức này có được gọi hay không
        change_password_widget = ChangePasswordWidget("admin")  # Truyền username vào đây nếu cần
        change_password_widget.exec()

    def manage_rooms(self):
        self.room_management_window = RoomManagementWindow()  # Tạo instance của RoomManagementWindow
        self.room_management_window.show()  # Hiển thị RoomManagementWindow

    def manage_customers(self):
        self.customer_management_window = CustomerManagementWindow()  # Tạo instance của CustomerManagementWindow
        self.customer_management_window.show()  # Hiển thị CustomerManagementWindow

    def manage_services(self):
        QMessageBox.information(self, "Quản lý dịch vụ", "Manage Services button clicked.")

    def manage_revenue(self):
        QMessageBox.information(self, "Quản lý doanh thu", "Manage Revenue button clicked.")

    def manage_staff(self):
        self.employee_management_window = EmployeeManagementWindow()  # Tạo instance của EmployeeManagementWindow
        self.employee_management_window.show()  # Hiển thị EmployeeManagementWindow

    def manage_invoices(self):
        """Hiển thị cửa sổ quản lý hóa đơn"""
        self.invoice_management_window = InvoiceManagementWindow()  # Tạo instance của InvoiceManagementWindow
        self.invoice_management_window.show()  # Hiển thị InvoiceManagementWindow

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
        self.close()  # Đóng cửa sổ chính
        self.logout_signal.emit()  # Phát tín hiệu logout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow("admin")
    main_window.show()
    sys.exit(app.exec())
