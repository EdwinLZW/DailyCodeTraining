# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame4_sendwidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QCheckBox, QLineEdit, QPushButton

_translate = QtCore.QCoreApplication.translate


class UiSendWidget(QWidget):
    def __init__(self):
        super(UiSendWidget, self).__init__()

        self.widget = QWidget(self)
        self.widget.setMinimumSize(QtCore.QSize(570, 225))
        self.widget.setMaximumSize(QtCore.QSize(570, 225))

        self.send_box = QLineEdit(self.widget)
        self.send_box.setGeometry(QtCore.QRect(110, 130, 441, 41))

        self.file_path = QLineEdit(self.widget)
        self.file_path.setGeometry(QtCore.QRect(150, 15, 181, 21))

        self.clean_send_box = QPushButton("清空发送区", self.widget)
        self.clean_send_box.setGeometry(QtCore.QRect(10, 190, 91, 31))
        self.clean_send_box.setStyleSheet("font: 12pt \".SF NS Text\";")
        self.stop = QPushButton("停止", self.widget)
        self.stop.setGeometry(QtCore.QRect(100, 190, 51, 31))
        self.stop.setStyleSheet("font: 12pt \".SF NS Text\";")
        self.receive_data_to_file = QCheckBox("接受数据到文件", self.widget)
        self.receive_data_to_file.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.receive_data_to_file.setStyleSheet("font: 12pt \".SF NS Text\";")
        self.hex_display = QCheckBox("Hex显示", self.widget)
        self.hex_display.setGeometry(QtCore.QRect(10, 50, 71, 31))
        self.hex_display.setStyleSheet("font: 12pt \".SF NS Text\";")
        self.hide = QPushButton("隐藏", self.widget)
        self.hide.setGeometry(QtCore.QRect(490, 10, 51, 32))
        self.hide.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.open_file = QPushButton("打开文件", self.widget)
        self.open_file.setGeometry(QtCore.QRect(80, 10, 71, 32))
        self.open_file.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.timed_sending_edit = QLineEdit("7600", self.widget)
        self.timed_sending_edit.setGeometry(QtCore.QRect(280, 90, 41, 21))

        self.timed_sending_unit = QLabel("ms/次", self.widget)
        self.timed_sending_unit.setGeometry(QtCore.QRect(320, 90, 41, 21))
        self.timed_sending_unit.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.timeout_unit = QLabel("ms", self.widget)
        self.timeout_unit.setGeometry(QtCore.QRect(180, 90, 21, 21))
        self.timeout_unit.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.save_parameter = QPushButton("保存参数", self.widget)
        self.save_parameter.setGeometry(QtCore.QRect(410, 10, 71, 32))
        self.save_parameter.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.front_check = QCheckBox("最前", self.widget)
        self.front_check.setGeometry(QtCore.QRect(270, 50, 51, 21))

        self.front_check.setObjectName("front_check")
        self.save_data = QPushButton("保存数据", self.widget)
        self.save_data.setGeometry(QtCore.QRect(80, 50, 71, 32))
        self.save_data.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.timed_sending = QCheckBox("定时发送", self.widget)
        self.timed_sending.setGeometry(QtCore.QRect(210, 80, 71, 41))
        self.timed_sending.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.timeout = QLabel("超时时间", self.widget)
        self.timeout.setGeometry(QtCore.QRect(90, 90, 51, 21))
        self.timeout.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.clean_window = QPushButton("清除窗口", self.widget)
        self.clean_window.setGeometry(QtCore.QRect(10, 10, 71, 32))
        self.clean_window.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.send_file = QPushButton("发送文件", self.widget)
        self.send_file.setGeometry(QtCore.QRect(340, 10, 71, 32))
        self.send_file.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.endlish_check = QCheckBox("English", self.widget)
        self.endlish_check.setGeometry(QtCore.QRect(320, 50, 61, 20))
        self.endlish_check.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.add_enter_wrap = QCheckBox("加回车换行", self.widget)
        self.add_enter_wrap.setGeometry(QtCore.QRect(360, 80, 81, 41))
        self.add_enter_wrap.setStyleSheet("font: 12pt \".SF NS Text\";")
        self.timeout_edit = QLineEdit("20", self.widget)
        self.timeout_edit.setGeometry(QtCore.QRect(140, 90, 41, 21))
        self.add_timestamp_subcontracting = QCheckBox("加时间戳和分包", self.widget)
        self.add_timestamp_subcontracting.setGeometry(QtCore.QRect(450, 80, 111, 41))
        self.add_timestamp_subcontracting.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.hex_send = QCheckBox("Hex发送", self.widget)
        self.hex_send.setGeometry(QtCore.QRect(10, 80, 71, 41))
        self.hex_send.setStyleSheet("font: 12pt \".SF NS Text\";")

        self.sendbotton = QPushButton("发送", self.widget)
        self.sendbotton.setGeometry(QtCore.QRect(10, 130, 91, 41))
        self.sendbotton.setStyleSheet("font: 24pt \".SF NS Text\";")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiSendWidget()
    ex.show()
    sys.exit(app.exec_())