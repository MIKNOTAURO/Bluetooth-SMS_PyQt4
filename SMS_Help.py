# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help_dialog.ui'
#
# Created: Mon Aug 19 21:30:09 2013
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
        Help.resize(370, 470)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 344, 378))
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
        self.label.setText(_translate("Help", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Welcome</span></p></body></html>", None))
        self.label_2.setText(_translate("Help", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Requirements:</span></p><p><span style=\" font-size:10pt;\">1. Python language</span></p><p><span style=\" font-size:10pt;\">2. PyQt 4.9 or higher</span></p><p><span style=\" font-size:10pt;\">3. Computer with Bluetooth tecnology</span></p><p><span style=\" font-size:10pt;\">4. Mobile device with Bluetooth tecnology</span></p><p><span style=\" font-size:10pt;\">5. Balance in your phone device</span></p><p><span style=\" font-size:10pt;\"><br/></span><span style=\" font-size:11pt; font-weight:600;\">Notes:</span></p><p><span style=\" font-size:10pt;\">In order to allow you send sms messages, you must enable your bluetooth service in this computer and your mobile device too.</span></p><p><span style=\" font-size:10pt;\">From the available devices, choose one and then press the \'</span><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Send SMS</span><span style=\" font-size:10pt;\">\' button, and write your message, when done press the Ok button :)</span></p></body></html>", None))

