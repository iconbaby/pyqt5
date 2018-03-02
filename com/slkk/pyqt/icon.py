#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
this example shows an icon
"""
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip,
                             QPushButton)
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QpushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(200, 300, 1000, 400)
        self.setWindowTitle('icon')
        self.setWindowIcon(QIcon('gvim.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
