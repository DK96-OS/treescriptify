#!/usr/bin/python
"""Main Entry Point
"""
from sys import argv

from .argument_parser import parse_args
from . import tsfy


def main():
    input_data = parse_args(argv[1:])
    print(tsfy(input_data))


if __name__ == '__main__':
    main()
