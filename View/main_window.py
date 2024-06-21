import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from customer_management import CustomerManagementWindow  # Import CustomerManagementWindow


class MainWindow(QMainWindow):
    def __init__(self, role):
        super().__init__()
        self.setWindowTitle("Hotel Management System - Main")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.role_label = QLabel(f"Logged in as: {role}")
        layout.addWidget(self.role_label)

        self.manage_rooms_button = QPushButton("Manage Rooms")
        self.manage_rooms_button.clicked.connect(self.manage_rooms)
        layout.addWidget(self.manage_rooms_button)

        self.manage_customers_button = QPushButton("Manage Customers")
        self.manage_customers_button.clicked.connect(self.manage_customers)  # Connect to manage_customers method
        layout.addWidget(self.manage_customers_button)

        self.manage_services_button = QPushButton("Manage Services")
        self.manage_services_button.clicked.connect(self.manage_services)
        layout.addWidget(self.manage_services_button)

        self.manage_revenue_button = QPushButton("Manage Revenue")
        self.manage_revenue_button.clicked.connect(self.manage_revenue)
        layout.addWidget(self.manage_revenue_button)

        if role == 'admin':
            self.manage_staff_button = QPushButton("Manage Staff")
            self.manage_staff_button.clicked.connect(self.manage_staff)
            layout.addWidget(self.manage_staff_button)

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
        QMessageBox.information(self, "Manage Rooms", "Manage Rooms button clicked.")

    def manage_customers(self):
        self.customer_management_window = CustomerManagementWindow()  # Create an instance of CustomerManagementWindow
        self.customer_management_window.show()  # Show the CustomerManagementWindow


    def manage_services(self):
        QMessageBox.information(self, "Manage Services", "Manage Services button clicked.")

    def manage_revenue(self):
        QMessageBox.information(self, "Manage Revenue", "Manage Revenue button clicked.")

    def manage_staff(self):
        QMessageBox.information(self, "Manage Staff", "Manage Staff button clicked.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow("admin")
    main_window.show()
    sys.exit(app.exec())
