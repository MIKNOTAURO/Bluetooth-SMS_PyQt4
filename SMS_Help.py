# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_dialog.ui'
#
# Created: Sun Sep  8 17:35:08 2013
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

class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName(_fromUtf8("Help"))
        Help.resize(419, 448)
        Help.setWindowOpacity(1.0)
        Help.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(Help)
        self.verticalLayout.setContentsMargins(11, 14, 11, 14)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Help)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.scrollArea = QtGui.QScrollArea(Help)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -214, 377, 570))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.buttonBox = QtGui.QDialogButtonBox(Help)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Help)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Help.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Help.reject)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        Help.setWindowTitle(_translate("Help", "Help", None))
        self.label.setText(_translate("Help", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Welcome!</span></p></body></html>", None))
        self.label_2.setText(_translate("Help", "<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">Aim:</span></p><p align=\"justify\">This software allows you to send and receive SMS messages through a bluetooth link.</p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">How it works?</span></p><p align=\"justify\">The RFCOMM protocol is used to establish the bluetooth link between the computer and the mobile phone. Once the bluetooth link is created, the a Dial-up networking (DUN) service is needed in order to allow send the AT commands to the mobile device.</p><p align=\"justify\">NOTE: To use DUN, you must set both your phone’s and your computer’s Bluetooth settings to On and form a trusted pair between your computer and your mobile device.</p><p align=\"justify\">Finally, you need balance in your phone device!!!</p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">Send SMS:</span></p><p align=\"justify\">1. Once you have refreshed the devices list, you must choise a mobile device to connect.</p><p align=\"justify\">2. Click on Send SMS button. This action performs a search looking for the DUN service. If that service is found, you will be able to insert the thelephone number target and the message to send.</p><p align=\"justify\">3. When done, press the Ok button.</p><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600;\">Receive SMS:</span></p><p align=\"justify\">1. Once you have refressed the devices list, you must choose a mobile device to connect.</p><p align=\"justify\">2. Click on Inbox button. This action performs a search looking the DUN service. If that service is found, the SMS messages will be listed.</p></body></html>", None))

