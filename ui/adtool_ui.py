# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adtool.ui'
#
# Created: Wed Oct 03 16:51:49 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ADTool(object):
    def setupUi(self, ADTool):
        ADTool.setObjectName("ADTool")
        ADTool.resize(952, 611)
        self.verticalLayout = QtGui.QVBoxLayout(ADTool)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acclist_label = QtGui.QLabel(ADTool)
        self.acclist_label.setMaximumSize(QtCore.QSize(16777215, 80))
        self.acclist_label.setObjectName("acclist_label")
        self.horizontalLayout.addWidget(self.acclist_label)
        self.acclist_textbox = QtGui.QPlainTextEdit(ADTool)
        self.acclist_textbox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.acclist_textbox.setObjectName("acclist_textbox")
        self.horizontalLayout.addWidget(self.acclist_textbox)
        self.checkacc_button = QtGui.QPushButton(ADTool)
        self.checkacc_button.setObjectName("checkacc_button")
        self.horizontalLayout.addWidget(self.checkacc_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.defaultpwd_label = QtGui.QLabel(ADTool)
        self.defaultpwd_label.setObjectName("defaultpwd_label")
        self.horizontalLayout_3.addWidget(self.defaultpwd_label)
        self.defaultpwd_textbox = QtGui.QLineEdit(ADTool)
        self.defaultpwd_textbox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.defaultpwd_textbox.setObjectName("defaultpwd_textbox")
        self.horizontalLayout_3.addWidget(self.defaultpwd_textbox)
        self.date_label = QtGui.QLabel(ADTool)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_3.addWidget(self.date_label)
        self.date_textbox = QtGui.QLineEdit(ADTool)
        self.date_textbox.setMaximumSize(QtCore.QSize(100, 20))
        self.date_textbox.setObjectName("date_textbox")
        self.horizontalLayout_3.addWidget(self.date_textbox)
        self.targetou_label = QtGui.QLabel(ADTool)
        self.targetou_label.setObjectName("targetou_label")
        self.horizontalLayout_3.addWidget(self.targetou_label)
        self.targetou_textbox = QtGui.QLineEdit(ADTool)
        self.targetou_textbox.setObjectName("targetou_textbox")
        self.horizontalLayout_3.addWidget(self.targetou_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.acctable_widget = QtGui.QTableWidget(ADTool)
        self.acctable_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acctable_widget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.acctable_widget.setObjectName("acctable_widget")
        self.acctable_widget.setColumnCount(6)
        self.acctable_widget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.acctable_widget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.acctable_widget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.acctable_widget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.acctable_widget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.acctable_widget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.acctable_widget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.acctable_widget)
        self.log_widget = QtGui.QListWidget(ADTool)
        self.log_widget.setMaximumSize(QtCore.QSize(16777215, 192))
        self.log_widget.setObjectName("log_widget")
        self.verticalLayout.addWidget(self.log_widget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resetpwd_button = QtGui.QPushButton(ADTool)
        self.resetpwd_button.setObjectName("resetpwd_button")
        self.horizontalLayout_2.addWidget(self.resetpwd_button)
        self.disable_button = QtGui.QPushButton(ADTool)
        self.disable_button.setObjectName("disable_button")
        self.horizontalLayout_2.addWidget(self.disable_button)
        self.unlock_button = QtGui.QPushButton(ADTool)
        self.unlock_button.setObjectName("unlock_button")
        self.horizontalLayout_2.addWidget(self.unlock_button)
        self.line = QtGui.QFrame(ADTool)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.extend_date = QtGui.QLineEdit(ADTool)
        self.extend_date.setMaximumSize(QtCore.QSize(100, 16777215))
        self.extend_date.setObjectName("extend_date")
        self.horizontalLayout_2.addWidget(self.extend_date)
        self.extend_button = QtGui.QPushButton(ADTool)
        self.extend_button.setObjectName("extend_button")
        self.horizontalLayout_2.addWidget(self.extend_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.version_info = QtGui.QLabel(ADTool)
        self.version_info.setObjectName("version_info")
        self.horizontalLayout_2.addWidget(self.version_info)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ADTool)
        QtCore.QMetaObject.connectSlotsByName(ADTool)

    def retranslateUi(self, ADTool):
        ADTool.setWindowTitle(QtGui.QApplication.translate("ADTool", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.acclist_label.setText(QtGui.QApplication.translate("ADTool", "   Danh sách Acc  ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkacc_button.setText(QtGui.QApplication.translate("ADTool", "Check Account", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultpwd_label.setText(QtGui.QApplication.translate("ADTool", "Default Password", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultpwd_textbox.setText(QtGui.QApplication.translate("ADTool", "12345abcd", None, QtGui.QApplication.UnicodeUTF8))
        self.date_label.setText(QtGui.QApplication.translate("ADTool", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.targetou_label.setText(QtGui.QApplication.translate("ADTool", "Target OU", None, QtGui.QApplication.UnicodeUTF8))
        self.acctable_widget.setSortingEnabled(True)
        self.acctable_widget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("ADTool", "Acc", None, QtGui.QApplication.UnicodeUTF8))
        self.acctable_widget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("ADTool", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.acctable_widget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("ADTool", "Acc Expires", None, QtGui.QApplication.UnicodeUTF8))
        self.acctable_widget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("ADTool", "Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.acctable_widget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("ADTool", "DN", None, QtGui.QApplication.UnicodeUTF8))
        self.acctable_widget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("ADTool", "✔", None, QtGui.QApplication.UnicodeUTF8))
        self.resetpwd_button.setText(QtGui.QApplication.translate("ADTool", "Reset Password", None, QtGui.QApplication.UnicodeUTF8))
        self.disable_button.setText(QtGui.QApplication.translate("ADTool", "Disable Account", None, QtGui.QApplication.UnicodeUTF8))
        self.unlock_button.setText(QtGui.QApplication.translate("ADTool", "Unlock", None, QtGui.QApplication.UnicodeUTF8))
        self.extend_button.setText(QtGui.QApplication.translate("ADTool", "Extend Account", None, QtGui.QApplication.UnicodeUTF8))
        self.version_info.setText(QtGui.QApplication.translate("ADTool", "v 10/03/2012 by congnt3", None, QtGui.QApplication.UnicodeUTF8))

