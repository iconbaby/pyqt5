#!/usr/bin/python3
#
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QTextEdit, QMainWindow
, QAction, QFileDialog)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI();

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'OPEN', self)
        openFile.setShortcut('Ctrl +O')
        openFile.setStatusTip('open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('File dialogs ')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'for ')
            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
