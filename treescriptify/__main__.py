#!/usr/bin/python


def main():
    import os
    from sys import argv
    from .argument_parser import parse_args
    from . import tsfy, tsfy_windows
    input_data = parse_args(argv[1:])
    output_data = tsfy_windows(input_data) if os.name == 'nt' else tsfy(input_data)
    print(output_data)


if __name__ == '__main__':
    main()