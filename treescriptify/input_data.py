""" Input Data to the Program
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class InputData:
    """ The optional flags to modify the output of the program.

**Fields:**
 - include_hidden (bool): Whether to include hidden files and directories. Default: True.
 - directories_only (bool): Filter out all files. Default: False.
 - git_ignore (bool): Try to use gitignore. Note, unix-tree required. No windows support yet. Default: True.
 - prune_dirs (bool): Filter out empty directories. Default: False.
    """
    include_hidden: bool = True
    directories_only: bool = False
    git_ignore: bool = True
    prune_dirs: bool = False