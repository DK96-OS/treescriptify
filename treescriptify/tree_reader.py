"""
"""
import json
from typing import Generator

from .tree_node_data import TreeNodeData


def generate_from_json(json_string: str) -> Generator[TreeNodeData, None, None]:
    """Read the JSON string and generate TreeNodeData for all elements.
    """
    full_json = json.loads(json_string)
    for i in full_json['contents']:
        for node in _process_node(i, 0):
            yield node


def _process_node(node: dict, depth: int) -> Generator[TreeNodeData, None, None]:
    """
    """
    if node['type'] == 'file':
        yield TreeNodeData(depth, False, node['name'])
    else:
        yield TreeNodeData(depth, True, node['name'])
        for nested_nodes in node.get('contents', []):
            for node in _process_node(nested_nodes, depth + 1):
                yield node
