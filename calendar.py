import sys, os
from datetime import date
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled2.ui', self)
        self.setFixedSize(800, 600)
        self.save = []

        if not os.path.isfile('Save'):
            with open('Save', 'w') as file:
                pass

        self.pushButton.clicked.connect(self.add_event)
        self.pushButton_3.clicked.connect(self.edit_event)
        self.pushButton_2.clicked.connect(self.remove_event)
        self.pushButton_4.clicked.connect(self.add_save)
        self.pushButton_5.clicked.connect(self.unpack)

    def add_event(self):
        date0 = self.calendarWidget.selectedDate().getDate()
        date1 = date(date0[0], date0[1], date0[2])
        current_index = self.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, 'Добавить данные', 'Название данных')
        if ok and text is not None:
            text = f'{date1} {text}'
            self.save.append(text)
            self.listWidget.insertItem(current_index, text)
        self.listWidget.sortItems()
    def edit_event(self):
        date0 = self.calendarWidget.selectedDate().getDate()
        date1 = date(date0[0], date0[1], date0[2])
        current_index = self.listWidget.currentRow()
        item = self.listWidget.item(current_index)
        if item is not None:
            text, ok = QInputDialog.getText(self, 'Редактировать данные', 'Название данных')
            if ok and text is not None:
                self.save.remove(item.text())
                self.save.append(f'{date1} {text}')
                item.setText(f'{date1} {text}')

    def remove_event(self):
        current_index = self.listWidget.currentRow()
        item = self.listWidget.item(current_index)
        if item is None:
            return
        question = QMessageBox.question(self, 'Удалить данные',
                                        'Вы хотите удалить данные? ' + item.text(),
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if question == QMessageBox.StandardButton.Yes:
            self.save.remove(item.text())
            item = self.listWidget.takeItem(current_index)
            del item

    def add_save(self):
        with open('Save', 'a') as file:
            for event in self.save:
                file.write(event + '\n')

    def unpack(self):
        data = []
        current_index = self.listWidget.currentRow()
        with open('Save') as file:
            for event in file:
                self.listWidget.insertItem(current_index, event[:-1])
        self.listWidget.sortItems()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())