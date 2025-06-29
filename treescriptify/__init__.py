""" TreeScriptify Package
"""
from typing import Generator

from .data.input_data import InputData
from .file_tree import generate_tree
from .script_writer import generate_script


def tsfy(
    data: InputData,
) -> str:
    """ Run Treescriptify with the given Input.

**Parameters:**
 - data (InputData): The program options and ignore patterns.

**Returns:**
 str - The total TreeScript output from the operation.
    """
    return '\n'.join(
        generate_treescript(data)
    )


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
