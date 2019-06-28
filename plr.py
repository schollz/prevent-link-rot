from lib import *
import argparse

def parseargs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', action='store_true', help="list output wanted", dest='listy')
    parser.add_argument('-if', nargs='?', type=argparse.FileType('r'),
                        default=sys.stdin, action='store', dest='input')
    parser.add_argument('-of', nargs='?', type=argparse.FileType('w'),
                         default=sys.stdout, action='store', dest='output')
    return parser.parse_args()

def main():
    args = parseargs()
    linkfunc = getWebArchiveLink
    if args.output.name != '<stdout>':
        writeoutput = args.output.write
    else:
        writeoutput = print
    print(args.output.name)
    if args.input.name != '<stdin>':
        content = args.input.read()
        content = replaceText(content, archiveList=args.listy)
    if type(content) == list:
        for i in content:
            writeoutput(i + '\n')
    else:
        writeoutput(content)
if __name__ == '__main__':
    main()
