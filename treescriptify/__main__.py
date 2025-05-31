#!/usr/bin/python


def main():
    from sys import argv
    from .argument_parser import parse_args
    from . import tsfy
    input_data = parse_args(argv[1:])
    output_data = tsfy(input_data)
    print(output_data)


if __name__ == '__main__':
    main()