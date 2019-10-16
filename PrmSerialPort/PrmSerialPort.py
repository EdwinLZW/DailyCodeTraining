# -*- coding: utf-8 -*-
__author__ = 'zhouwu.liu'
__version__ = 'v0.0.3'


from PyQt5.QtGui import QIcon, QBrush, QPixmap

from Contral import *


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
        self.setGeometry(300, 300, 876, 900)
        # 创建MdiArea控件
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        # self.mdi.setBackground(QBrush(QPixmap("./images/background.jpg")))

        # self.setWindowTitle("PrmSerialPort {}".format(__version__))

    def initUI(self):

        newMenu = QMenu('新建文件(&S)', self)
        newTcpAct = QAction(QIcon('./images/new.jpeg'), 'TCPClient', self)
        newTcpAct.setShortcut('Ctrl+Shift+T')
        newTcpAct.setStatusTip('TCPClient')
        newSerAct = QAction(QIcon('./images/new.jpeg'), 'SerialPort', self)
        newSerAct.setShortcut('Ctrl+Shift+S')
        newSerAct.setStatusTip('SerialPort')
        newMenu.addAction(newTcpAct)
        newMenu.addAction(newSerAct)
        newMenu.triggered.connect(self.creat_subwindow)

        exitAct = QAction(QIcon('./images/exit.jpeg'), '退出', self)  # 创建一个具有特定图标和“退出”标签的动作
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出程序')

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('项目')
        fileMenu.addMenu(newMenu)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAct)
        fileMenu.triggered.connect(self.creat_subwindow)

    def creat_subwindow(self, q):

        # 选择“New”则新建一个子窗口并显示，每创建一个子窗口则子窗口名称数增加1
        if q.text().encode('utf8') == "TCPClient":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(UiSerialPort('TCP'))
            # sub.setMinimumSize(QtCore.QSize(885, 800))
            sub.setMaximumSize(QtCore.QSize(885, 800))
            sub.setWindowTitle("PrmTcpPort")
            self.mdi.addSubWindow(sub)
            sub.show()

        elif q.text().encode('utf8') == "SerialPort":
            MainWindow.count = MainWindow.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(UiSerialPort('Serial'))
            # sub.setMinimumSize(QtCore.QSize(885, 800))
            sub.setMaximumSize(QtCore.QSize(885, 800))
            sub.setWindowTitle("PrmSerialPort")
            self.mdi.addSubWindow(sub)
            sub.show()

        # 选择“cascade”则将创建的子窗口层叠显示
        if q.text().encode('utf8') == "退出":
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())
