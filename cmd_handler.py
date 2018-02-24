import opts_parser
import os
from connect import Connect

"""Command handler

A handler handles most of commands.

"""
class Handler():
    help_msg = '''
    Usage: ACTION [OPTIONS] [COMPONENT]
    ACTION:
        list:             list all packages
        set:              set packagename

        THE FOLLOWING ACTION NEED SET UP packagename FIRST
        attacksurface:    get an app's attack surface
        start:            start an activity
        startservice:     start a service
        stopservice:      stop a service
        broadcast:        send a broadcast
        exit:             exit Bronzer
        

    OPTIONS:
        -D --debug:                  enable debug switch
        -a --action ACTION:          add an action
        -d --data-uri URI:           set a data-uri
        -c --category CATEGORY:      add a category
        -e --extra TYPE VALUE:       add an extra value
        --eb --extra-bool VALUE:      add an extra boolean value
        --ei --extra-int VALUE:       add an extra int value
        --el --extra-long VALUE:      add an extra long value
        --ef --extra-float VALUE:     add an extra float value
        --eu --extra-uri VALUE:       add an extra uri value
        --es --extra-string VALUE:    add an extra string value

    COMPONENT:
        an android component name

    '''



    local_action = ["set", "start", "startservice", "stopservice", "broadcast"]
    remote_action = ["list", "attacksurface"]
    package_name = ""


    """Handle a command
    
    Args:
        cmd: A command.

    Returns:
        A message after command executing

    """
    def handle(self, cmd):
        rtn_msg = "Handle cmd failed."
        tokens = str.split(cmd)
        action = tokens[0]

        if action in self.remote_action:
            rtn_msg = self.handle_remote_cmd(cmd)
        elif action in self.local_action:
            rtn_msg = self.handle_local_cmd(cmd)
        else:
            rtn_msg = self.help_msg

        return rtn_msg

    def handle_remote_cmd(self, cmd):
        tokens = str.split(cmd)
        action = tokens[0]
        rtn_msg = "Handle remote cmd failed."
        print("remote action " + action)

        connect = Connect()
    
        if action == "list":
            rtn_msg = connect.sendCmd(action)
        elif action == "attacksurface":
            if self.package_name.strip():
                rtn_msg = connect.sendCmd(action + " " + self.package_name)
            else:
                rtn_msg = "Please use set action to set a package"
        
        return rtn_msg


    def handle_local_cmd(self, cmd):
        # print("handle_cmd")
        tokens = str.split(cmd)
        action = tokens[0]
        print("local action: " + action)
        parser = opts_parser.OptsParser()


        if action == "set":
            self.package_name = tokens[1]

        elif action == "start" or action == "startservice" or action == "stopservice" or action == "broadcast":
            command = ""
            if action != "broadcast":
                component_name = tokens[1]
                command += "adb shell am " + action + self.package_name + "/" + self.package_name + "." + component_name
            else:
                command += "adb shell am broadcast"

            parse_result = parser.parse(tokens[2:])
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

        else:
            print(self.help_msg)

            