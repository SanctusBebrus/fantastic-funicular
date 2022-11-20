import sys
import sqlite3
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class Espresso(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.show_info()

    def show_info(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['ИД', 'Сорт', 'Обжарка', 'Растворимость', 'Вкус', 'Цена', 'Объем'])
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)

        con = sqlite3.connect('coffee.sqlite.db')
        cur = con.cursor()

        result = cur.execute('''SELECT * FROM CoffeeInfo
                                WHERE id > 0''').fetchall()
        for en, res in enumerate(result[::-1]):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            self.add_to_table(en, res)

        con.close()

    def add_to_table(self, n, row):
        for num, elem in enumerate(row):
            self.tableWidget.setItem(n, num, QTableWidgetItem(str(elem)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fg = Espresso()
    fg.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
