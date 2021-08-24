from smart_home_light import lamp_operations
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-d", "--disable", dest="turn_off", action="store_true", help="this command turn off light")
    parser.add_option("-e", "--enable", dest="turn_on", action="store_true", help="this command turn on light")

    options, args = parser.parse_args()

    if options.turn_off:
        lamp_operations("off")
    if options.turn_on:
        lamp_operations("on ")







