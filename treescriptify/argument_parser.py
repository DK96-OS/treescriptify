"""Argument Parsing Methods
"""
from argparse import ArgumentParser

from treescriptify.input_data import InputData


def parse_args(arguments: list[str]) -> InputData:
    """Parse the arguments, and determine the program's Input Data.
    """
    try:
        args = _define_arguments().parse_args(arguments)
    except SystemExit as e:
        exit("Unable to Parse Arguments.")
    return InputData(
        include_hidden=args.hide,
        directories_only=args.directories,
        git_ignore=args.gitignore,
        prune_dirs=args.prune
    )


def _define_arguments() -> ArgumentParser:
    """Create and initialize the ArgumentParser.
    """
    parser = ArgumentParser(
        description='Treescriptify'
    )
    parser.add_argument(
        '-a',
        '--hide',
        action='store_false',
        default=True,
        help='Hidden files are shown by default. This flag hides them.'
    )
    parser.add_argument(
        '-d',
        '--directories',
        action='store_true',
        default=False,
        help='Flag to show only the directories.'
    )
    parser.add_argument(
        '--gitignore',
        action='store_false',
        default=True,
        help='Gitignore is enabled by default. This flag disables .gitignore.'
    )
    parser.add_argument(
        '--prune',
        action='store_true',
        default=False,
        help='Flag to prune empty directories from the output.'
    )
    return parser
