from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsRotation
from PySide6.QtGui import QPixmap, QTransform
import sys, os, time
from photo import Ui_MainWindow
from PyQt6 import QtCore



# 1
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('My App')
        self.images = os.listdir('IMAGES')
        self.now = 0
        self.rotation = 0

        self.image = self.ui.image
        self.pixmap = QPixmap(os.path.join('IMAGES', self.images[self.now]))
        self.image.setPixmap(self.pixmap)

        self.ui.right.clicked.connect(self.right)
        self.ui.left.clicked.connect(self.left)
        self.ui.last.clicked.connect(self.last)
        self.ui.first.clicked.connect(self.first)
        self.ui.timesleep.clicked.connect(self.timesleep)
        self.ui.delete_2.clicked.connect(self.delete_2)
        self.ui.right1.clicked.connect(self.right1)
        self.ui.left1.clicked.connect(self.left1)


    def right(self):
        self.now = min(self.now + 1, len(self.images) - 1)
        self.pixmap = QPixmap(os.path.join('IMAGES', self.images[self.now]))
        self.image.setPixmap(self.pixmap)
    def left(self):
        self.now = max(self.now - 1, 0)
        self.pixmap = QPixmap(os.path.join('IMAGES', self.images[self.now]))
        self.image.setPixmap(self.pixmap)

    def last(self):
        self.now = len(self.images) - 1
        self.pixmap = QPixmap(os.path.join('IMAGES', self.images[self.now]))
        self.image.setPixmap(self.pixmap)
    def first(self):
        self.now = 0
        self.pixmap = QPixmap(os.path.join('IMAGES', self.images[self.now]))
        self.image.setPixmap(self.pixmap)

    def timesleep(self):

        self.pixmap = QPixmap(os.path.join('IMAGES', self.images[i]))
        self.image.setPixmap(self.pixmap)

    def right1(self):
        pixmap = QPixmap(self.images[self.now])
        self.rotation += 1
        transform = QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform)
        self.image.setPixmap(pixmap)
    def left1(self):
        pixmap = QPixmap(self.images[self.now])
        self.rotation -= 1
        transform = QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform)
        self.image.setPixmap(pixmap)

    def delete_2(self):
        if self.now == 0 and len(self.images) > 1:
            self.now += 1
            self.pixmap = QPixmap(os.path.join('IMAGES', self.images[self.now]))
            self.image.setPixmap(self.pixmap)
            self.images.pop(self.now - 1)
        elif len(self.images) > 1:
            self.now -= 1
            self.pixmap = QPixmap(os.path.join('IMAGES', self.images[self.now]))
            self.image.setPixmap(self.pixmap)
            self.images.pop(self.now + 1)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
