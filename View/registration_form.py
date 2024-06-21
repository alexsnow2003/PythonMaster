import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
from Entity.Database import create_connection, close_connection
from login_form import LoginRegistrationForm  # Import the login form


class RegistrationForm(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Registration Form")
        self.setGeometry(200, 200, 400, 300)

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

        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register_user)
        layout.addWidget(self.register_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        layout.addWidget(self.cancel_button)

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

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if username and password and confirm_password:
            if password == confirm_password:
                connection = create_connection()
                if connection:
                    cursor = connection.cursor()
                    try:
                        cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
                        connection.commit()
                        QMessageBox.information(self, "Registration Successful", "Registration completed successfully.")
                        self.close()  # Close registration form
                        self.parent().show()  # Show the login form
                    except Exception as e:
                        QMessageBox.critical(self, "Error", f"Database error: {e}")
                    finally:
                        cursor.close()
                        close_connection(connection)
            else:
                QMessageBox.warning(self, "Error", "Passwords do not match.")
        else:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_registration_form = LoginRegistrationForm()
    login_registration_form.show()
    sys.exit(app.exec())
