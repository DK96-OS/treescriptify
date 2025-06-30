#!/usr/bin/python
from pathlib import Path


def main():
    # Author: DK96-OS 2024 - 2025
    from sys import argv
    from treescriptify import generate_treescript, input
    #
    input_data = input.validate_arguments(argv[1:])
    for x in generate_treescript(input_data):
        print(x, end='\n')


if __name__ == '__main__':
    from sys import path
    # Get the directory of the current file (__file__ is the path to the script being executed)
    # Add the directory to sys.path
    path.append(str(Path(__file__).resolve().parent.parent))
    main()
