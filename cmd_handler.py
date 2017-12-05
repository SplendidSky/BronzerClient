class Handler():
    help_msg = "help message"

    def handle(self, cmd):
        rtn_msg = "Handle cmd failed."
        try:
            if cmd == "help":
                rtn_msg = self.help_msg
            else:
                rtn_msg = handle_cmd(cmd)
        except TypeError:
            rtn_msg = "Wrong cmd type."
        except IndexError:
            rtn_msg = "Too few arguments."
        finally:
            return rtn_msg
    
    def handle_cmd(self, cmd):
        pass

