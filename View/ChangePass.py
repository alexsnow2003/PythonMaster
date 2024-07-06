import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import mysql.connector


class ChangePasswordWidget(QWidget):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.old_password_label = QLabel('Old Password:')
        self.old_password_input = QLineEdit()
        self.old_password_input.setEchoMode(QLineEdit.Password)

        self.new_password_label = QLabel('New Password:')
        self.new_password_input = QLineEdit()
        self.new_password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel('Confirm New Password:')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.change_password_button = QPushButton('Change Password')
        self.change_password_button.clicked.connect(self.change_password)

        layout.addWidget(self.old_password_label)
        layout.addWidget(self.old_password_input)
        layout.addWidget(self.new_password_label)
        layout.addWidget(self.new_password_input)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)
        layout.addWidget(self.change_password_button)

        self.setLayout(layout)
        self.setWindowTitle('Change Password')
        self.show()

    def change_password(self):
        old_password = self.old_password_input.text()
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if new_password != confirm_password:
            QMessageBox.warning(self, 'Error', 'New password and confirmation do not match.')
            return

        try:
            conn = mysql.connector.connect(
                host='localhost',
                port=3307,
                user='root',
                password='123456',
                database='QLKS'
            )
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM user WHERE username = %s", (self.username,))
            result = cursor.fetchone()

            if result and result[0] == old_password:
                cursor.execute("UPDATE user SET password = %s WHERE username = %s", (new_password, self.username))
                conn.commit()
                QMessageBox.information(self, 'Success', 'Password changed successfully.')
            else:
                QMessageBox.warning(self, 'Error', 'Old password is incorrect.')

        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Database Error', f"Error: {err}")
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    username = 'snow'  # Replace with the logged-in user's username
    change_password_widget = ChangePasswordWidget(username)
    sys.exit(app.exec_())
