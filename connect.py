import os
import socket
from singleton import Singleton

class Connect(metaclass=Singleton):
    CMD_START_SERVICE = 'adb shell am broadcast -a CONNECT_SERVICE_START'
    CMD_STOP_SERVICE = 'adb shell am broadcast -a CONNECT_SERVICE_STOP'
    CMD_PORT_FORWARD = 'adb forward tcp:15831 tcp:15831'

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        

    def startConnect(self):
        os.system(CMD_START_SERVICE)
        os.system(CMD_PORT_FORWARD)
        self.socket.connect(('127.0.0.1', 15831))

    def stopConnect(self):
        os.system(CMD_STOP_SERVICE)
        self.socket.close()

    def sendCmd(self, cmd):
        self.socket.send(cmd)
        buffer = []
        while True:
            d = self.socket.recv(1024)
            if data:
                buffer.append(d)
            else:
                break
        data = ''.join(buffer)
        return data