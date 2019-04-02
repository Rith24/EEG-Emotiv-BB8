# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jagan\OneDrive\Desktop\WelcomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from OpenEyeTraining import Ui_OpenEyeTraining
#from main_GUI import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 500)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TitleOfTheScreen = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setUnderline(True)
        self.TitleOfTheScreen.setFont(font)
        self.TitleOfTheScreen.setTextFormat(QtCore.Qt.AutoText)
        self.TitleOfTheScreen.setScaledContents(True)
        self.TitleOfTheScreen.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.TitleOfTheScreen.setObjectName("TitleOfTheScreen")
        self.verticalLayout_3.addWidget(self.TitleOfTheScreen)
        self.promptsWhatToDo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.promptsWhatToDo.setFont(font)
        self.promptsWhatToDo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.promptsWhatToDo.setObjectName("promptsWhatToDo")
        self.verticalLayout_3.addWidget(self.promptsWhatToDo)
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.verticalLayout_3.addWidget(self.button1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button1.clicked.connect(self.displayScreen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleOfTheScreen.setText(_translate("MainWindow", "Welcome to BB8 GUI"))
        self.promptsWhatToDo.setText(_translate("MainWindow", "Click \"Continue\" to start Training"))
        self.button1.setText(_translate("MainWindow", "Continue"))

    def displayScreen (self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OpenEyeTraining()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

