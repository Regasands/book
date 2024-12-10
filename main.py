from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRectF, QSize

from PyQt6 import uic
import sys


class A(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.b_1.clicked.connect(self.creats)
        self.b = False
    
    def creats(self):
        self.b = not self.b
        self.update()
    def paintEvent(self, event):
        if not self.b:
            return
        painter = QPainter(self)
        painter.setBrush(QColor('yellow'))
        painter.drawEllipse(200, 200, 30, 30)



if __name__ == '__main__':
    a = QApplication(sys.argv)
    e = A()
    e.show()
    sys.exit(a.exec())