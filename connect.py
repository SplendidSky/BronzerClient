import os
import socket

class Connect:
    CMD_START_SERVICE = 'adb shell am broadcast -a CONNECT_SERVICE_START'
    CMD_STOP_SERVICE = 'adb shell am broadcast -a CONNECT_SERVICE_STOP'
    CMD_PORT_FORWARD = 'adb forward tcp:15831 tcp:15831'

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        

    def startConnect(self):
        os.system(CMD_START_SERVICE)
        os.system(CMD_PORT_FORWARD)
        self.s.connect(('127.0.0.1', 15831))

    def stopConnect(self):
        os.system(CMD_STOP_SERVICE)
        self.s.close()