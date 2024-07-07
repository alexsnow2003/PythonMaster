from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(721, 601)
        MainWindow.setStyleSheet("background-color: rgb(199, 200, 133);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtID = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtID.setGeometry(QtCore.QRect(190, 120, 321, 31))
        self.txtID.setStyleSheet("background-color: rgb(206, 255, 255);")
        self.txtID.setObjectName("txtID")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 30, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btCapNhat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btCapNhat.setGeometry(QtCore.QRect(190, 480, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btCapNhat.setFont(font)
        self.btCapNhat.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btCapNhat.setObjectName("btCapNhat")
        self.txtMoTa = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtMoTa.setGeometry(QtCore.QRect(190, 220, 321, 141))
        self.txtMoTa.setStyleSheet("background-color: rgb(206, 255, 255);")
        self.txtMoTa.setObjectName("txtMoTa")
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
        self.txtGia = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtGia.setGeometry(QtCore.QRect(190, 380, 321, 31))
        self.txtGia.setStyleSheet("background-color: rgb(206, 255, 255);")
        self.txtGia.setObjectName("txtGia")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 380, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtTen = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtTen.setGeometry(QtCore.QRect(190, 170, 321, 31))
        self.txtTen.setStyleSheet("background-color:rgb(206, 255, 255);")
        self.txtTen.setObjectName("txtTen")
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
        self.txtDvt = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txtDvt.setGeometry(QtCore.QRect(190, 430, 321, 31))
        self.txtDvt.setStyleSheet("background-color: rgb(206, 255, 255);")
        self.txtDvt.setObjectName("txtDvt")
        self.btThoat = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btThoat.setGeometry(QtCore.QRect(390, 480, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btThoat.setFont(font)
        self.btThoat.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btThoat.setObjectName("btThoat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btCapNhat.clicked.connect(self.update_data)
        self.btThoat.clicked.connect(self.open_form_dv)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtID.setPlaceholderText(_translate("MainWindow", "Nhập ID"))
        self.label.setText(_translate("MainWindow", "Sửa Dịch Vụ"))
        self.btCapNhat.setText(_translate("MainWindow", "Cập Nhật"))
        self.txtMoTa.setPlaceholderText(_translate("MainWindow", "Nhập ......"))
        self.label_3.setText(_translate("MainWindow", "Mô Tả Dịch Vụ :"))
        self.label_2.setText(_translate("MainWindow", "ID Dịch Vụ :"))
        self.txtGia.setPlaceholderText(_translate("MainWindow", "VND"))
        self.label_4.setText(_translate("MainWindow", "Giá :"))
        self.txtTen.setPlaceholderText(_translate("MainWindow", "Nhập Tên Dịch Vụ"))
        self.label_5.setText(_translate("MainWindow", "Tên :"))
        self.label_6.setText(_translate("MainWindow", "Đơn vị tính:"))
        self.txtDvt.setPlaceholderText(_translate("MainWindow", "..."))
        self.btThoat.setText(_translate("MainWindow", "Thoát"))

    def update_data(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='phuc123',
                database='qlks'
            )

            if connection.is_connected():
                cursor = connection.cursor()

                # Retrieve data from UI
                ma_dv = self.txtID.toPlainText().strip()
                ten_dv = self.txtTen.toPlainText().strip()
                mo_ta = self.txtMoTa.toPlainText().strip()
                gia = self.txtGia.toPlainText().strip()
                dvt = self.txtDvt.toPlainText().strip()

                # Validate input
                if not (ma_dv and ten_dv and mo_ta and gia and dvt):
                    QtWidgets.QMessageBox.critical(None, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
                    return

                # Update database
                update_query = """
                    UPDATE DichVu 
                    SET TenDV = %s, MoTa = %s, DonGia = %s, Dvt = %s
                    WHERE MaDV = %s
                """
                data = (ten_dv, mo_ta, gia, dvt, ma_dv)
                cursor.execute(update_query, data)
                connection.commit()

                QtWidgets.QMessageBox.information(None, "Thông báo", "Cập nhật dịch vụ thành công.")

        except Error as e:
            print("Lỗi khi cập nhật dịch vụ:", e)
            QtWidgets.QMessageBox.critical(None, "Lỗi", "Không thể cập nhật dịch vụ.")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def open_form_dv(self):

        from form_dv import Ui_MainWindow as Formdv_MainWindow  # Import lại form danh sách dịch vụ
        self.window = QtWidgets.QMainWindow()
        self.ui = Formdv_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
