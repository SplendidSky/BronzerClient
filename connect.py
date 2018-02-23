import os
import socket
from singleton import Singleton

class Connect(metaclass=Singleton):
    """CONNECT TO ANDROID!
    
    Use this class to connect to your android.

    """
    
    def __init__(self):
        self.port = 15831
        self.CMD_EXTRA_OPTS = ''

        self.CMD_START_SERVICE = 'adb {extra} shell am broadcast -a CONNECT_SERVICE_START '.format(extra=self.CMD_EXTRA_OPTS)
        self.CMD_STOP_SERVICE = 'adb {extra} shell am broadcast -a CONNECT_SERVICE_STOP'.format(extra=self.CMD_EXTRA_OPTS)
        self.CMD_PORT_FORWARD = 'adb {extra} forward tcp:{port} tcp:{port}'
        self.CMD_LIST_DEVICES = 'adb devices'

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        

    def updateCmd(self):
        self.CMD_START_SERVICE = 'adb {extra} shell am broadcast -a CONNECT_SERVICE_START '.format(extra=self.CMD_EXTRA_OPTS)
        self.CMD_STOP_SERVICE = 'adb {extra} shell am broadcast -a CONNECT_SERVICE_STOP'.format(extra=self.CMD_EXTRA_OPTS)
        self.CMD_PORT_FORWARD = 'adb {extra} forward tcp:{port} tcp:{port}'

    def startConnect(self):
        while os.system(self.CMD_START_SERVICE) != 0:
            os.system(self.CMD_LIST_DEVICES)
            print('''Use d/e/s to specify a device:
d                            - directs command to the only connected USB device
e                            - directs command to the only running emulator
s <specific device>          - directs command to the device or emulator with the given
''')
            opts=input("Bronzer-SpecifyDevice>> ")
            self.CMD_EXTRA_OPTS = '-' + opts
            self.updateCmd()
            print(self.CMD_START_SERVICE)


        while os.system(self.CMD_PORT_FORWARD.format(port=self.port)) != 0:
            print("Current port {} is occupied, choose another port".format())
            self.port=input("Bronzer-ChoosePort>> ")
            self.updateCmd()
        
        self.socket.connect(('127.0.0.1', self.port))

    def stopConnect(self):
        os.system(self.CMD_STOP_SERVICE)
        self.socket.close()

    """Retrive message from android
    When you want to know whether android has sent something to you, use this.

    Returns:
        A string comes from android.
        If android doesn't send anything to you, return None.
    """
    def retriveMsg(self):
        data = self.socket.recv(40960)
        return bytes.decode(data)


    """Send command to android and retrive the response
    
    Args:
        cmd: Just a command.

    Returns:
        A string that android answers to the command.
    """
    def sendCmd(self, cmd):
        self.socket.sendall(str.encode(cmd))
        return self.retriveMsg()
