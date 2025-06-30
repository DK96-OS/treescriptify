"""Tree Node Data
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeNodeData:
    """ The Dataclass container for an individual node in the FileTree.

**Fields:**
 - depth (int): The depth of the node in the tree.
 - is_dir (bool): Whether the node is a directory or a file.
 - name (str): The name of the node in the FileTree.
    """
    depth: int
    is_dir: bool
    name: str
