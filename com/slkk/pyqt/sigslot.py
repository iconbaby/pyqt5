#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        qlcd = QLCDNumber(self)
        qslide = QSlider(Qt.Horizontal, self)
        qslide.valueChanged.connect(qlcd.display)
        vbox.addWidget(qlcd)
        vbox.addWidget(qslide)

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('sigslot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
