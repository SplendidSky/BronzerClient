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
        assess:           assess security
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
        -D --debug:                   enable debug switch
        -a --action ACTION:           add an action
        -d --data-uri URI:            set a data-uri
        -c --category CATEGORY:       add a category
        -e --extra TYPE VALUE:        add an extra value
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
    remote_action = ["assess", "list", "attacksurface"]
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
        elif action == "assess":
            
            _packages = connect.sendCmd("list")
            packages = str.split(_packages)

            for package in packages:
                print(package)
                _exported_activities = connect.sendCmd("_exported_activities " + package)
                _exported_services = connect.sendCmd("_exported_services " + package)
                exported_activities = str.split(_exported_activities)
                exported_services = str.split(_exported_services)
                # exported_activities[0] is a placeholder
                for exported_activity in exported_activities[1:]:
                    command =  "adb shell am start -n " + package + "/" + exported_activity
                    print(command)
                    output = os.popen(command)
                    output = output.readlines()
                    print(output)
                    if len(output) > 2:
                        continue
                    print(package,"/", exported_activity, "can be called in outer environment.\n")
                    # break
                    # print("OS: ", os.system(command))

                # exported_services[0] is a placeholder
                for exported_service in exported_services[1:]:
                    command = "adb shell am startservice -n " + package + "/" + exported_service
                    output = os.popen(command)
                    output = output.readlines()
                    print(output)
                    if len(output) > 2:
                        continue
                    print(package,"/", exported_service, "can be manipulated in outer environment.\n")
                    # break
                    # print("OS: ", os.system(command))


        
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
                command += "adb shell am " + action + " -n " + self.package_name + "/" + component_name
            else:
                command += "adb shell am broadcast"

            (options,args) = parser.parse(tokens[2:])
            print(options)
            if options.debug is not None:
                command += " -D"
            if options.action is not None:
                command += " -a " + options.action
            if options.data_uri is not None:
                command += " -d " + options.data_uri
            if options.category is not None:
                command += " -c " + options.category
            if options.extra_int is not None:
                command += " --ei " + options.extra_int
            if options.extra_bool is not None:
                command += " --ez " + options.extra_bool
            if options.extra_long is not None:
                command += " --el " + options.extra_long
            if options.extra_float is not None:
                command += " --ef " + options.extra_float
            if options.extra_uri is not None:
                command += " --eu " + options.extra_uri
            if options.extra_string is not None:
                command += " --es " + options.extra_string

            print(command)
            os.system(command)

        else:
            print(self.help_msg)

            