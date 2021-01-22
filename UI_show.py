# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_show.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.apart_Button = QtWidgets.QPushButton(self.centralwidget)
        self.apart_Button.setGeometry(QtCore.QRect(30, 370, 131, 28))
        self.apart_Button.setObjectName("apart_Button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 120, 691, 611))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.unit_Button = QtWidgets.QPushButton(self.centralwidget)
        self.unit_Button.setGeometry(QtCore.QRect(30, 440, 129, 28))
        self.unit_Button.setObjectName("unit_Button")
        self.address_Button = QtWidgets.QPushButton(self.centralwidget)
        self.address_Button.setGeometry(QtCore.QRect(30, 300, 129, 28))
        self.address_Button.setObjectName("address_Button")
        self.run_view_Button = QtWidgets.QPushButton(self.centralwidget)
        self.run_view_Button.setGeometry(QtCore.QRect(30, 220, 131, 28))
        self.run_view_Button.setObjectName("run_view_Button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 50, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.address_Button.raise_()
        self.unit_Button.raise_()
        self.apart_Button.raise_()
        self.run_view_Button.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.apart_Button.setText(_translate("MainWindow", "可视化户型数量"))
        self.label.setText(_translate("MainWindow", "              本界面用于显数据分析可视化图"))
        self.unit_Button.setText(_translate("MainWindow", "各个地区房源均价"))
        self.address_Button.setText(_translate("MainWindow", "各个地区房源数量"))
        self.run_view_Button.setText(_translate("MainWindow", "分析数据"))
        self.label_2.setText(_translate("MainWindow", "二手房数据分析可视化显示界面"))
