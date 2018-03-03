#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        impMenu = QMenu('import', self)
        impAct = QAction('Import mail',self)
        impMenu.addAction(impAct)
        fileAction = QAction('NEW',self)
        fileMenu.addAction(fileAction)
        fileMenu.addMenu(impMenu)

        self.setGeometry(100,100,500,500)
        self.setWindowTitle('submenu')
        self.show()
if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())



