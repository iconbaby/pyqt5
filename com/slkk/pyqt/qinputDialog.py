#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI();

    def initUI(self):
        self.label = QLabel('姓名', self)
        self.label.move(3, 10)

        self.textLine = QLineEdit(self)
        self.textLine.move(50, 10)

        self.btn = QPushButton('input', self)
        self.btn.move(50, 100)
        self.btn.clicked.connect(self.btnclick)

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('absolute ')
        self.show()

    def btnclick(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name ')
        if ok:
            self.textLine.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
