# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created: Sun Sep  1 11:26:41 2013
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

class Ui_Log(object):
    def setupUi(self, Log):
        Log.setObjectName(_fromUtf8("Log"))
        Log.resize(294, 338)
        self.horizontalLayout = QtGui.QHBoxLayout(Log)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textBrowser = QtGui.QTextBrowser(Log)
        self.textBrowser.setFrameShape(QtGui.QFrame.Panel)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.horizontalLayout.addWidget(self.textBrowser)

        self.retranslateUi(Log)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        Log.setWindowTitle(_translate("Log", "Form", None))
        self.textBrowser.setHtml(_translate("Log", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))

