"""Input Data to the Program
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class InputData:
    """The optional flags to modify the output of the program.
    """

    include_hidden: bool = True
    #
    directories_only: bool = False
    #
    git_ignore: bool = True
    #
    prune_dirs: bool = False
