import argparse
from singleton import Singleton

class ArgsParser(metaclass=Singleton):
    def __init__(self):
        print("ArgsParser")
        self.parser = argparse.ArgumentParser(prog="PROG")
        
        self.parser.add_argument("-D", "--debug", action="store_true", dest="debug", help="Enable debugging")
        self.parser.add_argument("-a", "--action", dest="action", help="Action")
        self.parser.add_argument("-d", "--data-uri",dest="data_uri", help="Data uri")
        self.parser.add_argument("-c", "--category", dest="category", help="Category")
        self.parser.add_argument("-e", "--extra", nargs=2, dest="extra", help="Extra value")
        self.parser.add_argument("-eb", "--extra-bool", dest="extra_bool", help="Extra bool value")
        self.parser.add_argument("-ei", "--extra-int", dest="extra_int", help="Extra int value")
        self.parser.add_argument("-el", "--extra-long", dest="extra_long", help="Extra long value")
        self.parser.add_argument("-ef", "--extra-float", dest="extra_float", help="Extra float value")
        self.parser.add_argument("-eu", "--extra-uri", dest="extra_uri", help="Extra uri value")
        self.parser.add_argument("-es", "--extra-string", dest="extra_string", help="Extra string value")
        

        # self.parser.add_argument("start", help="Start an activity")
        # self.parser.add_argument('strarservice', dest="service", help="Start a service")

    def parse(self, args):
        # print("parse " + args)
        return self.parser.parse_args(args)