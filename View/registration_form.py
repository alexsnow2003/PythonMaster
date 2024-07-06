import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from Entity.Database import create_connection, close_connection

class RegisterForm(QMainWindow):
    def __init__(self, login_form=None):
        super().__init__()
        self.login_form = login_form
        self.setupUi(self)

    def setupUi(self, MainWindow):
        self.setObjectName("MainWindow")
        self.resize(457, 428)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.username_input = QLineEdit(parent=self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(160, 100, 171, 31))
        self.username_input.setObjectName("username_input")

        self.password_input = QLineEdit(parent=self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(160, 160, 171, 31))
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setObjectName("password_input")

        self.confirm_password_input = QLineEdit(parent=self.centralwidget)
        self.confirm_password_input.setGeometry(QtCore.QRect(160, 210, 171, 31))
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input.setObjectName("confirm_password_input")

        self.register_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(170, 260, 131, 41))
        self.register_button.setObjectName("register_button")
        self.register_button.clicked.connect(self.register_user)

        self.login_button = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(240, 310, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.return_to_login)

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 61, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 61, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 320, 131, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 220, 101, 16))
        self.label_5.setObjectName("label_5")

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_input.setPlaceholderText(_translate("MainWindow", "Nhập username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.password_input.setPlaceholderText(_translate("MainWindow", "Nhập password"))
        self.register_button.setText(_translate("MainWindow", "Đăng ký"))
        self.login_button.setText(_translate("MainWindow", "Đăng nhập"))
        self.label.setText(_translate("MainWindow", "Register"))
        self.label_4.setText(_translate("MainWindow", "Bạn đã có tài khoản ? "))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.label_5.setText(_translate("MainWindow", "Confirm Password"))
        self.confirm_password_input.setPlaceholderText(_translate("MainWindow", "Confirm password"))

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
                        QMessageBox.information(None, "Registration Successful", "Registration completed successfully.")
                        self.close()
                        if self.login_form:
                            self.login_form.show()
                    except Exception as e:
                        QMessageBox.critical(None, "Error", f"Database error: {e}")
                    finally:
                        cursor.close()
                        close_connection(connection)
            else:
                QMessageBox.warning(None, "Error", "Passwords do not match.")
        else:
            QMessageBox.warning(None, "Error", "Please fill in all fields.")

    def return_to_login(self):
        self.close()
        if self.login_form:
            self.login_form.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = RegisterForm()
    main_window.show()
    sys.exit(app.exec())
