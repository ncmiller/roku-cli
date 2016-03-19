import argparse
from roku import Roku
from discover import discover_roku
from blessed import Terminal


usage_menu = (
        "  +-------------------------------+-------------------------+\n"
        "  | Back           B              | Replay          R       |\n"
        "  | Home           H              | Info/Settings   i       |\n"
        "  | Left           h or <Left>    | Rewind          r       |\n"
        "  | Down           j or <Down>    | Fast-Fwd        f       |\n"
        "  | Up             k or <Up>      | Play/Pause      <Space> |\n"
        "  | Right          l or <Right>   | Enter Text      /       |\n"
        "  | Ok/Enter       <Enter>        |                         |\n"
        "  +-------------------------------+-------------------------+\n"
        "   (press q to exit)\n")


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

    def text_entry(self):
        pass

    def run(self):
        ipaddr = self.parseargs().ipaddr

        # If IP not specified, use Roku discovery and let user choose
        if ipaddr:
            roku = Roku(ipaddr)
        else:
            roku = discover_roku()

        print(usage_menu)

        term = Terminal()

        cmd_func_map = {
            'B':         roku.back,
            'H':         roku.home,
            'h':         roku.left,
            'KEY_LEFT':  roku.left,
            'j':         roku.down,
            'KEY_DOWN':  roku.down,
            'k':         roku.up,
            'KEY_UP':    roku.up,
            'l':         roku.right,
            'KEY_RIGHT': roku.right,
            'KEY_ENTER': roku.select,
            'R':         roku.replay,
            'i':         roku.info,
            'r':         roku.reverse,
            'f':         roku.forward,
            ' ':         roku.play,
            '/':         self.text_entry}

        # Main interactive loop
        with term.cbreak():
            val = ''
            while val.lower() != 'q':
                val = term.inkey()
                if not val:
                    continue
                if val.is_sequence:
                    val = val.name
                if val in cmd_func_map:
                    cmd_func_map[val]()


def main():
    RokuCLI().run()
