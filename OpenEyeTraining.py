# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jagan\OneDrive\Desktop\OpenEyeTraining.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenEyeTraining(object):
    def setupUi(self, OpenEyeTraining):
        OpenEyeTraining.setObjectName("OpenEyeTraining")
        OpenEyeTraining.setEnabled(True)
        OpenEyeTraining.resize(780, 670)
        self.centralwidget = QtWidgets.QWidget(OpenEyeTraining)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 130, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.startTrainingOpen = QtWidgets.QPushButton(self.centralwidget)
        self.startTrainingOpen.setGeometry(QtCore.QRect(290, 250, 112, 34))
        self.startTrainingOpen.setObjectName("startTrainingOpen")
        self.progressBarOpenEyes = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarOpenEyes.setGeometry(QtCore.QRect(230, 450, 300, 25))
        self.progressBarOpenEyes.setProperty("value", 24)
        self.progressBarOpenEyes.setObjectName("progressBarOpenEyes")
        OpenEyeTraining.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OpenEyeTraining)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 31))
        self.menubar.setObjectName("menubar")
        OpenEyeTraining.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OpenEyeTraining)
        self.statusbar.setObjectName("statusbar")
        OpenEyeTraining.setStatusBar(self.statusbar)

        self.retranslateUi(OpenEyeTraining)
        QtCore.QMetaObject.connectSlotsByName(OpenEyeTraining)

    def retranslateUi(self, OpenEyeTraining):
        _translate = QtCore.QCoreApplication.translate
        OpenEyeTraining.setWindowTitle(_translate("OpenEyeTraining", "MainWindow"))
        self.label.setText(_translate("OpenEyeTraining", "Open Eye Training"))
        self.startTrainingOpen.setText(_translate("OpenEyeTraining", "Start Training"))
        
    #TODO: add a function that gets number of packets and turn into progress bar
    #      and open the closed eye training and close this window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenEyeTraining = QtWidgets.QMainWindow()
    ui = Ui_OpenEyeTraining()
    ui.setupUi(OpenEyeTraining)
    OpenEyeTraining.show()
    sys.exit(app.exec_())

