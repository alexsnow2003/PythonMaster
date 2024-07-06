from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
import mysql.connector
from mysql.connector import Error

class RevenueManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quản lý doanh thu")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()
        self.revenue_label = QLabel("Doanh thu của khách sạn")
        self.revenue_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #333;")
        main_layout.addWidget(self.revenue_label)

        self.revenue_table = QTableWidget()
        self.revenue_table.setColumnCount(2)
        self.revenue_table.setHorizontalHeaderLabels(['Ngày', 'Doanh thu (VND)'])
        self.revenue_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        main_layout.addWidget(self.revenue_table)

        self.load_revenue_button = QPushButton("Tải doanh thu")
        self.load_revenue_button.clicked.connect(self.load_revenue)
        self.load_revenue_button.setStyleSheet(
            "font-size: 16px; padding: 12px; background-color: #0275d8; color: white; border: none; border-radius: 8px;")
        main_layout.addWidget(self.load_revenue_button)

        self.central_widget.setLayout(main_layout)

        self.setStyleSheet("""
            QLabel {
                font-size: 18px;
                margin-bottom: 16px;
            }
            QPushButton {
                font-size: 18px;
                padding: 15px;
                background-color: #0275d8;
                color: white;
                border: none;
                border-radius: 8px;
                margin-bottom: 12px;
            }
            QPushButton:hover {
                background-color: #025aa5;
            }
            QPushButton:pressed {
                background-color: #014682;
            }
        """)

    def load_revenue(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                database='QLKS',
                user='root',
                password='123456'
            )
            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                cursor.execute(
                    "SELECT DATE(P.NgayDatPhong) AS Ngay, SUM(D.DonGia) AS DoanhThu "
                    "FROM PhieuDangKy P "
                    "INNER JOIN HoaDon D ON P.MaPDK = D.MaPDK "
                    "GROUP BY DATE(P.NgayDatPhong) "
                    "ORDER BY DATE(P.NgayDatPhong)"
                )
                revenue_data = cursor.fetchall()
                self.display_revenue(revenue_data)
                cursor.close()
        except Error as e:
            print(f"Error loading revenue: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                connection.close()

    def display_revenue(self, revenue_data):
        self.revenue_table.setRowCount(len(revenue_data))
        for row, data in enumerate(revenue_data):
            self.revenue_table.setItem(row, 0, QTableWidgetItem(data['Ngay'].strftime('%Y-%m-%d')))
            self.revenue_table.setItem(row, 1, QTableWidgetItem(f"{data['DoanhThu']:.0f} VND"))
