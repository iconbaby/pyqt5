#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI();

    def initUI(self):
        gride = QGridLayout();

        x = 0;
        y = 0;

        self.text = "x:{0},y:{1}".format(x, y)
        self.label = QLabel(self.text, self);
        gride.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(gride)

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('absolute ')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
