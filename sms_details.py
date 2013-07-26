# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sms_details.ui'
#
# Created: Wed Jul 24 20:53:23 2013
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

class Ui_SMSDetails(object):
    def setupUi(self, SMSDetails):
        SMSDetails.setObjectName(_fromUtf8("SMSDetails"))
        SMSDetails.resize(511, 374)
        SMSDetails.setMinimumSize(QtCore.QSize(347, 347))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        SMSDetails.setFont(font)
        SMSDetails.setModal(True)
        self.gridLayout = QtGui.QGridLayout(SMSDetails)
        self.gridLayout.setContentsMargins(11, 14, 11, 14)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SMSDetails)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(SMSDetails)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SMSDetails)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(SMSDetails)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SMSDetails)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(SMSDetails)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SMSDetails.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SMSDetails.reject)
        QtCore.QMetaObject.connectSlotsByName(SMSDetails)

    def retranslateUi(self, SMSDetails):
        SMSDetails.setWindowTitle(_translate("SMSDetails", "Edit SMS Message", None))
        self.label.setText(_translate("SMSDetails", "Phone number", None))
        self.label_2.setText(_translate("SMSDetails", "Type your message", None))

