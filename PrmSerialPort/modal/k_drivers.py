__Author__ = "jinhui.huang"

import serial
import socket
import time
import datetime
import select
import threading
from abc import abstractmethod, ABCMeta, abstractproperty
from threading import Thread


def print_with_time(info):
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f --------> {}'.format(info))


class AbstractDevice(object):
    __metaclass__ = ABCMeta

    def __init__(self, publisher=None):
        self.publisher = publisher

    def log(self, msg):
        print_with_time(msg)

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractproperty
    def is_open(self):
        pass

    @abstractmethod
    def send(self, cmd, description=''):
        pass

    @abstractmethod
    def send_by_byte(self, cmd, interval=0.005, description=''):
        pass

    @abstractmethod
    def set_timeout(self, timeout=3000):
        """
        set communication timeout
        :param timeout: ms
        :return:
        """
        pass

    @abstractmethod
    def read_string(self):
        pass

    @abstractmethod
    def set_detect_string(self, string):
        pass

    @abstractmethod
    def wait_detect(self):
        pass


class SerialPort(AbstractDevice):
    def __init__(self, portname, baudrate=921600, timeout=6, end_str='\n', recv_signal=None):
        super(SerialPort, self).__init__()
        self._portname = portname
        self._baudrate = baudrate
        self._timeout = timeout
        self._end_str = end_str
        self._b_read_in_background = False
        self._detect_str = ''
        self._port = None
        self._str_buffer = ''
        self._lock = threading.Lock()
        self._recv_signal = recv_signal
        self.connect()

    def connect(self):
        if not self.is_open():
            # if not serial not open, then reopen.
            try:
                self._port = serial.Serial(self._portname, baudrate=self._baudrate, timeout=self._timeout)
                self._b_read_in_background = True
            except Exception:
                raise RuntimeError("Open serial port error: %s", self._portname)

            if self._b_read_in_background:
                t = Thread(target=self._read_data_in_background, name=self._portname)
                t.setDaemon(True)
                t.start()

    def close(self):
        if self._port.isOpen():
            self._port.flush()
            self._port.close()
            self._b_read_in_background = False

    def send(self, cmd, description=''):
        if self._port.isOpen():
            self._port.flushInput()
            self._port.flushOutput()
            self._port.write(cmd + self._end_str)
            self.log(description + '[Send:]' + cmd + self._end_str)
        else:
            raise RuntimeError("Cmd send error, port not open: %s", self._port.name)

    def send_by_byte(self, cmd, interval=0.005, description=''):
        if self._port.isOpen():
            self._port.flushInput()
            self._port.flushOutput()
            self.log(cmd)
            for sc in cmd:
                self._port.write(sc)
                time.sleep(interval)
            self._port.write(self._end_str)
            self.log(description + '[Send:]' + cmd + self._end_str)
        else:
            raise RuntimeError("Cmd send error, port not open: %s", self._port.name)

    def set_timeout(self, timeout=3000):
        self._timeout = timeout / 1000.0
        self._port.timeout = self._timeout

    def is_open(self):
        try:
            return self._port.isOpen()
        except Exception:
            return False

    def read_string(self):
        """
        read all buffer data, and then empty buffer
        :return:
        """
        return_str = ''
        if self._lock.acquire(True):
            return_str = self._str_buffer
            self._str_buffer = ''
            self._lock.release()
        return return_str

    def wait_detect(self, timeout=6):
        """
        wait detect string until timout
        :param timeout:
        :return:
        """
        detect = False
        timeout_happen = False
        begin = time.time()
        if self.is_open():
            # detect string until found or timeout
            while True:
                if self._lock.acquire(True):
                    detect = self._detect_str in self._str_buffer
                self._lock.release()
                if detect:
                    break
                if time.time() - begin > timeout:
                    timeout_happen = True
                    break
                else:
                    time.sleep(0.05)
            if timeout_happen:
                return False, 'timeout'
            else:
                return detect, self._detect_str

    def set_detect_string(self, string):
        """
        set detect string
        :param string:
        :return:
        """
        self._detect_str = string

    def _read_existing(self):
        res = self._port.read(self._port.inWaiting())
        if res != "":
            self.log('[Receive:]' + res)
        return res

    def _read_data_in_background(self):
        """
        read data in a single thread
        :return:
        """
        while self._b_read_in_background:
            ret, _, _ = select.select([self._port], [], [], 0)
            if ret:
                self._analysis_data(self._read_existing())
            time.sleep(0.001)

    def _analysis_data(self, data):
        """
        analysis the input data
        :param data:
        :return:
        """
        self._recv_signal.emit(data)
        self._recv_signal.emit(self._end_str)

        if self._lock.acquire(True):
            self._str_buffer += data
        self._lock.release()


class TcpSocket(AbstractDevice):
    def __init__(self, ip, port, end_str='\r\n', timeout=0.5, publisher=None):
        super(TcpSocket, self).__init__(publisher)
        self._ip = ip
        self._port = port
        self._end_str = end_str
        self._timeout = timeout
        self._session = None
        self._status = False
        self._b_read_in_background = False
        self._lock = threading.Lock()
        self._str_buffer = ''
        self.connect()

    def connect(self):
        if not self.is_open():
            try:
                self._session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._session.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                self._session.settimeout(self._timeout)
                if self._session.connect_ex((self._ip, self._port)) == 0:
                    self._status = True
                else:
                    self._status = False
            except Exception:
                self._status = False
                raise RuntimeError("Can not connect to %s:%s", self._ip, self._port)
            if self._status:
                t = threading.Thread(target=self._read_data_in_background,
                                     name='{}:{}'.format(self._ip, self._port)).start()

    def close(self):
        if self.is_open():
            self._session.shutdown(socket.SHUT_RDWR)
            self._session.close()
            self._session = None
            self._status = False

    def send(self, cmd, description=''):
        """
        send cmd in one
        :param cmd:
        :param description:
        :return:
        """
        if self.is_open():
            try:
                self.log(" >>>>>> [ {} --> '{}' ]".format(description, cmd))
                self._session.send(cmd + self._end_str)
            except Exception:
                raise RuntimeError("CMD Send Error, %s:%s", self._ip, self._port)
        else:
            raise RuntimeError("%s:%s did not connected", self._ip, self._port)

    def send_by_byte(self, cmd, interval=0.005, description=''):
        """
        send cmd one by one byte
        :param cmd:
        :param interval:
        :param description:
        :return:
        """
        if self.is_open():
            try:
                for i in cmd:
                    self._session.send(i)
                    time.sleep(interval)
                self._session.send(self._end_str)
                self.log(" >>>>>> [ {} --> '{}' ]".format(description, cmd))
            except Exception:
                raise RuntimeError("CMD Send Error, %s:%s", self._ip, self._port)
        else:
            raise RuntimeError("%s:%s did not connected", self._ip, self._port)

    def read_until(self, terminator, next_line_check=False, next_line_flag=''):
        timeout_happen = False
        line = ""
        # collect start time
        begin = time.time()
        if self.is_open():
            while True:
                c = self._session.recv(1)
                if c:
                    line += c
                    if line.rfind(terminator) > 0:
                        if next_line_check:
                            if line.split('\n')[-1].split() == next_line_flag:
                                break
                        else:
                            break
                    time.sleep(0.001)
                if time.time() - begin > self._timeout:
                    timeout_happen = True
                    break
            if timeout_happen:
                raise RuntimeError("Error: timeout %s", line)
            return line
        else:
            raise RuntimeError("%s:%s did not connected", self._ip, self._port)

    def is_open(self):
        return self._status

    def _read_data_in_background(self):
        while self._b_read_in_background:
            ret, _, _ = select.select([self._session], [], [], 0)
            if ret:
                res = self._session.recv(1024)
                self._analysis_data(res)
            time.sleep(0.001)

    def _analysis_data(self, data):
        if self._lock.acquire(True):
            self._str_buffer += data
        self._lock.release()


if __name__ == '__main__':
    se = SerialPort('/dev/cu.usbserial-FT2HRKE1', 115200)

    # time.sleep(10)
    se.set_detect_string('IN1')
    b, s = se.wait_detect()
    print b, s
    print se.read_string()
    se._b_read_in_background = False
    se.close()
