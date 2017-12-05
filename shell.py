import argparse
from connect import Connect
# from cmd_handler import Handler

class Shell():

    def run(self):
        print("Welcome to Bronzer!")
        connect = Connect()
        connect.startConnect()
        welcome_msg = connect.retriveMsg()
        print(welcome_msg)

        while(True):
            cmd = input("Bronzer>>")
            if not cmd.strip():
                continue
            if cmd.strip() == "exit":
                connect.sendCmd(cmd)
                break

            msg = connect.sendCmd(cmd)
            print(msg)
            # handler = Handler()
            # rtn_msg = handler.handle(cmd)
            # print(rtn_msg)

        connect.stopConnect()
        exit(0)