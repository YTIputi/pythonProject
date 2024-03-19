from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6 import QtWidgets
from random import randint
import sys, os


# 1
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.f, self.s = 0, 0
        if not os.path.isfile('res.txt'):
            with open('res.txt', 'w') as file:
                file.write(f'0 0')
        else:
            with open('res.txt') as file:
                self.f, self.s = map(int, file.readline().split())
        self.setWindowTitle('My App')
        self.setFixedSize(300, 300)
        self.label = QtWidgets.QLabel("Сделать что-то", self)
        self.label.move((300 - self.label.width()) // 2, 0)

        self.yes = QtWidgets.QPushButton("За", self)
        self.yes.move((300 - self.yes.width()) // 4, self.label.height())
        self.yes_text = QtWidgets.QLabel(f"{self.f}", self)
        self.yes_text.move((300 - self.yes.width()) // 4, self.label.height() * 2)
        self.yes.clicked.connect(self.s_yes)

        self.no = QtWidgets.QPushButton("Против", self)
        self.no.move((300 - self.no.width()) // 4 * 3, self.label.height())
        self.no_text = QtWidgets.QLabel(f"{self.s}", self)
        self.no_text.move((300 - self.no.width()) // 4 * 3, self.label.height() * 2)
        self.no.clicked.connect(self.s_no)

        self.rest = QtWidgets.QPushButton("Сброс", self)
        self.rest.move((300 - self.label.width()) // 2, (300 - self.label.height()) // 2)
        self.rest.clicked.connect(self.restart)

    def s_yes(self):
        self.yes_text.setText(str(int(self.yes_text.text()) + 1))
        with open('res.txt') as file:
            self.f, self.s = map(int, file.readline().split())
            self.f += 1
        with open('res.txt', 'w') as file:
            file.write(f'{self.f} {self.s}')

    def s_no(self):
        self.no_text.setText(str(int(self.no_text.text()) + 1))
        with open('res.txt') as file:
            self.f, self.s = map(int, file.readline().split())
            self.s += 1
        with open('res.txt', 'w') as file:
            file.write(f'{self.f} {self.s}')

    def restart(self):
        self.f, self.s = 0, 0
        with open('res.txt', 'w') as file:
            file.write(f'{self.f} {self.s}')
        self.yes_text.setText(f'{self.f}')
        self.no_text.setText(f'{self.s}')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
