"""TreeScriptify Package
"""
from .input_data import InputData
from .tree_runner import get_tree_json
from .tree_reader import generate_from_json
from .script_writer import generate_script
from .windows_tree import win_tree


def tsfy(data: InputData) -> str:
    """Run Treescriptify on the given Inputs.
    """
    return '\n'.join(
        generate_script(
            generate_from_json(
                get_tree_json(data)
            )
        )
    )


def tsfy_windows(data: InputData) -> str:
    """Run Treescriptify on the given Inputs, on a Windows OS.
    """
    return '\n'.join(
        generate_script(
            win_tree(data)
        )
    )
