#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle("messageBox")
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sur to quit?", QMessageBox
                                     .Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accpet()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
