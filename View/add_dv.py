from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, form_dv_window=None):
        self.form_dv_window = form_dv_window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 601)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtaddID = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtaddID.setGeometry(QtCore.QRect(190, 120, 321, 31))
        self.txtaddID.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.txtaddID.setObjectName("txtaddID")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.txtaddCapNhat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.txtaddCapNhat.setGeometry(QtCore.QRect(180, 480, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtaddCapNhat.setFont(font)
        self.txtaddCapNhat.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.txtaddCapNhat.setObjectName("txtaddCapNhat")
        self.txtaddMoTa = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtaddMoTa.setGeometry(QtCore.QRect(190, 220, 321, 141))
        self.txtaddMoTa.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.txtaddMoTa.setObjectName("txtaddMoTa")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.txtaddGia = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtaddGia.setGeometry(QtCore.QRect(190, 380, 321, 31))
        self.txtaddGia.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.txtaddGia.setObjectName("txtaddGia")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtaddTen = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtaddTen.setGeometry(QtCore.QRect(190, 170, 321, 31))
        self.txtaddTen.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.txtaddTen.setObjectName("txtaddTen")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 430, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtaddGia_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtaddGia_2.setGeometry(QtCore.QRect(190, 430, 321, 31))
        self.txtaddGia_2.setStyleSheet("background-color: rgb(85, 255, 0);")
        self.txtaddGia_2.setObjectName("txtaddGia_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Thêm nút thoát
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(400, 480, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btnExit.setObjectName("btnExit")
        self.btnExit.setText("Thoát")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect button click to the method
        self.txtaddCapNhat.clicked.connect(self.add_service)
        self.btnExit.clicked.connect(lambda: self.open_form_dv(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtaddID.setPlaceholderText(_translate("MainWindow", "Nhập ID"))
        self.label.setText(_translate("MainWindow", "Thêm Dịch Vụ"))
        self.txtaddCapNhat.setText(_translate("MainWindow", "Cập Nhật"))
        self.txtaddMoTa.setPlaceholderText(_translate("MainWindow", "Nhập ......"))
        self.label_3.setText(_translate("MainWindow", "Mô Tả Dịch Vụ :"))
        self.label_2.setText(_translate("MainWindow", "ID Dịch Vụ :"))
        self.txtaddGia.setPlaceholderText(_translate("MainWindow", "VND"))
        self.label_4.setText(_translate("MainWindow", "Giá :"))
        self.txtaddTen.setPlaceholderText(_translate("MainWindow", "Nhập Tên Dịch Vụ"))
        self.label_5.setText(_translate("MainWindow", "Tên :"))
        self.label_6.setText(_translate("MainWindow", "Đơn vị tính:"))
        self.txtaddGia_2.setPlaceholderText(_translate("MainWindow", "..."))

    def add_service(self):
        ma_dv = self.txtaddID.toPlainText()
        ten_dv = self.txtaddTen.toPlainText()
        mo_ta = self.txtaddMoTa.toPlainText()
        gia = self.txtaddGia.toPlainText()
        dvt = self.txtaddGia_2.toPlainText()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # Thay bằng username của bạn
                password='phuc123',  # Thay bằng password của bạn
                database='qlks'  # Tên cơ sở dữ liệu đã tạo
            )

            if connection.is_connected():
                cursor = connection.cursor()
                query = "INSERT INTO DichVu (MaDV,TenDV, DonGia, Dvt, MoTa) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, (ma_dv, ten_dv, gia, dvt, mo_ta))
                connection.commit()
                QtWidgets.QMessageBox.information(None, 'Thông báo', 'Dịch vụ đã được thêm thành công!')

        except Error as e:
            QtWidgets.QMessageBox.critical(None, 'Error', f"Lỗi khi thêm dịch vụ: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def open_form_dv(self, MainWindow):
        if self.form_dv_window is None or not self.form_dv_window.isVisible():
            from form_dv import Ui_MainWindow as Formdv_MainWindow  # Import lại form danh sách dịch vụ
            self.form_dv_window = QtWidgets.QMainWindow()
            self.ui = Formdv_MainWindow()
            self.ui.setupUi(self.form_dv_window)
            self.form_dv_window.show()
        MainWindow.close()  # Đóng cửa sổ add_dv hiện tại


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    form_dv_window = None
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, form_dv_window)
    MainWindow.show()
    sys.exit(app.exec())
