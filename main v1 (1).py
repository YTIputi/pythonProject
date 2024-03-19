from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt6 import QtWidgets
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.res()
        self.flag = [0] * 3
        self.w, self.h = 500, 500
        self.setFixedSize(self.w, self.h)

        self.restart = QPushButton('Сброс', self)
        self.restart.move(int((self.w - self.restart.width()) * 0.5), 0)
        self.restart.clicked.connect(self.res)

        self.label1 = QLabel('Сделать что-то...', self)
        self.label1.move(int((self.w - self.label1.width()) * 0.5), int(self.h * 0.25))

        self.butt1_1, self.butt1_2 = QPushButton('За', self), QPushButton('Против', self)
        self.butt1_1.move(int((self.w - self.butt1_1.width()) * 0.25), int(self.h * 0.25))
        self.butt1_2.move(int((self.w - self.butt1_2.width()) * 0.75), int(self.h * 0.25))
        self.butt1_1.clicked.connect(self.data1)


        self.label2 = QLabel('Сделать что-то...', self)
        self.label2.move(int((self.w - self.label2.width()) * 0.5), int(self.h * 0.5))

        self.butt2_1, self.butt2_2 = QPushButton('За', self), QPushButton('Против', self)
        self.butt2_1.move(int((self.w - self.butt2_1.width()) * 0.25), int(self.h * 0.5))
        self.butt2_2.move(int((self.w - self.butt2_2.width()) * 0.75), int(self.h * 0.5))
        self.butt2_1.clicked.connect(self.data2)


        self.label3 = QLabel('Сделать что-то...', self)
        self.label3.move(int((self.w - self.label3.width()) * 0.5), int(self.h * 0.75))

        self.butt3_1, self.butt3_2 = QPushButton('За', self), QPushButton('Против', self)
        self.butt3_1.move(int((self.w - self.butt3_1.width()) * 0.25), int(self.h * 0.75))
        self.butt3_2.move(int((self.w - self.butt3_2.width()) * 0.75), int(self.h * 0.75))
        self.butt3_1.clicked.connect(self.data3)


    def data1(self):
        with open('data', 'a') as file:
            if not self.flag[0]:
                file.write('1 - За\n')
                self.flag[0] = 1
    def data2(self):
        with open('data', 'a') as file:
            if not self.flag[1]:
                file.write('2 - За\n')
                self.flag[1] = 1
    def data3(self):
        with open('data', 'a') as file:
            if not self.flag[2]:
                file.write('3 - За\n')
                self.flag[2] = 1

    def res(self):
        with open('data', 'w') as file:
            pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()