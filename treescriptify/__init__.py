""" TreeScriptify Package
"""
from typing import Generator

from .data.input_data import InputData
from .file_tree import generate_tree
from .script_writer import generate_script


def treescriptify(
    data: InputData,
) -> str:
    """ Run Treescriptify with the given Input.

**Parameters:**
 - data (InputData): The program options and ignore patterns.

**Returns:**
 str - The total TreeScript output from the operation.
    """
    treescript = '\n'.join(
        generate_treescript(data)
    )
    if len(treescript) > 0:
        treescript += '\n'
    return treescript


def generate_treescript(
    data: InputData,
) -> Generator[str, None, None]:
    """ Generate lines of TreeScript using the InputData options and ignore patterns.

**Parameters:**
 - data (InputData): The program options and ignore patterns.

**Yields:**
 str - Lines of TreeScript.
    """
    yield from generate_script(
        generate_tree(data)
    )
