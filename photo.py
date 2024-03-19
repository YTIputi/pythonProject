# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'photo.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.image = QLabel(self.centralwidget)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(50, 50, 700, 700))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 780, 721, 61))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.delete_2 = QPushButton(self.widget)
        self.delete_2.setObjectName(u"delete_2")

        self.horizontalLayout.addWidget(self.delete_2)

        self.left1 = QPushButton(self.widget)
        self.left1.setObjectName(u"left1")

        self.horizontalLayout.addWidget(self.left1)

        self.right1 = QPushButton(self.widget)
        self.right1.setObjectName(u"right1")

        self.horizontalLayout.addWidget(self.right1)

        self.timesleep = QPushButton(self.widget)
        self.timesleep.setObjectName(u"timesleep")

        self.horizontalLayout.addWidget(self.timesleep)

        self.first = QPushButton(self.widget)
        self.first.setObjectName(u"first")

        self.horizontalLayout.addWidget(self.first)

        self.last = QPushButton(self.widget)
        self.last.setObjectName(u"last")

        self.horizontalLayout.addWidget(self.last)

        self.left = QPushButton(self.widget)
        self.left.setObjectName(u"left")

        self.horizontalLayout.addWidget(self.left)

        self.right = QPushButton(self.widget)
        self.right.setObjectName(u"right")

        self.horizontalLayout.addWidget(self.right)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.left1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.right1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.timesleep.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0430\u0439\u0434-\u0448\u043e\u0443", None))
        self.first.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043d\u0430\u0447\u0430\u043b\u043e", None))
        self.last.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043a\u043e\u043d\u0435\u0446", None))
        self.left.setText(QCoreApplication.translate("MainWindow", u"<=", None))
        self.right.setText(QCoreApplication.translate("MainWindow", u"=>", None))
    # retranslateUi

