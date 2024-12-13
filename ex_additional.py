from PyQt6.QtWidgets import QWidget, QApplication,  QDialog, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QFont
from PyQt6 import uic
import sys
import sqlite3

class BookInfoDialog(QDialog):
    def __init__(self, dicters):
        super().__init__()
        self.setWindowTitle("Информация о книге")

        # Установка изображения
        image_label = QLabel()
        if dicters.get('img'):
            pixmap = QPixmap(dicters.get('img'))
        else:
            pixmap = QPixmap('image.png')
        image_label.setPixmap(pixmap)
        

        # Текстовые метки
        title_label = QLabel(f"Название\n{dicters['name']}")
        title_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))

        author_label = QLabel(f"Автор\n{dicters['author']}")
        author_label.setFont(QFont("Arial", 12))

        year_label = QLabel(f"Год выпуска\n{dicters['year']}")
        year_label.setFont(QFont("Arial", 12))

        genre_label = QLabel(f"Жанр\n{dicters['genre']}")
        genre_label.setFont(QFont("Arial", 12))

        # Размещение элементов в макете
        layout = QVBoxLayout()
        layout.addWidget(image_label)
        layout.addWidget(title_label)
        layout.addWidget(author_label)
        layout.addWidget(year_label)
        layout.addWidget(genre_label)
        self.setLayout(layout)


class Book(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('12.ui', self)
        # Создаём элемент списка
        # list_item = QListWidgetItem(self.listWidget)  # Создаём элемент
        # button = QPushButton("F", self)  # Создаём кнопку
        # button.clicked.connect(self.find_book)
        self.dic = {}
        self.con = sqlite3.connect('database.sql')
        self.cur = self.con.cursor()
        self.listWidget.itemClicked.connect(self.show_m)
        self.find_2.clicked.connect(self.find_book)

        # self.listWidget.setItemWidget(list_item, button)  # До
    def show_m(self, item):
        book = item.text()
        dial = BookInfoDialog(self.dic[book])
        dial.exec()
    def find_book(self):
        self.listWidget.clear()
        self.dic = {}
        fild = self.find.currentText()
        text = self.fileds.text()
        print('yes', fild, text)
        if fild == 'Автор':
            self.cur.execute('''SELECT * FROM BOOK''')
            res = list(filter(lambda x: text in x[2], self.cur.fetchall()))
        else:
            self.cur.execute('''SELECT * FROM BOOK''')
            res = list(filter(lambda x: text in x[1], self.cur.fetchall()))
        print(res)
        for e in res:
            dicters = {'name': e[1], 'author': e[2], 'year': e[3], 'genre': e[4], 'img': e[5]}
            self.dic[e[1]] = dicters
        for key in self.dic:
            self.listWidget.addItem(key)


if __name__ == '__main__':
    a = QApplication(sys.argv)
    e = Book()
    e.show()
    sys.exit(a.exec())