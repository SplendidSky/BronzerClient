import optparse
from singleton import Singleton

class OptsParser(metaclass=Singleton):

    def __init__(self):
        print("OptsParser")
        self.parser = optparse.OptionParser(prog="Bronzer")
        
        self.parser.add_option("-D", "--debug", action="store_true", dest="debug", help="Enable debugging")
        self.parser.add_option("-a", "--action", dest="action", help="Action")
        self.parser.add_option("-d", "--data-uri",dest="data_uri", help="Data uri")
        self.parser.add_option("-c", "--category", dest="category", help="Category")
        self.parser.add_option("-e", "--extra", nargs=2, dest="extra", help="Extra value")
        self.parser.add_option("--eb", "--extra-bool", dest="extra_bool", help="Extra bool value")
        self.parser.add_option("--ei", "--extra-int", dest="extra_int", help="Extra int value")
        self.parser.add_option("--el", "--extra-long", dest="extra_long", help="Extra long value")
        self.parser.add_option("--ef", "--extra-float", dest="extra_float", help="Extra float value")
        self.parser.add_option("--eu", "--extra-uri", dest="extra_uri", help="Extra uri value")
        self.parser.add_option("--es", "--extra-string", dest="extra_string", help="Extra string value")
        

        # self.parser.add_option("start", help="Start an activity")
        # self.parser.add_option('strarservice', dest="service", help="Start a service")

    """Parse options

    Args:
        cmd: A command.

    Returns:
        A tuple ([dict]options, [list]args).

    """
    def parse(self, cmd):
        # print("parse " + cmd)
        return self.parser.parse_args(cmd)