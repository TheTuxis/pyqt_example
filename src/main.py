#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic

BASE_DIR = '/Users/pdalmasso/Dev/Project/curso_interfaz/src/'


class MyWindowsClass:
    def __init__(self):
        self.MainWindow = uic.loadUi('mainwindow.ui')
        self.MainWindow.connect(
            self.MainWindow.btn_ok, QtCore.SIGNAL("clicked()"),
            self.click_btn_ok
        )

    def click_btn_ok(self):
        text = self.MainWindow.le_01.text()
        self.MainWindow.lbl_result.setText(text)
        self.MainWindow.textEdit.append(text)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainwindow = MyWindowsClass()
    mainwindow.MainWindow.show()
    app.exec_()
