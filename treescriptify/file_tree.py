""" Python implementation of Tree.
"""
from pathlib import Path
from re import Pattern
from typing import Generator

from treescriptify.data.input_data import InputData
from treescriptify.data.tree_node_data import TreeNodeData


def generate_tree(
    data: InputData,
    path: Path = Path('./'),
) -> Generator[TreeNodeData, None, None]:
    """ Generate Tree Node Data for all files and directories in the given path.

**Parameters:
 - data (InputData): The program options and inputs.
 - path (str): The root path of the TreeScript.

**Yields:**
 TreeNodeData - Dataclass objects representing Nodes in the FileTree.
    """
    if data.directories_only:
        if data.prune_dirs:
            yield from _nonempty_dir_only_tree(data, path)
        else:
            yield from _dir_only_tree(data, path)
    elif data.prune_dirs:
        yield from _prune_only_tree(data, path)
    else:
        yield from _basic_tree(data, path)


def _basic_tree(
    data: InputData,
    path: Path,
    depth: int = 0,
) -> Generator[TreeNodeData, None, None]:
    """ Simply Files and Directories.
    """
    if 0 < data.depth <= depth - 1:
        return
    for entry in sorted(path.glob('*')):
        #if data.ignore_patterns is not None and _should_ignore_node(data.ignore_patterns, entry):
        #    continue
        if data.ignore_hidden and entry.name.startswith('.'):
            continue
        is_directory = entry.is_dir(follow_symlinks=False)
        yield TreeNodeData(depth, is_directory, entry.name)
        if is_directory:
            yield from _basic_tree(data, entry, depth=depth + 1)


def _dir_only_tree(
    data: InputData,
    path: Path,
    depth: int = 0,
    debug: bool = False,
) -> Generator[TreeNodeData, None, None]:
    """ Only Yields Directories.
    """
    if 0 < data.depth < depth:
        return
    for entry in sorted(path.glob('*')):
        if is_directory := entry.is_dir(follow_symlinks=False):
            #if data.ignore_patterns is not None and _should_ignore_node(data.ignore_patterns, entry):
            #    continue
            if data.ignore_hidden and entry.name.startswith('.'):
                continue
            yield TreeNodeData(depth, is_directory, entry.name)
            yield from _dir_only_tree(data, entry, depth=depth + 1)
        elif debug:
            print(f"Ignoring File {entry.name}")


def _nonempty_dir_only_tree(
    data: InputData,
    path: Path,
    depth: int = 0,
    debug: bool = False,
) -> Generator[TreeNodeData, None, None]:
    """ Only Yields Non-Empty Directories.
    """
    if 0 < data.depth < depth:
        return
    for entry in sorted(path.glob('*')):
        if is_directory := entry.is_dir(follow_symlinks=False):
            #if data.ignore_patterns is not None and _should_ignore_node(data.ignore_patterns, entry):
            #    continue
            if data.ignore_hidden and entry.name.startswith('.'):
                continue
            if any(entry.glob('*')): # Only if directory is non-empty
                yield TreeNodeData(depth, is_directory, entry.name)
                yield from _nonempty_dir_only_tree(data, entry, depth=depth + 1)
        elif debug:
            print(f"Ignoring File {entry.name}")


def _prune_only_tree(
    data: InputData,
    path: Path,
    depth: int = 0,
) -> Generator[TreeNodeData, None, None]:
    """ Yields Files and Non-Empty Directories.
    """
    if 0 < data.depth < depth:
        return
    for entry in sorted(path.glob('*')):
        #if data.ignore_patterns is not None and _should_ignore_node(data.ignore_patterns, entry):
        #    continue
        if data.ignore_hidden and entry.name.startswith('.'):
            continue
        if entry.is_dir(follow_symlinks=False):
            if any(entry.glob('*')): # The directory must be non-empty, or ignore it
                yield TreeNodeData(depth, is_dir=True, name=entry.name)
                yield from _prune_only_tree(data, entry, depth=depth + 1)
        else:
            yield TreeNodeData(depth, is_dir=False, name=entry.name)


def _should_ignore_node(
    ignore_patterns: list[Pattern],
    tree_node_path: Path,
) -> bool:
    for ip in ignore_patterns:
        if ip.match(str(tree_node_path)):
            return True
    return False