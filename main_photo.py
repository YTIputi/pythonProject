from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QApplication, QWidget, QDialog, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys, os


class HelloWindow(QMainWindow):
    def __init__(self):
        super(HelloWindow, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Hello window')

        font = QFont(os.path.join('font', 'Droid Sans Mono.ttf'), 30)
        self.setFont(font)

        central_widget = QWidget()
        layout = QVBoxLayout()

        label = QLabel('Hello')
        label.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        button = QPushButton('Register')
        font = QFont(os.path.join('font', 'Droid Sans Mono.ttf'), 10)
        button.setFont(font)
        button.clicked.connect(self.reg)

        layout.addWidget(label)
        layout.addWidget(button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def reg(self):
        e2.show()
        self.close()


class RegisterWindow (QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.setWindowTitle('Register window')

        font = QFont(os.path.join('font', 'Droid Sans Mono.ttf'), 10)
        self.setFont(font)

        central_widget = QWidget()
        layout = QVBoxLayout()

        layout1 = QHBoxLayout()

        login0 = QLabel('Ваш логин')

        self.login = QLineEdit()
        self.login.setPlaceholderText('Введите логин')

        self.login_text = QLabel()

        layout.addWidget(login0)
        layout1.addWidget(self.login)
        layout1.addWidget(self.login_text)

        layout.addLayout(layout1)

        layout2 = QHBoxLayout()

        password0 = QLabel('Ваш пароль')

        self.password = QLineEdit()
        self.password.setPlaceholderText('Введите пароль')

        self.password_text = QLabel()

        layout.addWidget(password0)
        layout2.addWidget(self.password)
        layout2.addWidget(self.password_text)

        layout.addLayout(layout2)

        layout3 = QHBoxLayout()

        self.repeat_password = QLineEdit()
        self.repeat_password.setPlaceholderText('Введите пароль повторно')

        self.repeat_password_text = QLabel()

        layout3.addWidget(self.repeat_password)
        layout3.addWidget(self.repeat_password_text)

        layout.addLayout(layout3)

        layout4 = QHBoxLayout()

        email0 = QLabel('Ваша электронная почта')

        self.email = QLineEdit()
        self.email.setPlaceholderText('Введите электронную почту')

        self.email_text = QLabel()

        layout.addWidget(email0)
        layout4.addWidget(self.email)
        layout4.addWidget(self.email_text)

        layout.addLayout(layout4)

        layout5 = QHBoxLayout()

        num0 = QLabel('Ваш номер телефона')

        self.num = QLineEdit()
        self.num.setPlaceholderText('Введите номер телефона')

        self.num_text = QLabel()

        layout.addWidget(num0)
        layout5.addWidget(self.num)
        layout5.addWidget(self.num_text)

        layout.addLayout(layout5)

        layout6 = QHBoxLayout()

        name0 = QLabel('Ваш ФИО')

        self.name = QLineEdit()

        layout6.addWidget(name0)
        layout6.addWidget(self.name)

        layout.addLayout(layout6)

        layout7 = QHBoxLayout()

        city0 = QLabel('Ваш город')

        self.city = QLineEdit()

        layout7.addWidget(city0)
        layout7.addWidget(self.city)

        layout.addLayout(layout7)

        layout8 = QHBoxLayout()

        about0 = QLabel('О себе')

        self.about = QLineEdit()
        self.about.setPlaceholderText('')

        layout8.addWidget(about0)
        layout8.addWidget(self.about)

        layout.addLayout(layout8)

        central_widget.setLayout(layout)

        self.button = QPushButton('Отправить')
        layout.addWidget(self.button)

        self.setCentralWidget(central_widget)

        self.login.returnPressed.connect(self.log_text)
        # self.password.textEdited.connect()
        # self.repeat_password.textEdited.connect()
        # self.email.textEdited.connect()
        # self.num.textEdited.connect()
        # self.name.textEdited.connect()
        # self.city.textEdited.connect()
        # self.about.textEdited.connect()

    def log_text(self):
        print(self.login.text())


app = QApplication([])
e1 = HelloWindow()
e2 = RegisterWindow()
e1.show()
app.exec()