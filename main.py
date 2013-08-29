# -*- coding: utf-8 -*-
#from nose.tools import *

from sys import argv, exit

from PyQt4 import QtGui, QtCore

from time import sleep

import bluetooth
import functools

from SMS import Ui_SMS
from SMS_Help import Ui_Help
from SMS_Send import Ui_SMSDetails

class Help(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)

		self.ui = Ui_Help()
		self.ui.setupUi(self)

class Main(QtGui.QMainWindow):
	def __init__(self, app):
		QtGui.QMainWindow.__init__(self)

		self.application = app

#		self.setTranslators()

		self.ui = Ui_SMS()

		self.ui.setupUi(self)
#
#		self.combo = QtGui.QComboBox()
#		self.ui.toolBar.addWidget(self.combo)
#		self.combo.insertItems(1,["English","Spanish"])
#
		self.ui.actionHelp.triggered.connect(self.helpTriggered)
		self.ui.actionSend.triggered.connect(self.sendTriggered)
		self.ui.actionRefresh.triggered.connect(self.refreshDevices)

		self.scrollAreaLayout = QtGui.QVBoxLayout()

		self.address = ""

#	def setTranslators(self):
#		self.english_translator = QtCore.QTranslator(self.application)
#		self.english_translator.load("lang_en")
#		self.spanish_translator = QtCore.QTranslator(self.application)
#		self.spanish_translator.load("lang_es")
#
#	def setEnglishTranslator(self):
#		self.removeTranslator(self.spanish_translator)
#		self.installTranslator(self.english_translator)
#		self.ui.retranslateUi(self)
#
#	def setSpanishTranslator(self):
#		self.removeTranslator(self.english_translator)
#		self.installTranslator(self.spanish_translator)
#		self.ui.retranslateUi(self)

	def helpTriggered(self):
		aux = Help()
		aux.exec_()

	def sendTriggered(self):
		edit_sms = QtGui.QDialog()
		aux = Ui_SMSDetails()
		aux.setupUi(edit_sms)

		r = edit_sms.exec_()

		if r:
			phone_number	= str(aux.lineEdit.text())
			sms_data			= str(aux.textEdit.toPlainText())

			info					= ""
			for addr, name in self.devices:
				if addr == self.address:
					info				= 'Great, the phone was found!\nPlease wait ...\nLooking for Dial-up networking service...\n'
					host				= addr
					services		= bluetooth.find_service(address = host)
					channel			= 0
					if len(services) > 0:
						for service in services:
							name		= service["name"]
							if name == "Dial-up networking" or name == "Dial-Up Networking" or name == "Dial-up Networking":
								channel = service["port"]
								if channel != 0:
									info += "Found Dial-up networking at channel "
									info += str(channel)
									break
					else:
						QtGui.QMessageBox.critical(self, "Information",
								"No available services\nTry another device, please.")
						return

					if channel == 0:
						QtGui.QMessageBox.critical(self, "Information",
								"No Dial-up networking service detected!\nTry another device, please.")
						return

					QtGui.QMessageBox.information(self, "Information", info)

					mobile	= '52' + phone_number

					socket	= bluetooth.BluetoothSocket(bluetooth.RFCOMM)
					sleep(2)
					socket.connect((host, channel))

					socket.send('AT+CMGF=1\r')
					sleep(2)
					print socket.recv(1024)
					command	= 'AT+CMGS="+' + mobile + '"\r'
					print "%r" % command
					socket.send(command)
					sleep(2)
					print socket.recv(1024)
					socket.send(sms_data+chr(26))
					sleep(2)
					print socket.recv(1024)
					socket.close()


	def clearLayout(self, layout):
		if layout is not None:
			while layout.count():
				item = layout.takeAt(0)
				widget = item.widget()
				if widget is not None:
					widget.deleteLater()
				else:
					self.clearLayout(item.layout())

	def radioToggled(self, address):
		self.ui.actionSend.setEnabled(True)
		self.address = address
		
	def findDevices(self):
		return bluetooth.discover_devices(lookup_names = True)

	def refreshDevices(self):
		self.clearLayout(self.scrollAreaLayout)

		self.devices = self.findDevices()

		if len(self.devices) > 0:
			self.ui.actionSend.setEnabled(False)
			message = QtGui.QLabel(self.tr("Chose from the mobile devices below:"))

			self.scrollAreaLayout.addWidget(message)

			separator = QtGui.QFrame()
			separator.setFrameShape(QtGui.QFrame.HLine)
			separator.setFrameShadow(QtGui.QFrame.Sunken)

			self.scrollAreaLayout.addWidget(separator)

			for address, name in self.devices:
				deviceName = QtGui.QLabel("     " + address)

				radio = QtGui.QRadioButton(name)

				separator = QtGui.QFrame()
				separator.setFrameShape(QtGui.QFrame.HLine)
				separator.setFrameShadow(QtGui.QFrame.Sunken)

				self.scrollAreaLayout.addWidget(radio)
				self.scrollAreaLayout.addWidget(deviceName)
				self.scrollAreaLayout.addWidget(separator)

				radio.toggled.connect(functools.partial(self.radioToggled, address))
			
			self.ui.scrollAreaWidgetContents.setLayout(self.scrollAreaLayout)
			self.scrollAreaLayout.addStretch(1)
			
		else:
			self.scrollAreaLayout.addWidget(QtGui.QLabel("No bluetooth devices found."))
			self.ui.scrollAreaWidgetContents.setLayout(self.scrollAreaLayout)


if __name__ == "__main__":
  app = QtGui.QApplication(argv)

  SMSMain = Main(app)
  SMSMain.show()
  exit(app.exec_())

