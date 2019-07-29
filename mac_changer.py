import subprocess
import optparse

def mac_change(interface, mac_adr):
    print("[+] Changing mac address for " + interface + " to " + mac_adr)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_adr])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--i", "--interface", dest="interface", help="Interface to change mac address")
    parser.add_option("--m", "--mac", dest="mac_adr", help="New mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.mac_adr:
        parser.error("[-] Please specify an  New Mac address, use --help for more info.")
    return options


options1 = get_arguments()

mac_change(options1.interface, options1.mac_adr)


