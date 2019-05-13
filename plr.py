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
        writeoutput = args.output.write
    else:
        writeoutput = print

    content = args.input.read()
    content = replaceText(content,False)
    writeoutput(content)
        
if __name__ == '__main__':
    main()
