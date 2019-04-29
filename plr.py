from lib import *
import argparse

def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-if', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin, action='store', dest='input')
    parser.add_argument('-of', nargs='?', type=argparse.FileType('w'),
                         default=sys.stdout, action='store', dest='output')
    parser.add_argument('-permacc', action='store_true')
    return parser.parse_args()

def main():
    args = parseargs()
    if args.permacc:
        linkfunc = getPermaccLink
    else:
        linkfunc = getWebArchiveLink
    if args.output.name != '<stdout>':
        writeoutput = output.write
    else:
        writeoutput = print
    for line in args.input:
        if isurl(line):
            writeoutput(linkfunc(line)[1])
        else:
            print("Not a url, skipping")

