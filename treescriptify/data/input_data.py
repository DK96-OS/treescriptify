""" Input Data to the Program
"""
from dataclasses import dataclass
#from re import Pattern


@dataclass(frozen=True)
class InputData:
    """ The optional flags to modify the output of the program.

**Fields:**
 - ignore_hidden (bool): Whether to ignore hidden files and directories. Default: False.
 - directories_only (bool): Filter out all files. Default: False.
 - prune_dirs (bool): Filter out empty directories. Default: False.
 - depth (int): The maximum depth of directories to traverse. Default: 0. Zero is unlimited.
 # Not-Yet Implemented:
 - ignore_patterns (list[Pattern]?): The patterns that will filter TreeScript output. Default: None. Contains Gitignore Regex patterns. Should be None instead of Empty list.
    """
    ignore_hidden: bool = False
    directories_only: bool = False
    prune_dirs: bool = False
    depth: int = 0
    #ignore_patterns: list[Pattern] | None = None

    def is_depth_exceeded(self, depth: int) -> bool:
        """ Determine whether the depth has been exceeded.
 - When depth is zero (default), this method returns false.

**Parameters:**
 - depth (int): The tree depth to check against the set limit.

**Returns:**
 bool - True if the given depth exceeds the InputData limit.
        """
        return 0 < self.depth <= depth
