"""
"""
import json
from typing import Generator

from treescriptify.tree_node_data import TreeNodeData


def generate_from_json(json_string: str) -> Generator[TreeNodeData, None, None]:
    """
    """
    tree_son, report = json.loads(json_string)
    tree_son = tree_son['contents']
    depth = 0
    # todo:
    for i in tree_son:

    pass
