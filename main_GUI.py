#!/usr/bin/ env python
import WelcomeScreen, OpenEyeTraining, ClosedEyeTraining
from PyQt5 import QtCore, QtGui, QtWidgets

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WelcomeScreen.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
main()