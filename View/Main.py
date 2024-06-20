from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Sidebar import MySidebar

app = QApplication(sys.argv)

window = MySidebar()
window.show()
app.exec_()