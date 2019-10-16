#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'zhouwu.liu'

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import *


class UiPropretyWidgetBotton(QTableWidget):

    pro_btn_sig = pyqtSignal(dict)

    def __init__(self):
        super(UiPropretyWidgetBotton, self).__init__(0, 5)
        # self.setGeometry(0,0,10,10)
        self.setMouseTracking(True)
        # self.connect(self, QtCore.SIGNAL(cellEntered(int, int)), this, SLOT(MouseTrackItem(int, int)))

        # Todo 设置水平方向的表头标签与垂直方向上的表头标签，注意必须在初始化行列之后进行，否则，没有效果
        # TableWidget.setHorizontalHeaderLabels(['a','b','c'])

        # TODO 网格线显示
        # self.setShowGrid(False)

        # Todo 设置垂直方向的表头标签
        # TableWidget.setVerticalHeaderLabels(['1', '2', '3', '4'])

        # TODO 设置水平方向表格为自适应的伸缩模式
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)

        # TODO 将表格变为禁止编辑
        # TableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # TODO 设置表格整行选中
        # self.setSelectionBehavior(QAbstractItemView.SelectRows)

        # TODO 将行与列的高度设置为所显示的内容的宽度高度匹配
        self.resizeColumnsToContents()
        # self.resizeRowsToContents()

        # TODO 表格头的显示与隐藏
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)

        # TODO 在单元格内放置控件
        # for i in range(10):
        #     checkbox = QCheckBox()
        #     btn = QPushButton('URAT SET GCUF EHFIO')
        #     self.setCellWidget(i, 0, checkbox)
        #     self.setCellWidget(i, 2, btn)
        #     # 添加数据
        #     newItem=QTableWidgetItem('0')
        #     self.setItem(i, 3, newItem)
        #
        #     newItem=QTableWidgetItem('1000')
        #     self.setItem(i, 4, newItem)

        # TODO 将行与列的高度设置
        # self.setColumnWidth(0,20)
        # self.setRowHeight(0,20)

        # TODO 合并单元格

        # TODO 单元格激活
        # self.itemActivated()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=UiPropretyWidgetBotton()
    # win.addcommandwidget(2)
    win.show()
    sys.exit(app.exec_())
