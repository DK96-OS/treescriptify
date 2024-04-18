"""Tree Node Data
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeNodeData:
    """
    """

    depth: int
    #
    is_dir: bool
    #
    name: str
