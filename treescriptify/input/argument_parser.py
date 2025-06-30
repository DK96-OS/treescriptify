""" Argument Parsing Methods
"""
from argparse import ArgumentParser

from treescriptify.input.argument_data import ArgumentData


def parse_args(arguments: list[str]) -> ArgumentData:
    """ Parse the arguments, and determine the program's Input Data.
    """
    try:
        args = _define_arguments().parse_args(arguments)
    except SystemExit:
        exit("Unable to Parse Arguments.")
    if args.depth < 0:
        exit("Invalid Depth Argument.")
    return ArgumentData(
        include_hidden=args.hide,
        directories_only=args.directories,
        git_ignore=args.gitignore,
        prune_dirs=args.prune,
        depth=args.depth,
    )


def _define_arguments() -> ArgumentParser:
    """ Create and initialize the ArgumentParser.
    """
    parser = ArgumentParser(
        description='Treescriptify creates TreeScript from an existing File Tree.'
    )
    parser.add_argument(
        '-a',
        '--hide',
        action='store_false',
        default=True,
        help='Include hidden Files and Directories in the TreeScript output. Default: True. Setting this flag removes hidden Files and Directories.'
    )
    parser.add_argument(
        '-d',
        '--directories',
        action='store_true',
        default=False,
        help='Only Directories in TreeScript output.'
    )
    parser.add_argument(
        '--gitignore','--no-gitignore',
        action='store_false',
        default=True,
        help='Apply Gitignore patterns to Files and Directories in TreeScript output. Default: True. Setting this flag disables .gitignore.'
    )
    parser.add_argument(
        '--prune', '-p',
        action='store_true',
        default=False,
        help='Only Non-Empty Directories in TreeScript output. Default: False. This may be applied with or without Depth argument.'
    )
    parser.add_argument(
        "--depth",
        type=int,
        default=0,
        help="The depth in the tree to stop recursion at. The number of parent Directories in the path. Directories with larger depth are not traversed, only displayed in the TreeScript output.",
    )
    return parser
