#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouwu.liu'

from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal, QThread, pyqtSlot
from UIwidget import *
from PyQt5.QtWidgets import *
import csv
from functools import partial
import threading
import time


class UiSerialPort(QWidget):
    def __init__(self, flag=None):
        super(UiSerialPort, self).__init__()

        self.cmd_content = None
        self.cmd_msg = dict()
        self.cmdlist = list()
        self.cyclenum = 10

        self.flag = flag
        self.setMaximumSize(QtCore.QSize(885, 800))
        self.send = UiSendWidget()
        self.propreheader = UiPropretyWidgetHeader()
        self.proprebotton = UiPropretyWidgetBotton()
        self.serial = UiSerialSendWidget()
        self.tcpset = UiTcpSendWidget()
        self.receive = UiReceiveWidget()

        self.propretyevent()
        self.sendevent()

        self.initUI()

    def initUI(self):
        glayout = QGridLayout()
        glayout.addWidget(self.propreheader, 0, 0, 1, 1)
        glayout.addWidget(self.proprebotton, 1, 0, 6, 1)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.receive)
        hlayout.addLayout(glayout)

        hlayout2 = QHBoxLayout()
        if self.flag == 'TCP':
            hlayout2.addWidget(self.tcpset)
        else:
            hlayout2.addWidget(self.serial)
        hlayout2.addWidget(self.send)

        vlayout2 = QVBoxLayout()
        vlayout2.addLayout(hlayout)
        vlayout2.addLayout(hlayout2)

        self.setLayout(vlayout2)

    def propretyevent(self):
        self.propreheader.delete.clicked.connect(self.deletecommandwidget)
        self.propreheader.add.clicked.connect(self.creatcommandwidget)
        self.propreheader.cycle_send.clicked.connect(self.enablecyclesend)
        self.proprebotton.itemClicked.connect(self.clicktest)

    def sendevent(self):
        self.send.open_file.clicked.connect(self.openfile)
        self.send.send_file.clicked.connect(self.sendcommandprofile)
        self.send.clean_window.clicked.connect(self.receivewindowclear)
        self.send.clean_send_box.clicked.connect(self.sendboxclear)
        self.send.sendbotton.clicked.connect(self.sendmessage)

    # propretyevent func
    def creatcommandwidget(self):
        flagrow = self.proprebotton.rowCount()
        self.proprebotton.insertRow(flagrow)
        self.addcommandwidget(flagrow)

    def deletecommandwidget(self):
        try:
            if self.proprebotton.rowCount() > 0:
                self.proprebotton.removeRow(self.proprebotton.rowCount() - 1)
                self.cmd_msg.pop('row{}'.format(self.proprebotton.rowCount()))
                # self.sss = self.dealordersendmsg()
            # print self.cmd_msg
        except Exception as e:
            pass

    def enablecyclesend(self):
        if self.propreheader.cycle_send.checkState() == Qt.Checked:
            self.propreheader.cycle_send_num.setEnabled(True)
        else:
            self.propreheader.cycle_send_num.setEnabled(False)

    # sendevent func
    def openfile(self):
        try:
            fname = QFileDialog.getOpenFileName(self, '打开文件','./')
            if fname[0]:
                with open(fname[0], 'rb') as f:
                    csv_obj = csv.DictReader(f)
                    self.cmd_content = [row for row in csv_obj]
                self.send.file_path.setText(fname[0])
        except Exception as e:
            pass

    def sendcommandprofile(self):
        try:
            flagrow = self.proprebotton.rowCount()
            for id, item in enumerate(self.cmd_content):
                # print id, item
                self.proprebotton.insertRow(flagrow + id)
                self.addcommandwidget(flag=flagrow + id, cmdmsg=item)
                # self.sss = self.dealordersendmsg()
            # print self.cmd_msg
        except Exception as e:
            print e

    def receivewindowclear(self):
        self.receive.receive_box.clear()

    def sendboxclear(self):
        self.send.send_box.clear()

    def sendmessage(self):
        if self.propreheader.order_send.checkState() == Qt.Checked:
            if self.propreheader.cycle_send.checkState() == Qt.Checked:
                cyclenum = self.propreheader.cycle_send_num.text()
                # print cyclenum, type(cyclenum)
                cmdlist = self.dealordersendmsg()
                print cmdlist
                # self.cyclesendcmmand(int(cyclenum), cmdlist)
                # pass

    # other func
    def addcommandwidget(self, flag=None, cmdmsg=None):
        self.defaultcmd = dict()
        if cmdmsg:
            if type(cmdmsg['CmdName']) is not str:
                cmdmsg['CmdName'] = cmdmsg['CmdName'].text()
            checkbox = QCheckBox()
            if cmdmsg['Hex'] == '1':
                checkbox.toggle()
            btn = QPushButton('{}'.format(cmdmsg['CmdName']))
            btn.clicked.connect(partial(self.propresendcommand, flag))
            self.proprebotton.setCellWidget(flag, 0, checkbox)
            self.proprebotton.setCellWidget(flag, 2, btn)
            newItem1 = QTableWidgetItem('{}'.format(cmdmsg['Command']))
            self.proprebotton.setItem(flag, 1, newItem1)
            newItem2 = QTableWidgetItem('{}'.format(cmdmsg['Sort']))
            self.proprebotton.setItem(flag, 3, newItem2)
            newItem3 = QTableWidgetItem('{}'.format(cmdmsg['Delay']))
            self.proprebotton.setItem(flag, 4, newItem3)
            cmdmsg['CmdName'] = btn
            self.cmd_msg.setdefault('row{}'.format(flag), cmdmsg)

        else:
            checkbox = QCheckBox()
            btn = QPushButton('Send')
            btn.clicked.connect(partial(self.propresendcommand, flag))
            self.proprebotton.setCellWidget(flag, 0, checkbox)
            self.proprebotton.setCellWidget(flag, 2, btn)
            newItem1 = QTableWidgetItem('')
            self.proprebotton.setItem(flag, 1, newItem1)
            newItem2 = QTableWidgetItem('0')
            self.proprebotton.setItem(flag, 3, newItem2)
            newItem3 = QTableWidgetItem('1000')
            self.proprebotton.setItem(flag, 4, newItem3)
            self.defaultcmd.setdefault('Hex', '0')
            self.defaultcmd.setdefault('Command', newItem1.text())
            self.defaultcmd.setdefault('CmdName', btn)
            self.defaultcmd.setdefault('Sort', newItem2.text())
            self.defaultcmd.setdefault('Delay', newItem3.text())
            self.cmd_msg.setdefault('row{}'.format(flag), self.defaultcmd)

    def propresendcommand(self, rowindx):
        try:
            currentrowmsg = self.cmd_msg['row{}'.format(rowindx)]
            currentrowmsg['Command'] = self.proprebotton.item(rowindx, 1).text()
            sendcmd = currentrowmsg['Command']
            if not sendcmd:
                QMessageBox.warning(QMessageBox(), "ATTENTION", "Command is None,please add!")
                return
            self.receive.receive_box.append(sendcmd)
            self.cmd_msg['row{}'.format(rowindx)]['Sort'] = self.proprebotton.item(rowindx, 3).text()
            self.cmd_msg['row{}'.format(rowindx)]['Delay'] = self.proprebotton.item(rowindx, 4).text()
            self.cmd_msg['row{}'.format(rowindx)]['Command'] = currentrowmsg['Command']
        except Exception as e:
            QMessageBox.warning(QMessageBox(), "ATTENTION", "Error-{}".format(e))

    def dealordersendmsg(self):
        cycle_command = list()
        ordercmd = dict()
        for key, value in self.cmd_msg.items():
            ordercmd.setdefault(value['Sort'], value['CmdName'].text())
        for i in sorted(ordercmd.items()):
            cycle_command.append(i[1])
        return cycle_command

    def cyclesendcmmand(self, num, cmdlist):
        for i in range(num):
            for i in cmdlist:
                time.sleep(1)
                self.receive.receive_box.append(i)

    def clicktest(self):
        row = self.proprebotton.sender().currentRow()
        column = self.proprebotton.sender().currentColumn()
        # print ">>>>>>>>>>>", row, column
        if self.proprebotton.sender():
            self.proprebotton.itemChanged.connect(partial(self.test, row, column))

    @pyqtSlot()
    def test(self, row, column):
        if column == 1:
            self.cmd_msg['row{}'.format(row)]['Command'] = self.proprebotton.item(row, column).text()
        if column == 3:
            self.cmd_msg['row{}'.format(row)]['Sort'] = self.proprebotton.item(row, column).text()
        if column == 4:
            self.cmd_msg['row{}'.format(row)]['Delay'] = self.proprebotton.item(row, column).text()
        self.proprebotton.itemChanged.disconnect()
        print self.cmd_msg


    # TODO API



