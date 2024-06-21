import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from Entity.Database import create_connection, close_connection
from main_window import MainWindow
from mysql.connector import Error

class LoginRegistrationForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login / Registration Form")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.open_registration_form)
        layout.addWidget(self.register_button)

        self.central_widget.setLayout(layout)

        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
                margin-bottom: 8px;
            }
            QLineEdit {
                font-size: 14px;
                padding: 8px;
                margin-bottom: 16px;
            }
            QPushButton {
                font-size: 16px;
                padding: 10px;
                background-color: #5cb85c;
                color: white;
                border: none;
                border-radius: 5px;
                margin-bottom: 8px;
            }
            QPushButton:hover {
                background-color: #4cae4c;
            }
        """)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username and password:
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
                    result = cursor.fetchone()
                    if result:
                        role = result[3]  # Assuming 'role' is the fourth column (index 3) in your table
                        self.open_main_window(role)
                        self.close()  # Close the login form after successful login
                    else:
                        QMessageBox.warning(self, "Error", "Invalid username or password")
                except Error as e:
                    QMessageBox.critical(self, "Error", f"Database error: {e}")
                finally:
                    cursor.close()
                    close_connection(connection)
        else:
            QMessageBox.warning(self, "Error", "Please enter both username and password")

    def open_main_window(self, role):
        self.main_window = MainWindow(role)
        self.main_window.show()

    def open_registration_form(self):
        from registration_form import RegistrationForm  # Move the import statement here
        if not self.registration_form:
            self.registration_form = RegistrationForm(parent=self)
        self.registration_form.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_registration_form = LoginRegistrationForm()
    login_registration_form.show()
    sys.exit(app.exec())
