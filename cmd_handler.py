import args_parser
import os
from connect import Connect

class Handler():
    help_msg = "help message"
    package_name = ""

    def handle(self, cmd):
        rtn_msg = "Handle cmd failed."
        if cmd == "help":
            rtn_msg = self.help_msg
        elif cmd == "list":
            connect = Connect()
            rtn_msg = connect.sendCmd("list")
        else:
            rtn_msg = self.handle_local_cmd(cmd)

        return rtn_msg

    
    def handle_local_cmd(self, cmd):
        # print("handle_cmd")
        cmds = str.split(cmd)
        action = cmds[0]
        print("action: "+action)
        parser = args_parser.ArgsParser()

        if action == "set":
            self.package_name = cmds[1]

        if action == "start" or action == "startservice" or action == "stopservice" or action == "broadcast":
            command = ""
            if action != "broadcast":
                component_name = cmds[1]
                command += "adb shell am " + action + self.package_name + "/" + self.package_name + "." + component_name
            else:
                command += "adb shell am broadcast"

            parse_result = parser.parse(cmds[2:])
            if parse_result.debug == True:
                command += " -D"
            if parse_result.action is not None:
                command += " -a " + parse_result.action
            if parse_result.data_uri is not None:
                command += " -d " + parse_result.data_uri
            if parse_result.category is not None:
                command += " -c " + parse_result.category
            if parse_result.extra_int is not None:
                command += " --ei " + parse_result.extra_int
            if parse_result.extra_bool is not None:
                command += " --ez " + parse_result.extra_bool
            if parse_result.extra_long is not None:
                command += " --el " + parse_result.extra_long
            if parse_result.extra_float is not None:
                command += " --ef " + parse_result.extra_float
            if parse_result.extra_uri is not None:
                command += " --eu " + parse_result.extra_uri
            if parse_result.extra_string is not None:
                command += " --es " + parse_result.extra_string

            print(command)
            # os.system(command)
            
        

        # print(results)