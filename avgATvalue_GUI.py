# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avgATvalue.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import training

class Ui_AverageAlphaThetaRatioValue(object):
    def setupUi(self, AverageAlphaThetaRatioValue):
        AverageAlphaThetaRatioValue.setObjectName("AverageAlphaThetaRatioValue")
        AverageAlphaThetaRatioValue.resize(825, 610)
        self.centralwidget = QtWidgets.QWidget(AverageAlphaThetaRatioValue)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.avgRatioOfAandTValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setUnderline(True)
        self.avgRatioOfAandTValue.setFont(font)
        self.avgRatioOfAandTValue.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.avgRatioOfAandTValue.setObjectName("avgRatioOfAandTValue")
        self.gridLayout.addWidget(self.avgRatioOfAandTValue, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        AverageAlphaThetaRatioValue.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AverageAlphaThetaRatioValue)
        self.statusbar.setObjectName("statusbar")
        AverageAlphaThetaRatioValue.setStatusBar(self.statusbar)

        self.retranslateUi(AverageAlphaThetaRatioValue)
        QtCore.QMetaObject.connectSlotsByName(AverageAlphaThetaRatioValue)

    def retranslateUi(self, AverageAlphaThetaRatioValue):
        _translate = QtCore.QCoreApplication.translate
        AverageAlphaThetaRatioValue.setWindowTitle(_translate("AverageAlphaThetaRatioValue", "Average of Alpha and Theta Ration Value"))
        self.avgRatioOfAandTValue.setText(_translate("AverageAlphaThetaRatioValue", "Average of Alpha and Theta ratio value: ", training.get_average_abt()))
        self.label.setText(_translate("AverageAlphaThetaRatioValue", "Ratio of Alpha and Theta eyesOpen: ", training.get_abt_o()))
        self.label_2.setText(_translate("AverageAlphaThetaRatioValue", "Ration of Alpha and Theta eyesClosed: ", training.get_abt_o()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AverageAlphaThetaRatioValue = QtWidgets.QMainWindow()
    ui = Ui_AverageAlphaThetaRatioValue()
    ui.setupUi(AverageAlphaThetaRatioValue)
    AverageAlphaThetaRatioValue.show()
    sys.exit(app.exec_())

