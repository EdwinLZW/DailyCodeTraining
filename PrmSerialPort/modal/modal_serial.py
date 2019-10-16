from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox
from GUI.ui_widgets.serial_window import SerialWindow
import serial.tools.list_ports as liports
from modal.k_drivers import SerialPort
import time


class ModalSerial(QObject):
    receive_signal = pyqtSignal(str, name='serial_receive')

    def __init__(self):
        super(ModalSerial, self).__init__()
        self.window = SerialWindow()
        self.fresh_port()
        self.register_events()
        self.serialport = None
        self._connected = False

    def fresh_port(self):
        port_list = []
        for port, _, _ in sorted(liports.comports()):
            if port:
                port_list.append(port)
        self.window.send_widget.port_choose.addItems(port_list)

    def connect(self):
        print 'connecting'
        portname = self.window.send_widget.port_choose.currentText()
        baudrate = self.window.send_widget.baudrate.currentText()
        try:
            self.serialport = SerialPort(portname, int(baudrate), recv_signal=self.receive_signal)
            self._connected = True
        except Exception:
            self.window.send_widget.discon_state.setChecked(True)
            QMessageBox.warning(self.window, 'port error', 'can not connect to port {}'.format(portname))
            # raise RuntimeError(Exception)
        if self._connected:
            self.window.send_widget.con_state.setChecked(True)
            self.window.send_widget.connect.setDisabled(True)
            self.window.send_widget.disconnect.setEnabled(True)
            self.window.send_widget.port_choose.setDisabled(True)

    def close(self):
        self.serialport.close()
        self.window.send_widget.discon_state.setChecked(True)
        self.window.send_widget.connect.setEnabled(True)
        self.window.send_widget.disconnect.setDisabled(True)
        self.window.send_widget.port_choose.setEnabled(True)

    def register_events(self):
        self.receive_signal.connect(self.display_receive_data)
        self.window.send_widget.connect.clicked.connect(self.connect)
        self.window.send_widget.disconnect.clicked.connect(self.close)
        self.window.multi_widget.scrollAreaWidgetContents.children()

    def display_receive_data(self, data):
        self.window.recv_widget.receive_box.insertPlainText(data)
        # move scrollbar to end
        self.window.recv_widget.receive_box.moveCursor(11)
