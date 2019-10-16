#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouwu.liu'
from PyQt5 import QtCore

from PyQt5.QtWidgets import QWidget, QCheckBox, QPushButton, QLabel, QApplication, QLineEdit
from PyQt5.QtCore import pyqtSignal, Qt


class UiPropretyWidgetHeader(QWidget):

    pro_header_sig = pyqtSignal(bool)

    def __init__(self):
        super(UiPropretyWidgetHeader, self).__init__()

        # self.pro_header_sig.connect()

        self.order_sort = QLabel("顺序", self)
        self.order_sort.setGeometry(QtCore.QRect(485, 20, 31, 21))

        self.hex = QLabel("Hex", self)
        self.hex.setGeometry(QtCore.QRect(0, 40, 31, 16))

        self.delete = QPushButton("-", self)
        self.delete.setGeometry(QtCore.QRect(380, 40, 21, 20))

        self.char_commend = QLabel("字符串(双击注释)", self)
        self.char_commend.setGeometry(QtCore.QRect(30, 40, 101, 16))

        self.cycle_send = QCheckBox("循环发送", self)
        # self.cycle_send.clicked.connect(self.dealwith)
        self.cycle_send.setGeometry(QtCore.QRect(0, 10, 87, 20))

        self.cycle_send_num = QLineEdit("10", self)
        self.cycle_send_num.setEnabled(False)
        self.cycle_send_num.setGeometry(QtCore.QRect(80, 10, 31, 20))

        self.lb_cycle_send = QLabel("次", self)
        self.lb_cycle_send.setGeometry(QtCore.QRect(115, 10, 21, 20))

        self.help = QPushButton("多条帮助", self)
        self.help.setGeometry(QtCore.QRect(150, 10, 81, 21))

        self.importini = QPushButton("导入ini", self)
        self.importini.setGeometry(QtCore.QRect(230, 10, 71, 21))

        self.delay_unit = QLabel("ms", self)
        self.delay_unit.setGeometry(QtCore.QRect(520, 40, 21, 16))

        self.add = QPushButton("+", self)
        self.add.setGeometry(QtCore.QRect(360, 40, 21, 20))

        self.delay = QLabel("延时", self)
        self.delay.setGeometry(QtCore.QRect(520, 20, 31, 21))

        self.order_send = QCheckBox("顺序发送", self)
        self.order_send.setGeometry(QtCore.QRect(400, 40, 81, 20))

    # def dealwith(self):
    #     if self.cycle_send.checkState() == Qt.Checked:
    #         self.cycle_send_num.setEnabled(True)
    #     else:
    #         self.cycle_send_num.setEnabled(False)

import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiPropretyWidgetHeader()
    ex.show()
    sys.exit(app.exec_())
