# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SMS.ui'
#
# Created: Wed Aug 28 22:36:01 2013
#      by: PyQt4 UI code generator 4.9.6
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

class Ui_SMS(object):
    def setupUi(self, SMS):
        SMS.setObjectName(_fromUtf8("SMS"))
        SMS.resize(538, 374)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SMS.setWindowIcon(icon)
        SMS.setIconSize(QtCore.QSize(32, 32))
        SMS.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QtGui.QWidget(SMS)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 520, 295))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(10, 10, 501, 281))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        SMS.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(SMS)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SMS.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(SMS)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        SMS.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRefresh = QtGui.QAction(SMS)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/refresh.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionRefresh.setIcon(icon1)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionHelp = QtGui.QAction(SMS)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/help.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon2)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionSend = QtGui.QAction(SMS)
        self.actionSend.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/send-sms.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSend.setIcon(icon3)
        self.actionSend.setObjectName(_fromUtf8("actionSend"))
        self.actionQuit = QtGui.QAction(SMS)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/exit.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon4)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionEs = QtGui.QAction(SMS)
        self.actionEs.setObjectName(_fromUtf8("actionEs"))
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionSend)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(SMS)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), SMS.close)
        QtCore.QMetaObject.connectSlotsByName(SMS)

    def retranslateUi(self, SMS):
        SMS.setWindowTitle(_translate("SMS", "SMS Service", None))
        self.toolBar.setWindowTitle(_translate("SMS", "toolBar", None))
        self.actionRefresh.setText(_translate("SMS", "Refresh", None))
        self.actionRefresh.setToolTip(_translate("SMS", "Look up for available devices", None))
        self.actionRefresh.setShortcut(_translate("SMS", "Ctrl+Shift+R", None))
        self.actionHelp.setText(_translate("SMS", "Help", None))
        self.actionHelp.setToolTip(_translate("SMS", "Show help", None))
        self.actionHelp.setShortcut(_translate("SMS", "Ctrl+Shift+H", None))
        self.actionSend.setText(_translate("SMS", "Send SMS", None))
        self.actionSend.setToolTip(_translate("SMS", "Send a SMS message", None))
        self.actionSend.setShortcut(_translate("SMS", "Ctrl+Shift+S", None))
        self.actionQuit.setText(_translate("SMS", "Quit", None))
        self.actionQuit.setToolTip(_translate("SMS", "Exit application", None))
        self.actionQuit.setShortcut(_translate("SMS", "Ctrl+Q", None))
        self.actionEs.setText(_translate("SMS", "es", None))
        self.actionEs.setToolTip(_translate("SMS", "Switch language (en-es)", None))

import resources_rc
