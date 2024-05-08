"""Python implementation of the Tree Command, for windows OS.
"""
from pathlib import Path
from typing import Generator

from .input_data import InputData
from .tree_node_data import TreeNodeData


def win_tree(
    data: InputData,
    path: Path = Path('./'),
) -> Generator[TreeNodeData, None, None]:
    """Generate Tree Node Data for all files and directories in the given path.

    Parameters:
    - data (InputData): The
    - path (str): The root path to run tree in.

    Return:
    Generator[TreeNodeData]
    """
    if data.directories_only:
        if data.prune_dirs:
            yield from _dirs_only_prune(data, path)
        else:
            yield from _dirs_only(data, path)
    else:
        yield from _gen_tree(data, path)


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
        yield TreeNodeData(depth, is_directory, entry.name)
        if is_directory:
            yield from _gen_tree(data, entry, depth + 1)


def _dirs_only(
    data: InputData,
    path: Path,
    depth: int = 0
) -> Generator[TreeNodeData, None, None]:
    """Only Yields Directories.
    """
    for entry in path.iterdir():
        if not data.include_hidden and entry.name.startswith('.'):
            continue
        if (is_directory := entry.is_dir()):
            yield TreeNodeData(depth, is_directory, entry.name)
            yield from _dirs_only(data, entry, depth + 1)
        else:
            #print(f"Ignoring File {entry.name}")
            pass


def _dirs_only_prune(
    data: InputData,
    path: Path,
    depth: int = 0
) -> Generator[TreeNodeData, None, None]:
    """Only Yields Directories, after pruning.
    """
    for entry in path.iterdir():
        if not data.include_hidden and entry.name.startswith('.'):
            continue
        if (is_directory := entry.is_dir()):
            # Check if directory is empty
            if any(entry.iterdir()):
                yield TreeNodeData(depth, is_directory, entry.name)
                yield from _dirs_only_prune(data, entry, depth + 1)
        else:
            #print(f"Ignoring File {entry.name}")
            pass

