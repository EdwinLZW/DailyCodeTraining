# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame3_tcp_setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QComboBox, QLineEdit, QPushButton, QRadioButton

_translate = QtCore.QCoreApplication.translate


class UiTcpSendWidget(QWidget):
    def __init__(self):
        super(UiTcpSendWidget, self).__init__()
    #     self.initUI()
    #
    # def initUI(self):
        self.setMinimumSize(QtCore.QSize(280, 240))
        self.setMaximumSize(QtCore.QSize(280, 240))

        layout = QGridLayout(self)

        self.port = QLabel("端口号", self)
        self.port_choose = QComboBox(self)
        self.port_choose.addItem("TCPClient")
        self.ip_addr = QLabel("IP地址", self)
        self.ip_addrtext = QLineEdit("169.254.1.32", self)
        self.ip_port = QLabel("Port", self)
        self.ip_porttext = QLineEdit("7600", self)
        self.connect = QPushButton("连接", self)
        self.con_state = QRadioButton(self)
        self.disconnect = QPushButton("断开", self)
        self.discon_state = QRadioButton(self)
        self.state = QLabel("TCPClient Connect!", self)
        self.renew = QPushButton("刷新", self)

        layout.addWidget(self.port, 0, 0, 1, 1)
        layout.addWidget(self.port_choose, 0, 1, 1, 3)
        layout.addWidget(self.ip_addr, 1, 0, 1, 1)
        layout.addWidget(self.ip_addrtext, 1, 1, 1, 1)
        layout.addWidget(self.ip_port, 2, 0, 1, 1)
        layout.addWidget(self.ip_porttext, 2, 1, 1, 1)
        layout.addWidget(self.connect, 2, 2, 1, 1)
        layout.addWidget(self.con_state, 2, 3, 1, 1)
        layout.addWidget(self.disconnect, 3, 2, 1, 1)
        layout.addWidget(self.discon_state, 3, 3, 1, 1)
        layout.addWidget(self.state, 4, 0, 1, 4)
        layout.addWidget(self.renew, 1, 2, 1, 2)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiTcpSendWidget()
    ex.show()
    sys.exit(app.exec_())