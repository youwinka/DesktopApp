from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

txt_title = 'Здоровье'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.bnt_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.bnt_next, alignment = Qt.AlignLeft)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.hide()
        self.fw = FinaWin()
    def connects(self):
        self.bnt_next.clicked.connect(self.next_click)