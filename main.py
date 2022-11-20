import sys
import sqlite3
from PyQt5 import uic

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class Cappuccino(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.add_func()
        self.show_info()

    def add_func(self):
        self.add_btn.clicked.connect(self.add_film)

    def add_film(self):
        add_dial = Adding_Dialog(self)
        add_dial.exec()
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


class Adding_Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.add_func()

    def add_func(self):
        self.pushButton.clicked.connect(self.add_to_db)

    def add_to_db(self):
        _id = self.lineEdit_7.text()
        _type = self.lineEdit_6.text()
        roast_level = self.lineEdit_5.text()
        solubility = self.lineEdit_4.text()

        taste = self.lineEdit_3.text()
        price = self.lineEdit_2.text()
        size = self.lineEdit.text()
        if not _type or not roast_level or not solubility or not _id or \
                not taste or not price or not size:
            msg = QtWidgets.QMessageBox()
            msg.about(self, 'Ошибка', 'Неверно заполнена форма')
            return False
        try:
            _id = int(_id)
            price = int(price)
            size = int(size)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.about(self, 'Ошибка', 'Неверно заполнена форма')
            return False

        con = sqlite3.connect('coffee.sqlite.db')
        cur = con.cursor()
        cur.execute(f'''INSERT INTO CoffeeInfo (id, type, roast_level, 
        solubility, taste, price, size)
        VALUES ({_id}, "{_type}", "{roast_level}", "{solubility}", "{taste}", 
                    {price}, {size})''')

        con.commit()
        cur.close()

        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fg = Cappuccino()
    fg.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
