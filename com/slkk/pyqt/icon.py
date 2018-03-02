#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
this example shows an icon
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 300, 1000, 400)
        self.setWindowTitle('icon')
        self.setWindowIcon(QIcon('gvim.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
