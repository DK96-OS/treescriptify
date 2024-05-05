"""Python implementation of the Tree Command, for windows OS.
"""
from pathlib import Path
from sys import exit
from typing import Generator

from .input_data import InputData
from .tree_node_data import TreeNodeData


def win_tree(data: InputData) -> Generator[TreeNodeData, None, None]:
    """Generate Tree Node Data for all files and directories in the given path.

    Parameters:
    - path (str): The root path to run tree in.

    Return:
    Generator[TreeNodeData]
    """
    try:
        tree_root = Path('./')
    except:
        exit('Failed to initiate Path')
    return _gen_tree(data, tree_root)


def _gen_tree(
    data: InputData,
    path: Path,
    depth: int = 0
) -> Generator[TreeNodeData, None, None]:
    """Mimic the Tree command.
    """
    for entry in path.iterdir():
        # Check Hidden Files option
        if not data.include_hidden and entry.name.startswith('.'):
            continue
        is_directory = entry.is_dir()
        if data.directories_only:
            if is_directory:
                # Check if prune_dirs is True and directory is empty 
                if not data.prune_dirs or any(_gen_tree(data, entry, depth + 1)):
                    yield TreeNodeData(depth, is_directory, entry.name)
        else:
            yield TreeNodeData(depth, is_directory, entry.name)
            if is_directory:
                yield from _gen_tree(data, entry, depth + 1)

