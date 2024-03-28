"""
"""
from argparse import ArgumentParser

from input.input_data import InputData


def parse_args(arguments: list[str]) -> InputData:
    """
    """
    parser = _define_arguments()
    parser.parse_args(arguments)
    # todo:
    return InputData(
        include_hidden=True,
        directories_only=False,
        git_ignore=False,
        prune_dirs=False
    )


def _define_arguments() -> ArgumentParser:
    """
    """
    parser = ArgumentParser()
    # todo: parser.add_argument()
    return parser
