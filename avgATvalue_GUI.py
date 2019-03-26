# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jagan\OneDrive\Desktop\avgATvalue.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import training

class Ui_AverageAlphaThetaRatioValue(object):
    def setupUi(self, AverageAlphaThetaRatioValue):
        AverageAlphaThetaRatioValue.setObjectName("AverageAlphaThetaRatioValue")
        AverageAlphaThetaRatioValue.resize(814, 630)
        self.centralwidget = QtWidgets.QWidget(AverageAlphaThetaRatioValue)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.avgRatioOfAandTValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setUnderline(True)
        self.avgRatioOfAandTValue.setFont(font)
        self.avgRatioOfAandTValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.avgRatioOfAandTValue.setObjectName("avgRatioOfAandTValue")
        self.gridLayout_2.addWidget(self.avgRatioOfAandTValue, 0, 0, 1, 1)
        AverageAlphaThetaRatioValue.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AverageAlphaThetaRatioValue)
        self.statusbar.setObjectName("statusbar")
        AverageAlphaThetaRatioValue.setStatusBar(self.statusbar)

        self.retranslateUi(AverageAlphaThetaRatioValue)
        QtCore.QMetaObject.connectSlotsByName(AverageAlphaThetaRatioValue)

    def retranslateUi(self, AverageAlphaThetaRatioValue):
        _translate = QtCore.QCoreApplication.translate
        AverageAlphaThetaRatioValue.setWindowTitle(_translate("AverageAlphaThetaRatioValue", "Average of Alpha and Theta Ration Value"))
        self.avgRatioOfAandTValue.setText(_translate("AverageAlphaThetaRatioValue", "Average of Alpha and Theta ratio value: "), training.get_average_abt())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AverageAlphaThetaRatioValue = QtWidgets.QMainWindow()
    ui = Ui_AverageAlphaThetaRatioValue()
    ui.setupUi(AverageAlphaThetaRatioValue)
    AverageAlphaThetaRatioValue.show()
    sys.exit(app.exec_())

