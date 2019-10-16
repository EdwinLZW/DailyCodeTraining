# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame3_serialport_setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton, QRadioButton, \
    QButtonGroup

BAUDRATE_LIST = [300, 600, 1200, 1800, 2400, 3600, 4800, 7200, 9600, 14400, 19200, 28800, 38400, 57600,
                 76800, 115200, 230400]
DATABITS_LIST = [8, 7, 6, 5]
PARITY_LIST = ['None', 'Odd', 'Even']
STOPBOTS_ITEM = [1, 1, 5, 2]
HANDSHAKE_LIST = ["None", "RTC/CTS", "DTR/DSR", "DCD"]


class UiSerialSendWidget(QWidget):
    def __init__(self):
        super(UiSerialSendWidget, self).__init__()
        #     self.initUI()
        #
        # def initUI(self):

        self.setMinimumSize(QtCore.QSize(280, 240))
        self.setMaximumSize(QtCore.QSize(280, 240))

        self.lbl_port = QLabel("port:", self)
        # self.lbl_port.setStyleSheet("font: 12pt \".SF NS Text\";")
        self.combobox_port = QComboBox(self)
        self.lbl_baudrate = QLabel("BaudRate:", self)
        self.combobox_baudrate = QComboBox(self)
        self.lbl_baudrate.setBuddy(self.combobox_baudrate)
        self.combobox_baudrate.addItems(map(str, BAUDRATE_LIST))

        self.lbl_databits = QLabel("DataBits:", self)
        self.combobox_databits = QComboBox(self)
        self.combobox_databits.addItems(map(str, DATABITS_LIST))
        self.lbl_databits.setBuddy(self.combobox_databits)

        self.lbl_stopbit = QLabel("StopBits:", self)
        self.combobox_stopbit = QComboBox(self)
        self.combobox_stopbit.addItems(map(str, STOPBOTS_ITEM))
        self.lbl_stopbit.setBuddy(self.combobox_stopbit)

        self.lbl_parity = QLabel("Parity:", self)
        self.combobox_parity = QComboBox(self)
        self.combobox_parity.addItems(map(str, PARITY_LIST))
        self.lbl_parity.setBuddy(self.combobox_parity)

        self.lbl_handshake = QLabel("HandShake:", self)
        self.combobox_handshake = QComboBox(self)
        self.combobox_handshake.addItems(map(str, HANDSHAKE_LIST))
        self.lbl_handshake.setBuddy(self.combobox_handshake)

        self.lbl_connect_tip = QLabel("disconnected", self)
        self.group_connect = QButtonGroup()
        self.btn_disconnect = QPushButton("断开", self)
        self.btn_connect = QPushButton("连接", self)
        self.btn_disconnect.setChecked(True)
        self.btn_disconnect.setDisabled(True)
        self.btn_connect.setChecked(True)
        self.group_connect.addButton(self.btn_connect)
        self.group_connect.addButton(self.btn_disconnect)

        self.btn_refresh = QPushButton("刷新", self)

        layout = QGridLayout(self)
        layout.addWidget(self.lbl_port, 0, 0, 1, 2)
        layout.addWidget(self.combobox_port, 0, 2, 1, 8)

        layout.addWidget(self.lbl_baudrate, 1, 0, 1, 2)
        layout.addWidget(self.combobox_baudrate, 1, 2, 1, 4)
        layout.addWidget(self.btn_refresh, 1, 6, 1, 4)

        layout.addWidget(self.lbl_databits, 3, 0, 1, 2)
        layout.addWidget(self.combobox_databits, 3, 2, 1, 4)

        layout.addWidget(self.lbl_stopbit, 4, 0, 1, 2)
        layout.addWidget(self.combobox_stopbit, 4, 2, 1, 4)

        layout.addWidget(self.lbl_parity, 5, 0, 1, 2)
        layout.addWidget(self.combobox_parity, 5, 2, 1, 4)

        layout.addWidget(self.lbl_handshake, 6, 0, 1, 2)
        layout.addWidget(self.combobox_handshake, 6, 2, 1, 4)

        layout.addWidget(self.btn_connect, 7, 0, 1, 2)
        layout.addWidget(self.btn_disconnect, 7, 2, 1, 2)

        layout.addWidget(self.lbl_connect_tip, 8, 0, 1, 5)
        layout.setSpacing(2)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiSerialSendWidget()
    ex.show()
    sys.exit(app.exec_())
