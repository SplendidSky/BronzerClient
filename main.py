from connect import Connect

if __name__ == '__main__':
    connect = Connect()
    connect.startConnect()
    welcome_msg = connect.retriveMsg()
    print(welcome_msg)
    data = connect.sendCmd("test")
    print(data)