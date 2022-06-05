# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGroupBox, QRadioButton, QListWidget, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
class Main_Window(QWidget):
    def __init__():
        super().__init__()
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Rufier's test")
vertical = QVBoxLayout()
text1 = QLabel('текст, много текста')
text2 = QLabel('текст, много текста, очень много текста, люблю текст, прям вообще жить без текста не могу, дайте текст, ещё больше текста')
button = QPushButton('Приступить')
vertical.addWidget(text1, alignment = Qt.AlignLeft)
vertical.addWidget(text2, alignment = Qt.AlignLeft)
vertical.addWidget(button, alignment = Qt.AlignCenter)
main_window.setLayout(vertical)
main_window.show()
app.exec_()
