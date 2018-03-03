#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI();

    def initUI(self):
        label1 = QLabel("Label 1 ", self)
        label1.move(10, 10)

        label2 = QLabel("Label 1 ", self)
        label2.move(20, 20)

        label3 = QLabel("Label 1 ", self)
        label3.move(30, 30)

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('absolute ')
        self.show()

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Escape:
    #         self.close()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
