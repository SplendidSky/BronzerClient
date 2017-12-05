import os
import socket
from singleton import Singleton

class Connect(metaclass=Singleton):
    
    def __init__(self):
        self.CMD_START_SERVICE = 'adb shell am broadcast -a CONNECT_SERVICE_START'
        self.CMD_STOP_SERVICE = 'adb shell am broadcast -a CONNECT_SERVICE_STOP'
        self.CMD_PORT_FORWARD = 'adb forward tcp:15831 tcp:15831'

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        

    def startConnect(self):
        os.system(self.CMD_START_SERVICE)
        os.system(self.CMD_PORT_FORWARD)
        self.socket.connect(('127.0.0.1', 15831))

    def stopConnect(self):
        os.system(self.CMD_STOP_SERVICE)
        self.socket.close()

    def retriveMsg(self):
        data = self.socket.recv(40960)
        return bytes.decode(data)

    def sendCmd(self, cmd):
        self.socket.sendall(str.encode(cmd))
        return self.retriveMsg()
