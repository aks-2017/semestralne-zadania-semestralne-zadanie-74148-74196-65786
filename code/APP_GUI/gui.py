# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri Nov 17 14:27:02 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1224, 610)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.guiBtnDelete = QtGui.QPushButton(self.centralwidget)
        self.guiBtnDelete.setGeometry(QtCore.QRect(820, 480, 98, 27))
        self.guiBtnDelete.setObjectName(_fromUtf8("guiBtnDelete"))
        self.guiCbForwarder = QtGui.QFontComboBox(self.centralwidget)
        self.guiCbForwarder.setGeometry(QtCore.QRect(110, 10, 201, 27))
        self.guiCbForwarder.setObjectName(_fromUtf8("guiCbForwarder"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(340, 10, 141, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.guiTblFirewallRules = QtGui.QTableWidget(self.centralwidget)
        self.guiTblFirewallRules.setGeometry(QtCore.QRect(10, 90, 801, 421))
        self.guiTblFirewallRules.setColumnCount(17)
        self.guiTblFirewallRules.setObjectName(_fromUtf8("guiTblFirewallRules"))
        self.guiTblFirewallRules.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.guiTblFirewallRules.setHorizontalHeaderItem(8, item)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 120, 66, 17))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(820, 60, 121, 411))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 30, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 66, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(0, 120, 66, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(0, 150, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(0, 180, 91, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(0, 210, 66, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(0, 240, 91, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(0, 270, 121, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(0, 300, 121, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 101, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(930, 480, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1040, 480, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(950, 90, 80, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(950, 120, 80, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(950, 150, 80, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(950, 180, 150, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(950, 210, 150, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(950, 240, 150, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(950, 270, 150, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(950, 300, 151, 27))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(950, 330, 80, 27))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(950, 360, 80, 27))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(1120, 240, 41, 27))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1106, 246, 16, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_9 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(1120, 270, 41, 27))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1106, 276, 16, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.guiBtnDelete.setText(_translate("MainWindow", "Delete", None))
        self.label.setText(_translate("MainWindow", "Forwarder", None))
        self.checkBox.setText(_translate("MainWindow", "Enable Firewall", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Action", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Src. MAC", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dst. MAC", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Src. IP", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "L4. Protocol", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Interface", None))
        item = self.guiTblFirewallRules.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Direction", None))
        self.label_3.setText(_translate("MainWindow", "Interface", None))
        self.label_4.setText(_translate("MainWindow", "Direction", None))
        self.label_2.setText(_translate("MainWindow", "Action", None))
        self.label_6.setText(_translate("MainWindow", "Src. MAC", None))
        self.label_7.setText(_translate("MainWindow", "Dst. MAC", None))
        self.label_8.setText(_translate("MainWindow", "Src. IP ", None))
        self.label_9.setText(_translate("MainWindow", "Dst. IP", None))
        self.label_10.setText(_translate("MainWindow", "L4 Protocol", None))
        self.label_12.setText(_translate("MainWindow", "Src. Port Number", None))
        self.label_13.setText(_translate("MainWindow", "Dst. Port Number", None))
        self.label_11.setText(_translate("MainWindow", "Firewall Rules ", None))
        self.pushButton.setText(_translate("MainWindow", "Create", None))
        self.pushButton_2.setText(_translate("MainWindow", "Edit", None))
        self.lineEdit.setText(_translate("MainWindow", "192.168.168.168", None))
        self.lineEdit_2.setText(_translate("MainWindow", "AA:AA:AA:AA:AA:AA", None))
        self.label_14.setText(_translate("MainWindow", "/", None))
        self.label_15.setText(_translate("MainWindow", "/", None))
