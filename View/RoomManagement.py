import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QMessageBox, QFrame, QWidget, QHBoxLayout,
    QGridLayout, QDialog, QFormLayout, QLineEdit, QDialogButtonBox, QInputDialog
)
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtCore import Qt
import mysql.connector
from mysql.connector import Error
from datetime import datetime

from View.AddRoomDialog import AddRoomDialog
from View.BookRoomDialog import BookRoomDialog
from View.CancelBookingDialog import CancelBookingDialog
from View.PaymentDialog import PaymentDialog
from View.RevenueManagement import RevenueManagementWindow
from View.RoomDetailsDialog import RoomDetailsDialog


class RoomManagementWindow(QMainWindow):
    def __init__(self, role='user'):
        super().__init__()
        self.setWindowTitle("Quản lý phòng")
        self.setGeometry(100, 100, 1200, 900)  # Thay đổi kích thước cửa sổ để hiển thị nhiều thông tin hơn
        self.role = role

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        button_layout = QVBoxLayout()

        self.logo_label = QLabel("Hotel Management System")
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.logo_label.setStyleSheet("color: #4A90E2; margin-bottom: 30px;")
        main_layout.addWidget(self.logo_label)

        self.room_label = QLabel("Danh sách phòng")
        self.room_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.room_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #333;")
        header_layout.addWidget(self.room_label)

        self.refresh_button = QPushButton("Làm mới")
        self.refresh_button.setIcon(QIcon("icons/refresh.png"))
        self.refresh_button.clicked.connect(self.load_rooms)
        self.refresh_button.setStyleSheet(
            "font-size: 16px; padding: 12px; background-color: #5cb85c; color: white; border: none; border-radius: 8px;")  # Tăng padding
        header_layout.addWidget(self.refresh_button)

        main_layout.addLayout(header_layout)

        self.room_grid = QGridLayout()
        main_layout.addLayout(self.room_grid)

        button_frame = QFrame()
        button_frame.setStyleSheet(
            "QFrame { background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 10px; padding: 20px; }")
        button_frame.setLayout(button_layout)

        if self.role == 'admin':
            self.manage_rooms_button = QPushButton("Thêm phòng")
            self.manage_rooms_button.setIcon(QIcon("icons/add.png"))
            self.manage_rooms_button.clicked.connect(self.add_room)
            button_layout.addWidget(self.manage_rooms_button)

        self.book_room_button = QPushButton("Đặt phòng")
        self.book_room_button.setIcon(QIcon("icons/book.png"))
        self.book_room_button.clicked.connect(self.book_room)
        button_layout.addWidget(self.book_room_button)

        self.cancel_booking_button = QPushButton("Hủy phòng")
        self.cancel_booking_button.setIcon(QIcon("icons/cancel.png"))
        self.cancel_booking_button.clicked.connect(self.cancel_booking)
        button_layout.addWidget(self.cancel_booking_button)

        self.payment_button = QPushButton("Thanh toán")
        self.payment_button.setIcon(QIcon("icons/payment.png"))
        self.payment_button.clicked.connect(self.process_payment)
        button_layout.addWidget(self.payment_button)

        self.revenue_button = QPushButton("Xem doanh thu")
        self.revenue_button.setIcon(QIcon("icons/revenue.png"))
        self.revenue_button.clicked.connect(self.view_revenue)
        button_layout.addWidget(self.revenue_button)

        self.search_room_button = QPushButton("Tìm kiếm phòng")
        self.search_room_button.setIcon(QIcon("icons/search.png"))
        self.search_room_button.clicked.connect(self.search_room)
        button_layout.addWidget(self.search_room_button)

        main_layout.addWidget(button_frame)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.central_widget.setLayout(main_layout)

        self.setStyleSheet("""
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
                border-radius: 8px;
                margin-bottom: 12px;
                min-width: 220px;
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

        self.load_rooms()

    def load_rooms(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                database='QLKS',
                user='root',
                password='123456'
            )
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                cursor.execute(
                    "SELECT Phong.MaPhong, Phong.MaLP, LoaiPhong.TenLP, LoaiPhong.Gia, Phong.TinhTrangPhong "
                    "FROM Phong INNER JOIN LoaiPhong ON Phong.MaLP = LoaiPhong.MaLP"
                )
                rooms = cursor.fetchall()
                self.display_rooms(rooms)
                cursor.close()
        except Error as e:
            print(f"Error loading rooms: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

    def display_rooms(self, rooms):
        for i in reversed(range(self.room_grid.count())):
            self.room_grid.itemAt(i).widget().setParent(None)

        status_icons = {
            "Trống": "icons/empty.png",
            "Đã đặt": "icons/booked.png",
            "Đang dọn dẹp": "icons/cleaning.png"
        }
        row = 0
        col = 0
        for room in rooms:
            icon_path = status_icons.get(room['TinhTrangPhong'], "")
            room_widget = self.create_room_widget(room, icon_path)
            self.room_grid.addWidget(room_widget, row, col)
            col += 1
            if col >= 4:  # Thay đổi số cột để hiển thị nhiều phòng hơn
                col = 0
                row += 1

    def create_room_widget(self, room, icon_path):
        room_widget = QWidget()
        layout = QVBoxLayout()

        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(icon_path).scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        info_label = QLabel(f"Phòng {room['MaPhong']}\nGiá: {room['Gia']} VND\nTrạng thái: {room['TinhTrangPhong']}")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(icon_label)
        layout.addWidget(info_label)

        room_widget.setLayout(layout)
        room_widget.setStyleSheet("border: 1px solid #ddd; border-radius: 12px; padding: 10px; margin: 5px; background-color: #fff;")  # Cải thiện giao diện

        # Set up the click event for the room_widget
        room_widget.mousePressEvent = lambda event, room_id=room['MaPhong']: self.show_room_details(room_id)

        return room_widget

    def show_room_details(self, room_id):
        dialog = RoomDetailsDialog(self, room_id)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_rooms()

    def add_room(self):
        dialog = AddRoomDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_rooms()

    def book_room(self):
        dialog = BookRoomDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_rooms()

    def cancel_booking(self):
        dialog = CancelBookingDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_rooms()

    def process_payment(self):
        dialog = PaymentDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_rooms()

    def view_revenue(self):
        self.revenue_window = RevenueManagementWindow()
        self.revenue_window.show()

    def search_room(self):
        text, ok = QInputDialog.getText(self, "Tìm kiếm phòng", "Nhập mã phòng cần tìm:")
        if ok and text:
            try:
                connection = mysql.connector.connect(
                    host='localhost',
                    port=3307,
                    database='QLKS',
                    user='root',
                    password='123456'
                )
                if connection.is_connected():
                    cursor = connection.cursor(dictionary=True)
                    cursor.execute(
                        "SELECT Phong.MaPhong, Phong.MaLP, LoaiPhong.TenLP, LoaiPhong.Gia, Phong.TinhTrangPhong "
                        "FROM Phong INNER JOIN LoaiPhong ON Phong.MaLP = LoaiPhong.MaLP WHERE Phong.MaPhong LIKE %s",
                        (f'%{text}%',)
                    )
                    rooms = cursor.fetchall()
                    if rooms:
                        self.display_rooms(rooms)
                    else:
                        QMessageBox.information(self, "Không tìm thấy", f"Không tìm thấy phòng có mã '{text}'.")
                    cursor.close()
            except Error as e:
                print(f"Error searching room: {e}")
            finally:
                if 'connection' in locals() and connection.is_connected():
                    connection.close()

    def logout(self):
        self.close()
