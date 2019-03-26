# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jagan\OneDrive\Desktop\OpenEyeTraining.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import training
import os
class Ui_OpenEyeTraining(object):
    def setupUi(self, OpenEyeTraining):
        OpenEyeTraining.setObjectName("OpenEyeTraining")
        OpenEyeTraining.setEnabled(True)
        OpenEyeTraining.resize(780, 670)
        self.centralwidget = QtWidgets.QWidget(OpenEyeTraining)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.OpenEyesTraining_progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.OpenEyesTraining_progressBar.setProperty("value", 0)
        self.OpenEyesTraining_progressBar.setObjectName("OpenEyesTraining_progressBar")
        self.gridLayout.addWidget(self.OpenEyesTraining_progressBar, 5, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 2, 0, 1, 1)
        self.OpenEyesLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenEyesLabel.sizePolicy().hasHeightForWidth())
        self.OpenEyesLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setUnderline(True)
        self.OpenEyesLabel.setFont(font)
        self.OpenEyesLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.OpenEyesLabel.setObjectName("OpenEyesLabel")
        self.gridLayout.addWidget(self.OpenEyesLabel, 0, 0, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout.addWidget(self.infoLabel, 1, 0, 1, 1)
        OpenEyeTraining.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OpenEyeTraining)
        self.statusbar.setObjectName("statusbar")
        OpenEyeTraining.setStatusBar(self.statusbar)

        self.retranslateUi(OpenEyeTraining)
        QtCore.QMetaObject.connectSlotsByName(OpenEyeTraining)

        self.button2.clicked.connect(self.open_eyes_training)
    def retranslateUi(self, OpenEyeTraining):
        _translate = QtCore.QCoreApplication.translate
        OpenEyeTraining.setWindowTitle(_translate("OpenEyeTraining", "MainWindow"))
        self.button2.setText(_translate("OpenEyeTraining", "Start Training"))
        self.OpenEyesLabel.setText(_translate("OpenEyeTraining", "BB8 Open Eyes Training"))
        self.infoLabel.setText(_translate("OpenEyeTraining", "Click \"Start Training\" and close your eyes"))
    def open_eyes_training(self, openeye):
        training.train(eyesopen= openeye)
        os.system('python2 ClosedEyeTraining.py')

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenEyeTraining = QtWidgets.QMainWindow()
    ui = Ui_OpenEyeTraining()
    ui.setupUi(OpenEyeTraining)
    OpenEyeTraining.show()
    sys.exit(app.exec_())

