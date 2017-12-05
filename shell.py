import argparse
from cmd_handler import Handler

class Shell():

    def run(self):
        print("Welcome to Bronzer!")
        while(True):
            cmd = input("Bronzer>>")
            if not cmd.strip():
                continue
            if cmd.strip() == "exit":
                break

            handler = Handler()
            rtn_msg = handler.handle(cmd)
            print(rtn_msg)
