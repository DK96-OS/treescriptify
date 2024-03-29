"""TreeScriptify Package
"""
from input.input_data import InputData
from treescriptify.tree_runner import get_tree_json
from treescriptify.tree_reader import generate_from_json
from treescriptify.script_writer import generate_script


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
