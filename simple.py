#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
window in pyqt5
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(800, 600)
    w.move(200, 50)
    w.setWindowTitle("Simple")
    w.show()
    sys.exit(app.exec_())