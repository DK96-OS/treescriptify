""" Arguments Received by the CLI argument parser.
 - This dataclass is only used within Input package.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentData:
    """ The optional flags to modify the output of the program.

**Fields:**
 - include_hidden (bool): Whether to include hidden files and directories. Default: True.
 - directories_only (bool): Filter out all files. Default: False.
 - git_ignore (bool): Whether to Load gitignore Patterns. Default: True.
 - prune_dirs (bool): Filter out empty directories. Default: False.
    """
    include_hidden: bool = True
    directories_only: bool = False
    git_ignore: bool = True
    prune_dirs: bool = False
    depth: int = 0
