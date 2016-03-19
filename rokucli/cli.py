import sys
import argparse
from roku import Roku
from discover import discover_roku
from blessed import Terminal


usage_menu = (
        "  +-------------------------------+-------------------------+\n"
        "  | Back           B or <Backsp>  | Replay          R       |\n"
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
        self.term = Terminal()
        self.roku = None

    def parseargs(self):
        parser = argparse.ArgumentParser(
                description='Interactive command-line control of Roku devices')
        parser.add_argument(
                'ipaddr',
                nargs='?',
                help=('IP address of Roku to connect to. By default, will ' +
                      'automatically detect Roku within LAN.'))
        return parser.parse_args()

    def text_entry(self):
        """ Relay literal text entry from user to Roku until
        <Enter> or <Esc> pressed. """

        allowed_sequences = set(['KEY_ENTER', 'KEY_ESCAPE', 'KEY_DELETE'])

        sys.stdout.write('Enter text (<Esc> to abort) : ')
        sys.stdout.flush()

        # Track start column to ensure user doesn't backspace too far
        start_column = self.term.get_location()[1]
        cur_column = start_column

        with self.term.cbreak():
            val = ''
            while val != 'KEY_ENTER' and val != 'KEY_ESCAPE':
                val = self.term.inkey()
                if not val:
                    continue
                elif val.is_sequence:
                    val = val.name
                    if val not in allowed_sequences:
                        continue

                if val == 'KEY_ENTER':
                    self.roku.enter()
                elif val == 'KEY_ESCAPE':
                    pass
                elif val == 'KEY_DELETE':
                    self.roku.backspace()
                    if cur_column > start_column:
                        sys.stdout.write(u'\b \b')
                        cur_column -= 1
                else:
                    self.roku.literal(val)
                    sys.stdout.write(val)
                    cur_column += 1
                sys.stdout.flush()

            # Clear to beginning of line
            sys.stdout.write(self.term.clear_bol)
            sys.stdout.write(self.term.move(self.term.height, 0))
            sys.stdout.flush()

    def run(self):
        ipaddr = self.parseargs().ipaddr

        # If IP not specified, use Roku discovery and let user choose
        if ipaddr:
            self.roku = Roku(ipaddr)
        else:
            self.roku = discover_roku()

        if not self.roku:
            return

        print(usage_menu)

        cmd_func_map = {
            'B':          self.roku.back,
            'KEY_DELETE': self.roku.back,
            'H':          self.roku.home,
            'h':          self.roku.left,
            'KEY_LEFT':   self.roku.left,
            'j':          self.roku.down,
            'KEY_DOWN':   self.roku.down,
            'k':          self.roku.up,
            'KEY_UP':     self.roku.up,
            'l':          self.roku.right,
            'KEY_RIGHT':  self.roku.right,
            'KEY_ENTER':  self.roku.select,
            'R':          self.roku.replay,
            'i':          self.roku.info,
            'r':          self.roku.reverse,
            'f':          self.roku.forward,
            ' ':          self.roku.play,
            '/':          self.text_entry}

        # Main interactive loop
        with self.term.cbreak():
            val = ''
            while val.lower() != 'q':
                val = self.term.inkey()
                if not val:
                    continue
                if val.is_sequence:
                    val = val.name
                if val in cmd_func_map:
                    try:
                        cmd_func_map[val]()
                    except:
                        print('Unable to communicate with roku at ' +
                              str(self.roku.host) + ':' + str(self.roku.port))
                        sys.exit(1)


def main():
    RokuCLI().run()

if __name__ == '__main__':
    main()
