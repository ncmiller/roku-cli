import argparse
from roku import Roku
from discover import discover_roku

class RokuCLI():
    """ Command-line interpreter for processing user input and relaying
    commands to Roku """
    def __init__(self):
        pass

    def parseargs(self):
        parser = argparse.ArgumentParser(
                description='Command-line control of Roku devices')
        parser.add_argument(
                'ipaddr',
                nargs='?',
                help=('IP address of Roku to connect to. By default, will ' +
                    'automatically detect Roku within LAN.'))
        return parser.parse_args()

    def run(self):
        ipaddr = self.parseargs().ipaddr

        # If IP not specified, use Roku discovery and let user choose
        if ipaddr:
            roku = Roku(ipaddr)
        else:
            roku = discover_roku()

        # Main interactive loop
        print('Running')
        while True:
            roku.home()
            break


def main():
    RokuCLI().run()
