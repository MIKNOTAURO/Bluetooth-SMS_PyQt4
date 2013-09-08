#!/usr/bin/env python

# -*- coding: utf-8 -*-

from sys import argv, exit

from time import sleep

import bluetooth, functools, threading

from PyQt4.QtCore import QTranslator, QThread

from PyQt4.QtGui import QApplication, QVBoxLayout, QHBoxLayout
from PyQt4.QtGui import QMainWindow, QDialog, QFrame
from PyQt4.QtGui import QLabel, QRadioButton, QMessageBox

from SMS import Ui_SMS
from SMS_Help import Ui_Help
from SMS_Send import Ui_SMSDetails

class Help(QDialog):
  def __init__(self):
    QDialog.__init__(self)

    self.ui = Ui_Help()
    self.ui.setupUi(self)


class Main(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)

    self.ui = Ui_SMS()
    self.ui.setupUi(self)

    self.ui.actionRefresh.triggered.connect(self.refreshTriggered)
    self.ui.actionSend.triggered.connect(self.sendTriggered)
    self.ui.actionInbox.triggered.connect(self.inboxTriggered)
    self.ui.actionHelp.triggered.connect(self.helpTriggered)

    self.widgetLayout = QVBoxLayout()

    self.address = ""
    self.channel = 0


  def helpTriggered(self):
    aux = Help()
    aux.exec_()


  def testConnection(self):
    self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    services = bluetooth.find_service(address = self.address)
    if len(services) > 0:
      self.info = self.tr('Please wait ...\n')
      self.info += self.tr('Looking for Dial-up networking service...\n\n\n')
      for service in services:
        name = service["name"]
        if name == "Dial-up networking" or name == "Dial-Up Networking" or name == "Dial-up Networking":
          self.channel = service["port"]
          self.info += self.tr("Found Dial-up networking at channel ") + "%d" % self.channel
          message_title = self.tr("Information")
          QMessageBox.information(self, message_title, self.info)
          break
    else:
      error = self.tr("No available services\nTry another device, please.")
      message_title = self.tr("Error message")
      QMessageBox.critical(self, message_title, error)
      return

    if self.channel == 0:
      error = self.tr("No Dial-up networking service detected!\nTry another device, please.")
      message_title = self.tr("Error message")
      QMessageBox.critical(self, message_title, error)
      return


  def connectToDevice(self):
    self.socket.connect((self.address, self.channel))


  def inboxTriggered(self):
    self.testConnection()
    if self.channel == 0:
      return

    self.connectToDevice()
    self.channel = 0

    self.clearLayout(self.widgetLayout)

    self.socket.send('AT+CMGL="ALL"\r')
    print self.socket.recv(1024)

    self.socket.close()


  def sendTriggered(self):
    self.testConnection()
    if self.channel == 0:
      return

    edit_sms = QDialog()
    aux = Ui_SMSDetails()
    aux.setupUi(edit_sms)

    r = edit_sms.exec_()

    if r:
      phone_number = str(aux.lineEdit.text())
      sms_data = str(aux.plainTextEdit.toPlainText())
      for addr, name in self.devices:
        if addr == self.address:
          self.connectToDevice()
          self.channel = 0

          mobile	= '52' + phone_number

          self.socket.send('AT+CMGF=1\r')
          sleep(2)
          print self.socket.recv(1024)
          command	= 'AT+CMGS="+' + mobile + '"\r'
          print "%r" % command
          self.socket.send(command)
          sleep(2)
          print self.socket.recv(1024)
          self.socket.send(sms_data+chr(26))
          sleep(2)
          print self.socket.recv(1024)
          self.socket.close()



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
    self.ui.actionInbox.setEnabled(True)
    self.ui.actionSend.setEnabled(True)
    self.address = address


  def refreshDevices(self):
    self.devices = bluetooth.discover_devices(lookup_names = True)


  def refreshTriggered(self):
    self.clearLayout(self.widgetLayout)

    self.widgetLayout.addWidget(QLabel(self.tr("No bluetooth devices found.")))
    self.ui.scrollAreaWidgetContents.setLayout(self.widgetLayout)
    self.refreshDevices()
    self.clearLayout(self.widgetLayout)

    if len(self.devices) > 0:
      self.clearLayout(self.widgetLayout)
      self.ui.actionSend.setEnabled(False)
      self.ui.actionInbox.setEnabled(False)
      message = QLabel(self.tr("Chose from the mobile devices below:"))

      self.widgetLayout.addWidget(message)

      separator = QFrame()
      separator.setFrameShape(QFrame.HLine)
      separator.setFrameShadow(QFrame.Sunken)

      self.widgetLayout.addWidget(separator)

      for address, name in self.devices:
        deviceName = QLabel(" " + address)
        radio = QRadioButton(name)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)

        self.widgetLayout.addWidget(radio)
        self.widgetLayout.addWidget(deviceName)
        self.widgetLayout.addWidget(separator)

        radio.toggled.connect(functools.partial(self.radioToggled, address))

      self.ui.scrollAreaWidgetContents.setLayout(self.widgetLayout)
      self.widgetLayout.addStretch(1)
    else:
      self.widgetLayout.addWidget(QLabel(self.tr("No bluetooth devices found.")))
      self.ui.scrollAreaWidgetContents.setLayout(self.widgetLayout)


if __name__ == "__main__":
  app = QApplication(argv)

  translator = QTranslator(app)
  translator.load("lang_es")
  app.installTranslator(translator)

  SMSMain = Main()
  SMSMain.show()
  exit(app.exec_())


