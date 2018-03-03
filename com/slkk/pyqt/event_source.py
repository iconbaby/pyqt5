#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI();

    def initUI(self):
        btn1 = QPushButton('Btn 1', self)
        btn1.move(50, 100)

        btn2 = QPushButton('Btn 2', self)
        btn2.move(200, 100)

        btn1.clicked.connect(self.btnClicked)
        btn2.clicked.connect(self.btnClicked)

        self.statusBar()
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('absolute ')
        self.show()

    def btnClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + "was pressed")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
