#!/usr/bin/env python3

from optparse import OptionParser
from optparse import OptionGroup
import sys

def main():
    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.set_defaults(verbose=False)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose")
    parser.add_option("-f", "--file", action="store", type="string",
                        dest="filename", help="write report to FILE")
    parser.add_option("-n", "--number", action="store", type="int", dest="number", help="print NUMBER lines")
    parser.add_option("-r", action="store_const", const="root", dest="user", help="only print root lines")
    parser.add_option("-e", dest="env")

    def is_release(option, opt_str, value, parser):
        if parser.values.env == "prd":
            raise parser.error("Can't release in production environment!")
        setattr(parser.values, option.dest, True)

    parser.add_option("--release", action="callback", callback=is_release, dest="release", help="release version")

    group = OptionGroup(parser, "Dangerous Options")
    group.add_option("-g", action="store_true", dest="group", help="Group Option")
    parser.add_option_group(group)

    options, args = parser.parse_args()
    print(f"options: {options}")
    print(f"args: {args}")

if __name__ == '__main__':
    main()
    sys.exit(0)

