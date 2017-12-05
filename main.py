from connect import Connect
from shell import Shell


if __name__ == '__main__':
    # connect = Connect()
    # connect.startConnect()
    # welcome_msg = connect.retriveMsg()
    # print(welcome_msg)
    # data = connect.sendCmd("test")
    # print(data)

    shell = Shell()
    shell.run()