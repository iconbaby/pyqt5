#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI();

    def initUI(self):
        okButton = QPushButton('OK', self)
        cancelButton = QPushButton('cancle', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('absolute ')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
