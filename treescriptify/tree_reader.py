"""
"""
import json
from json import JSONDecodeError
from sys import exit
from typing import Generator, Iterable

from .tree_node_data import TreeNodeData


def generate_from_json(json_string: str) -> Generator[TreeNodeData, None, None]:
    """Read the JSON string and generate TreeNodeData for all elements.
    """
    for i in _load_json(json_string):
        for node in _process_node(i, 0):
            yield node


def _load_json(json_str: str) -> Iterable[dict]:
    try:
        yield from json.loads(json_str)[0]['contents']
    except JSONDecodeError:
        exit("Failed to Decode JSON")
    return None


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