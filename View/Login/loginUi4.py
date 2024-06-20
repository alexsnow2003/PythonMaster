from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from Entity.Database import Database
from Icon.Ui_Sidebar import Ui_MainWindow  # Ensure this module is available


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 370, 480))

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 370, 480))
        self.label.setStyleSheet("border-image: url('background.png');\nborder-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\nborder-radius:20px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 280, 390))
        self.label_3.setStyleSheet("background-color:rgba(0, 0, 0, 100);\nborder-radius:15px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(135, 95, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 165, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 230, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
            "background-color:rgba(0, 0, 0, 0);\nborder:none;\nborder-bottom:2px solid rgba(105, 118, 132, 255);\ncolor:rgba(255, 255, 255, 230);\npadding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)

        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(91, 358, 191, 21))
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 140);")
        self.label_5.setObjectName("label_5")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(105, 399, 141, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                         color=QtGui.QColor(234, 221, 186, 100)))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                           color=QtGui.QColor(105, 118, 132, 100)))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3,
                                                                              color=QtGui.QColor(105, 118, 132, 100)))
        # Show connection status
        self.show_connection_status()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_connection_status(self):
        self.db = Database()
        status_message = self.db.connection_status

        # Display the connection status in a message box
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg_box.setText(status_message)
        msg_box.setWindowTitle("Database Connection Status")
        msg_box.exec()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.label_5.setText(_translate("Form", "Forgot your User Name or Password? "))
        self.pushButton_2.setText(_translate("Form", "S"))
        self.pushButton_3.setText(_translate("Form", "N"))
        self.pushButton_4.setText(_translate("Form", "O"))
        self.pushButton_5.setText(_translate("Form", "W"))

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        role = self.db.login_user(username, password)
        if role:
            QtWidgets.QMessageBox.information(None, "Login Successful", f"Welcome, {role}!")
            self.open_sidebar()

        else:
            QtWidgets.QMessageBox.warning(None, "Login Failed", "Invalid username or password.")

    def open_sidebar(self):
        self.sidebar_window = QtWidgets.QMainWindow()  # Changed to QMainWindow for a full application window
        self.ui = Ui_MainWindow()  # Assuming Ui_MainWindow is the correct class name in Ui_Sidebar module
        self.ui.setupUi(self.sidebar_window)
        self.sidebar_window.show()
        # Close the login form
        QtWidgets.QApplication.instance().activeWindow().close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
