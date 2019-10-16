# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_receive.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QTextEdit


class UiReceiveWidget(QWidget):
    def __init__(self):
        super(UiReceiveWidget, self).__init__()

        self.setMinimumSize(QtCore.QSize(280, 460))
        self.setMaximumSize(QtCore.QSize(300, 460))

        # layout = QGridLayout(self)
        self.receive_box = QTextEdit(self)
        self.receive_box.resize(280, 460)
        # layout.addWidget(self.receive_box, 0, 0, 1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiReceiveWidget()
    ex.show()
    sys.exit(app.exec_())