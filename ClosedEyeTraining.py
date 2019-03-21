# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jagan\OneDrive\Desktop\ClosedEyeTraining.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CloseEyeTraining(object):
    def setupUi(self, CloseEyeTraining):
        CloseEyeTraining.setObjectName("CloseEyeTraining")
        CloseEyeTraining.resize(780, 670)
        self.centralwidget = QtWidgets.QWidget(CloseEyeTraining)
        self.centralwidget.setObjectName("centralwidget")
        self.trainingclosed = QtWidgets.QLabel(self.centralwidget)
        self.trainingclosed.setGeometry(QtCore.QRect(260, 110, 281, 111))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setUnderline(True)
        self.trainingclosed.setFont(font)
        self.trainingclosed.setObjectName("trainingclosed")
        self.startTrainingClosed = QtWidgets.QPushButton(self.centralwidget)
        self.startTrainingClosed.setGeometry(QtCore.QRect(330, 270, 115, 35))
        self.startTrainingClosed.setObjectName("startTrainingClosed")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 360, 290, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        CloseEyeTraining.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CloseEyeTraining)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 31))
        self.menubar.setObjectName("menubar")
        CloseEyeTraining.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CloseEyeTraining)
        self.statusbar.setObjectName("statusbar")
        CloseEyeTraining.setStatusBar(self.statusbar)

        self.retranslateUi(CloseEyeTraining)
        QtCore.QMetaObject.connectSlotsByName(CloseEyeTraining)

    def retranslateUi(self, CloseEyeTraining):
        _translate = QtCore.QCoreApplication.translate
        CloseEyeTraining.setWindowTitle(_translate("CloseEyeTraining", "MainWindow"))
        self.trainingclosed.setText(_translate("CloseEyeTraining", "Closed Eye Training"))
        self.startTrainingClosed.setText(_translate("CloseEyeTraining", "Start Training"))

    #TODO: add a function that gets number of packets and turn into progress bar
    #      and close this window


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CloseEyeTraining = QtWidgets.QMainWindow()
    ui = Ui_CloseEyeTraining()
    ui.setupUi(CloseEyeTraining)
    CloseEyeTraining.show()
    sys.exit(app.exec_())

