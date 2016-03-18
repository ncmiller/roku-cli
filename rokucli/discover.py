from roku import Roku


def discover_roku():
    """ Search LAN for available Roku devices. Returns a Roku object. """

    print("Searching for Roku devices within LAN ...")
    rokus = Roku.discover()
    if not rokus:
        print("Unable to discover Roku devices. " +
              "Try again, or manually specify the IP address with " +
              "\'roku <ipaddr>\' (e.g. roku 192.168.1.130)")
        return None

    print("Found the following Roku devices:")
    for i, r in enumerate(rokus):
        print("[" + str(i+1) + "]   " + str(r.host) + ":" + str(r.port))
    print("")

    if len(rokus) == 1:
        print("Selecting Roku 1 by default")
        return rokus[0]
    else:
        print("Multiple Rokus found. Select the index of the Roku to control:")

        while True:
            try:
                query = "Select (1 to " + str(len(rokus)) + ") > "
                sel = int(raw_input(query)) - 1
                if sel >= len(rokus):
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid selection")

        return rokus[sel]
