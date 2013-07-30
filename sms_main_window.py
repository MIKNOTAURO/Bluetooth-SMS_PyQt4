# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Wed Jul 24 15:37:14 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from time import sleep

import bluetooth
import functools
import resources_rc

from help_dialog import Ui_Help
from sms_details import Ui_SMSDetails


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

class Ui_SMSMain(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_SMSMain, self).__init__()

    def findDevices(self):
        return bluetooth.discover_devices(lookup_names = True)

    def sendClicked(self, address):
        print "Send SMS button was clicked", address
        EditSMS = QtGui.QDialog()
        editDialog = Ui_SMSDetails()
        editDialog.setupUi(EditSMS)
        r = EditSMS.exec_()
        if r:
            phone_number = str(editDialog.lineEdit.text())
            sms_data   = str(editDialog.textEdit.toPlainText())
            information = ""
            for addr, name in self.availableDevices:
                if addr == self.address:
                    information = 'Great, the phone was found!\nPlease wait, looking for Dial-up networking service...\n'
                    host = addr
                    services = bluetooth.find_service(address = host)
                    channel = 0
                    if len(services) > 0:
                        for service in services:
                            name = service["name"]
                            if name == "Dial-up networking" or name == "Dial-Up Networking" or name == "Dial-up Networking":
                                channel = service["port"]

                            if channel != 0:
                                information += "Found Dial-up networking at channel "
                                information += str(channel)
                                break
                    else:
                        QtGui.QMessageBox.critical(self, "Information", "No available services\nTry another device, please.")
                        return
                
                    if channel == 0:
                        QtGui.QMessageBox.critical(self, "Information",
														"No Dial-Up Networking service detected!\nTry another device, please.")
                        return

                    QtGui.QMessageBox.information(self, "Information", information)

                    mobile = '52' + phone_number 
                    
                    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                    
                    socket.connect((host, channel))
                    
                    socket.send('AT+CMGF=1\r')
                    sleep(2)
                    print socket.recv(1024)
                    sleep(2)
                    command = 'AT+CMGS="+' + mobile + '"\r'
                    print "%r" % command
                    socket.send(command)
                    sleep(2)
                    print socket.recv(1024)
                    sleep(2)
                    socket.send(sms_data+chr(26))
                    sleep(2)
                    print socket.recv(1024)
                    sleep(2)
                    socket.close()

    def radioActivated(self, address):
        self.actionSend.setEnabled(True)
        self.address = address

    def refreshDevicesList(self):
        print "Refresh button pressed"
        self.availableDevices = self.findDevices()

        self.clearLayout(self.scrollAreaLayout)
        if len(self.availableDevices) > 0:
            message = QtGui.QLabel("Chose from the mobile devices below:")
            self.scrollAreaLayout.addWidget(message)
 
            line = QtGui.QFrame()
            line.setFrameShape(QtGui.QFrame.HLine)
            line.setFrameShadow(QtGui.QFrame.Sunken)
 
            self.scrollAreaLayout.addWidget(line)

            for address, name in self.availableDevices:
                deviceName = QtGui.QLabel("     " + address)

                radio = QtGui.QRadioButton(name)

                line = QtGui.QFrame()
                line.setFrameShape(QtGui.QFrame.HLine)
                line.setFrameShadow(QtGui.QFrame.Sunken)

                self.scrollAreaLayout.addWidget(radio)
                self.scrollAreaLayout.addWidget(deviceName)
                self.scrollAreaLayout.addWidget(line)

                radio.toggled.connect(functools.partial(self.radioActivated, address))

            self.scrollAreaWidgetContents.setLayout(self.scrollAreaLayout)
            self.scrollAreaLayout.addStretch(1)
        else:
            self.scrollAreaLayout.addWidget(QtGui.QLabel("No bluetooth devices found."))
            self.scrollAreaWidgetContents.setLayout(self.scrollAreaLayout)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def helpClicked(self):
        helpWindow = QtGui.QDialog()
        helpDialog = Ui_Help()
        helpDialog.setupUi(helpWindow)
        helpWindow.exec_()

    def setupUi(self, SMSMain):
        SMSMain.setObjectName(_fromUtf8("SMSMain"))
        SMSMain.resize(538, 374)
        SMSMain.setIconSize(QtCore.QSize(32, 32))
        SMSMain.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        SMSMain.setTabShape(QtGui.QTabWidget.Rounded)
        SMSMain.setDockNestingEnabled(False)
        SMSMain.setMinimumSize(250, 300)

        icon0 = QtGui.QIcon()
        icon0.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SMSMain.setWindowIcon(icon0)

        self.centralwidget = QtGui.QWidget(SMSMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.scrollAreaLayout = QtGui.QVBoxLayout()

        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)

        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 385))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
#
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        SMSMain.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(SMSMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SMSMain.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(SMSMain)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        SMSMain.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRefresh = QtGui.QAction(SMSMain)
        self.actionRefresh.setCheckable(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/search-52x52.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon)
        self.actionRefresh.setIconVisibleInMenu(True)
        self.actionRefresh.setPriority(QtGui.QAction.HighPriority)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))

        self.actionSend = QtGui.QAction(SMSMain)
        self.actionSend.setCheckable(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sent.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSend.setIcon(icon4)
        self.actionSend.setIconVisibleInMenu(True)
        self.actionSend.setObjectName(_fromUtf8("actionSend"))
        self.actionSend.setEnabled(False)

        self.actionMore = QtGui.QAction(SMSMain)
        self.actionMore.setCheckable(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sent.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMore.setIcon(icon5)
        self.actionMore.setIconVisibleInMenu(True)
        self.actionMore.setObjectName(_fromUtf8("actionMore"))
        self.actionMore.setEnabled(False)

        self.actionExit = QtGui.QAction(SMSMain)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionHelp = QtGui.QAction(SMSMain)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/gnome-help.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon2)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
#
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionSend)
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(SMSMain)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), SMSMain.close)
        self.actionSend.triggered.connect(functools.partial(self.sendClicked, "Hello"))

        self.actionHelp.triggered.connect(self.helpClicked)
        self.actionRefresh.triggered.connect(self.refreshDevicesList)

        self.address = ""
        QtCore.QMetaObject.connectSlotsByName(SMSMain)

    def retranslateUi(self, SMSMain):
        SMSMain.setWindowTitle(_translate("SMSMain", "SMS Service", None))
        SMSMain.setStatusTip(_translate("SMSMain", "Ready", None))
        self.toolBar.setWindowTitle(_translate("SMSMain", "toolBar", None))
        self.actionRefresh.setText(_translate("SMSMain", "Refresh", None))
        self.actionRefresh.setToolTip(_translate("SMSMain", "Looking for available devices", None))
        self.actionRefresh.setStatusTip(_translate("SMSMain", "Looking for available devices", None))
        self.actionRefresh.setShortcut(_translate("SMSMain", "Ctrl+R", None))
        self.actionExit.setText(_translate("SMSMain", "Exit", None))
        self.actionExit.setToolTip(_translate("SMSMain", "Exit application", None))
        self.actionExit.setStatusTip(_translate("SMSMain", "Exit application", None))
        self.actionExit.setShortcut(_translate("SMSMain", "Ctrl+Q", None))
        self.actionHelp.setText(_translate("SMSMain", "Help", None))
        self.actionHelp.setToolTip(_translate("SMSMain", "Help", None))
        self.actionHelp.setStatusTip(_translate("SMSMain", "Help", None))
        self.actionHelp.setShortcut(_translate("SMSMain", "Ctrl+H", None))
        self.actionSend.setText(_translate("SMSMain", "Send SMS", None))
        self.actionSend.setToolTip(_translate("SMSMain", "Send a SMS message to the selected device", None))
        self.actionSend.setStatusTip(_translate("SMSMain", "Send a SMS message to the selected device", None))
        self.actionSend.setShortcut(_translate("SMSMain", "Ctrl+S", None))

