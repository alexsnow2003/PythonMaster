import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QPushButton, QLineEdit, QLabel, QMessageBox, QTableWidget,
                             QTableWidgetItem, QHBoxLayout)
from customer_management import CustomerManagementWindow
from Entity.Database import *
class RoomManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Room Management")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.room_table = QTableWidget()
        self.room_table.setColumnCount(3)
        self.room_table.setHorizontalHeaderLabels(["Room ID", "Room Name", "Status"])
        layout.addWidget(self.room_table)

        self.load_rooms_button = QPushButton("Load Rooms")
        self.load_rooms_button.clicked.connect(self.load_rooms)
        layout.addWidget(self.load_rooms_button)

        self.search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter Room ID to search")
        self.search_button = QPushButton("Search Room")
        self.search_button.clicked.connect(self.search_room)
        self.search_layout.addWidget(self.search_input)
        self.search_layout.addWidget(self.search_button)
        layout.addLayout(self.search_layout)

        self.book_room_button = QPushButton("Book Room")
        self.book_room_button.clicked.connect(self.book_room)
        layout.addWidget(self.book_room_button)

        self.cancel_room_button = QPushButton("Cancel Room")
        self.cancel_room_button.clicked.connect(self.cancel_room)
        layout.addWidget(self.cancel_room_button)

        self.update_room_button = QPushButton("Update Room Info")
        self.update_room_button.clicked.connect(self.update_room_info)
        layout.addWidget(self.update_room_button)

        self.central_widget.setLayout(layout)

    def load_rooms(self):
        rooms = fetch_all_rooms()
        self.room_table.setRowCount(len(rooms))
        for row_idx, room in enumerate(rooms):
            self.room_table.setItem(row_idx, 0, QTableWidgetItem(str(room['MaPhong'])))
            self.room_table.setItem(row_idx, 1, QTableWidgetItem(room['TenPhong']))
            self.room_table.setItem(row_idx, 2, QTableWidgetItem(room['TinhTrang']))

    def search_room(self):
        room_id = self.search_input.text()
        room = search_room_by_id(room_id)
        if room:
            QMessageBox.information(self, "Room Found", f"Room ID: {room['MaPhong']}, Room Name: {room['TenPhong']}, Status: {room['TinhTrang']}")
        else:
            QMessageBox.warning(self, "Room Not Found", "No room found with the given ID.")

    def book_room(self):
        room_id = self.search_input.text()
        if book_room(room_id):
            QMessageBox.information(self, "Success", "Room booked successfully.")
            self.load_rooms()
        else:
            QMessageBox.warning(self, "Error", "Failed to book room.")

    def cancel_room(self):
        room_id = self.search_input.text()
        if cancel_room(room_id):
            QMessageBox.information(self, "Success", "Room booking cancelled.")
            self.load_rooms()
        else:
            QMessageBox.warning(self, "Error", "Failed to cancel room.")

    def update_room_info(self):
        room_id = self.search_input.text()
        room_name = "Updated Room Name"
        status = "Available"
        if update_room_info(room_id, room_name, status):
            QMessageBox.information(self, "Success", "Room info updated.")
            self.load_rooms()
        else:
            QMessageBox.warning(self, "Error", "Failed to update room info.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    room_management = RoomManagementWindow()
    room_management.show()
    sys.exit(app.exec())
