""" Generate TreeScript from Tree Node Data.
"""
from typing import Generator, Iterable

from treescriptify.data.tree_node_data import TreeNodeData


def generate_script(
    tree_nodes: Iterable[TreeNodeData],
    number_labels: bool = False,
) -> Generator[str, None, None]:
    """ Generate the TreeScript Line by Line for each Tree Node.
 - The Line-Number-Labels feature adds DataLabels to every file Tree Node.

**Parameters:**
 - tree_nodes (Iterable[TreeNodeData]): The Tree Nodes to generate TreeScript with.
 - line_number_labels (bool): Whether to enable the LineNumber Labels feature. Default: False.

**Yields:**
 str - Each a Line of TreeScript.
    """
    if number_labels:
        node_number = 1
        for node in tree_nodes:
            yield _write_line(node, f"n{node_number}")
            node_number += 1
    else:
        for node in tree_nodes:
            yield _write_line(node)


def _write_line(
    data: TreeNodeData,
    label: str = '',
) -> str:
    """ Convert a Tree Node into a line of TreeScript.

**Parameters:**
 - data (TreeNodeData): The dataclass container object for a Tree Node.

**Returns:**
 str - The Line of TreeScript generated from the Tree Node data.
    """
    line_end = "/" if data.is_dir else f" {label}" if label != '' else ''
    return data.depth * '  ' + f"{data.name}" + line_end
