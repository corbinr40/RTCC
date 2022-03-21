from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys

x = 490
y = 426
w = 163
h = 163

# It is considered a good tone to name classes in CamelCase.
class MyFirstGUI(QMainWindow): 

    def __init__(self):
        # Initializing QDialog and locking the size at a certain value
        super(MyFirstGUI, self).__init__()
        self.setWindowTitle("Face Location")
        #self.setFixedSize(640, 480)
        #self.setFixedSize(480, 640)
        #self.setWindowOpacity(0.1)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.showFullScreen()

    def paintEvent(self, e):
        # Draw Rectangle
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        #painter.drawRect(490, 426, 635, 571)
        #painter.drawRect(490, 426, 163, 163)
        painter.drawRect(x, y, w, h)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MyFirstGUI()
    gui.show()
    sys.exit(app.exec_())
