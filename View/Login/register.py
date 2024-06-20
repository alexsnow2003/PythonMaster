from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from Entity.Database import Database
from Icon.Ui_Sidebar import Ui_MainWindow
from View.Login.loginUi4 import Ui_Form

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 650)  # Tăng kích thước Form để có thêm không gian
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 40, 420, 560))  # Điều chỉnh kích thước widget chính

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 420, 560))  # Điều chỉnh kích thước nền
        self.label.setStyleSheet("border-image: url('background.png');\nborder-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 360, 500))  # Điều chỉnh kích thước nền bên trong
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\nborder-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 320, 460))  # Điều chỉnh kích thước nền bên trong cùng
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\nborder-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(165, 95, 90, 40))  # Điều chỉnh vị trí tiêu đề
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 165, 200, 40))  # Điều chỉnh vị trí trường tên đăng nhập
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 220, 200, 40))  # Điều chỉnh vị trí trường mật khẩu
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 275, 200, 40))  # Điều chỉnh vị trí trường xác nhận mật khẩu
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.first_name_input = QtWidgets.QLineEdit(self.widget)
        self.first_name_input.setGeometry(QtCore.QRect(110, 330, 200, 40))  # Điều chỉnh vị trí trường tên
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_name_input.setFont(font)
        self.first_name_input.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.first_name_input.setPlaceholderText("  First Name")
        self.first_name_input.setObjectName("first_name_input")

        self.last_name_input = QtWidgets.QLineEdit(self.widget)
        self.last_name_input.setGeometry(QtCore.QRect(110, 385, 200, 40))  # Điều chỉnh vị trí trường họ
        font = QtGui.QFont()
        font.setPointSize(10)
        self.last_name_input.setFont(font)
        self.last_name_input.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.last_name_input.setPlaceholderText("  Last Name")
        self.last_name_input.setObjectName("last_name_input")

        self.role_id_input = QtWidgets.QSpinBox(self.widget)
        self.role_id_input.setGeometry(QtCore.QRect(110, 440, 200, 40))  # Điều chỉnh vị trí trường vai trò
        font = QtGui.QFont()
        font.setPointSize(10)
        self.role_id_input.setFont(font)
        self.role_id_input.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.role_id_input.setMinimum(1)
        self.role_id_input.setObjectName("role_id_input")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(110, 495, 200, 40))  # Điều chỉnh vị trí nút đăng ký
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.register)

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                         color=QtGui.QColor(234, 221, 186, 100)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                           color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3,
                                                                              color=QtGui.QColor(105, 118, 132, 100)))

        self.show_connection_status()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_connection_status(self):
        self.db = Database()
        status_message = self.db.connection_status

        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText(status_message)
        msg_box.setWindowTitle("Trạng thái kết nối cơ sở dữ liệu")
        msg_box.exec()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Sign Up"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", " Confirm Password"))
        self.first_name_input.setPlaceholderText(_translate("Form", "  First Name"))
        self.last_name_input.setPlaceholderText(_translate("Form", "  Last Name"))
        self.pushButton.setText(_translate("Form", "S I G N U P"))

    def register(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm_password = self.lineEdit_3.text()
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        role_id = self.role_id_input.value()

        if password != confirm_password:
            QtWidgets.QMessageBox.warning(None, "Registration Failed", "Passwords do not match.")
            return

        if self.db.register_user(username, password, first_name, last_name, role_id):
            QtWidgets.QMessageBox.information(None, "Registration Successful", f"Welcome, {username}!")
            self.open_login_form()
        else:
            QtWidgets.QMessageBox.warning(None, "Registration Failed",
                                          "Username already exists or registration failed.")

    def open_login_form(self):
        self.login_form = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.login_form)
        self.login_form.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def open_sidebar(self):
        self.sidebar_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.sidebar_window)
        self.sidebar_window.show()
        QtWidgets.QApplication.instance().activeWindow().close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
