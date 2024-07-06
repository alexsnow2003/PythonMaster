import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt
from Entity.Database import create_connection, close_connection
from mysql.connector import Error
from main_window import MainWindow  # Đảm bảo import đúng lớp MainWindow

class LoginRegistrationForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(457, 426)
        self.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.username_input = QtWidgets.QTextEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(140, 100, 171, 31))
        self.username_input.setObjectName("username_input")
        self.password_input = QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(140, 160, 171, 31))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 61, 16))
        self.label_3.setObjectName("label_3")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(160, 230, 131, 41))
        self.login_button.setObjectName("login_button")
        self.register_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(240, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.register_button.setFont(font)
        self.register_button.setObjectName("register_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 300, 161, 16))
        self.label_4.setObjectName("label_4")
        self.show_password_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_password_button.setGeometry(QtCore.QRect(320, 160, 30, 30))
        self.show_password_button.setObjectName("show_password_button")
        self.show_password_button.setIcon(QtGui.QIcon("../Icon/viewpass.png"))
        self.show_password_button.setCheckable(True)
        self.show_password_button.clicked.connect(self.toggle_password_visibility)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.open_registration_form)

        self.main_window = None
        self.registration_form = None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Login"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Nhập username"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Nhập password"))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Đăng nhập"))
        self.register_button.setText(_translate("MainWindow", "Đăng ký"))
        self.label_4.setText(_translate("MainWindow", "Bạn chưa có tài khoản ? "))
        self.show_password_button.setText("")

    def toggle_password_visibility(self):
        if self.show_password_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def login(self):
        username = self.username_input.toPlainText()
        password = self.password_input.text()
        print(f"Attempting to login with username: {username} and password: {password}")

        if username and password:
            connection = create_connection()
            if connection:
                cursor = connection.cursor()
                try:
                    cursor.execute("SELECT * FROM user WHERE username=%s AND password=%s", (username, password))
                    result = cursor.fetchone()
                    if result:
                        role = result[3]  # Giả sử 'role' là cột thứ tư (index 3) trong bảng
                        print(f"Login successful. Role: {role}")
                        self.open_main_window(role)
                        self.hide()  # Ẩn form đăng nhập sau khi đăng nhập thành công
                    else:
                        QMessageBox.warning(None, "Error", "Invalid username or password")
                except Error as e:
                    print(f"Database error: {e}")
                    QMessageBox.critical(None, "Error", f"Database error: {e}")
                finally:
                    cursor.close()
                    close_connection(connection)
            else:
                print("Failed to create database connection")
        else:
            QMessageBox.warning(None, "Error", "Please enter both username and password")

    def open_main_window(self, role):
        try:
            self.main_window = MainWindow(role)
            self.main_window.logout_signal.connect(self.show_login_form)
            print("Main window created and signal connected.")
            self.main_window.show()
            print("Main window shown.")
        except Exception as e:
            print(f"Error opening main window: {e}")
            QMessageBox.critical(None, "Error", f"Error opening main window: {e}")

    def open_registration_form(self):
        from registration_form import RegisterForm  # Đặt import ở đây để tránh import không cần thiết
        if not self.registration_form:
            self.registration_form = RegisterForm(login_form=self)
        self.registration_form.show()
        self.hide()  # Ẩn form đăng nhập khi form đăng ký được mở

    def show_login_form(self):
        if self.main_window:
            self.main_window.close()
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = LoginRegistrationForm()
    main_window.show()
    sys.exit(app.exec())
