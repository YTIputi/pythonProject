from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsRotation
from PySide6.QtGui import QPixmap, QTransform
import sys, os, time
from plan2 import Ui_MainWindow
from PyQt6 import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('My App')
        self.images = os.listdir('IMAGES')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())