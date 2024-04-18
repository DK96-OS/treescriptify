"""Generate TreeScript from Tree Node Data.
"""
from typing import Generator

from .tree_node_data import TreeNodeData


def generate_script(tree_nodes: Generator[TreeNodeData, None, None]) -> Generator[str, None, None]:
    """Generate the TreeScript Line by Line for each Tree Node.
    """
    for node in tree_nodes:
        yield _write_line(node)


def _write_line(data: TreeNodeData) -> str:
    """Convert a Tree Node into a line of TreeScript.
    """
    line = data.depth * '  ' + data.name
    if data.is_dir:
        line += '/'
    return line
