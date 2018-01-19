import os
import socket
from singleton import Singleton

class Connect(metaclass=Singleton):
    """CONNECT TO ANDROID!
    
    Use this class to connect to your android.

    """
    
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
