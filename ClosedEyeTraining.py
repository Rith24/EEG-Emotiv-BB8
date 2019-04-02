# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jagan\OneDrive\Desktop\closedEyeTraining.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import training
from avgATvalue_GUI import Ui_AverageAlphaThetaRatioValue
class Ui_CloseEyeTraining(object):
    def setupUi(self, CloseEyeTraining):
        CloseEyeTraining.setObjectName("CloseEyeTraining")
        CloseEyeTraining.resize(780, 670)
        self.centralwidget = QtWidgets.QWidget(CloseEyeTraining)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 2, 0, 1, 1)
        self.ClosedEyesLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setUnderline(True)
        self.ClosedEyesLabel.setFont(font)
        self.ClosedEyesLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.ClosedEyesLabel.setObjectName("ClosedEyesLabel")
        self.gridLayout.addWidget(self.ClosedEyesLabel, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout.addWidget(self.infoLabel, 1, 0, 1, 1)
        CloseEyeTraining.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CloseEyeTraining)
        self.statusbar.setObjectName("statusbar")
        CloseEyeTraining.setStatusBar(self.statusbar)

        self.retranslateUi(CloseEyeTraining)
        QtCore.QMetaObject.connectSlotsByName(CloseEyeTraining)
        self.button3.clicked.connect(self.closed_eyes_training)
    def retranslateUi(self, CloseEyeTraining):
        _translate = QtCore.QCoreApplication.translate
        CloseEyeTraining.setWindowTitle(_translate("CloseEyeTraining", "MainWindow"))
        self.button3.setText(_translate("CloseEyeTraining", "Start Training"))
        self.ClosedEyesLabel.setText(_translate("CloseEyeTraining", "BB8 Closed Eyes Training"))
        self.infoLabel.setText(_translate("CloseEyeTraining", "Click \"Start Training\" and close your eyes"))
    def closed_eyes_training(self):
        #training.train(eyesopen=False)
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AverageAlphaThetaRatioValue()
        self.ui.setupUi(self.window)
        #MainWindow.hide()
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CloseEyeTraining = QtWidgets.QMainWindow()
    ui = Ui_CloseEyeTraining()
    ui.setupUi(CloseEyeTraining)
    CloseEyeTraining.show()
    sys.exit(app.exec_())

