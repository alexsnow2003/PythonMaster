from Icon.Ui_Sidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication
from PyQt6 import QtWidgets


class MySidebar(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MySidebar, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboard)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard)

        self.prolife_1.clicked.connect(self.switch_to_prolife)
        self.prolife_2.clicked.connect(self.switch_to_prolife)

        self.room_1.clicked.connect(self.switch_to_room)
        self.room_2.clicked.connect(self.switch_to_room)

        self.booking_1.clicked.connect(self.switch_to_booking)
        self.booking_2.clicked.connect(self.switch_to_booking)

        self.checkout_1.clicked.connect(self.switch_to_checkout)
        self.checkout_2.clicked.connect(self.switch_to_checkout)

        self.customer_1.clicked.connect(self.switch_to_customer)
        self.customer_2.clicked.connect(self.switch_to_customer)

    def switch_to_dashboard(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_prolife(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_room(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MySidebar()
    window.show()
    sys.exit(app.exec())