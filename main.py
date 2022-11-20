import sys
import sqlite3
from PyQt5 import uic

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 369)
        Dialog.setMinimumSize(QtCore.QSize(454, 369))
        Dialog.setMaximumSize(QtCore.QSize(454, 369))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 0, 251, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 10, 101, 311))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_7.setText(_translate("Dialog", "ИД"))
        self.label_6.setText(_translate("Dialog", "Сорт"))
        self.label_5.setText(_translate("Dialog", "Обжарка"))
        self.label_4.setText(_translate("Dialog", "Растворимость"))
        self.label_3.setText(_translate("Dialog", "Вкус"))
        self.label_2.setText(_translate("Dialog", "Цена"))
        self.label.setText(_translate("Dialog", "Объем"))
        self.pushButton.setText(_translate("Dialog", "Ок"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 368)
        MainWindow.setMinimumSize(QtCore.QSize(997, 368))
        MainWindow.setMaximumSize(QtCore.QSize(997, 368))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1001, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(0, 270, 93, 28))
        self.add_btn.setObjectName("add_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Espresso"))
        self.add_btn.setText(_translate("MainWindow", "Добавить"))


class LatteMacchiato(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        con = sqlite3.connect('data/coffee.sqlite.db')
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


class Adding_Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
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

        con = sqlite3.connect('data/coffee.sqlite.db')
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
    fg = LatteMacchiato()
    fg.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
