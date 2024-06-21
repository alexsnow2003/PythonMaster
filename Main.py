from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from View.Sidebar import MySidebar

app = QApplication(sys.argv)

window = MySidebar()
window.show()
app.exec_()