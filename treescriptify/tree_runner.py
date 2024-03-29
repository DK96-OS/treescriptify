"""Tree Runner
"""
import subprocess

from input.input_data import InputData


def get_tree_json(data: InputData) -> str:
    """Obtain the Tree Information as a JSON string.
    """
    result = subprocess.run(
        args=['tree', '-J', '-i', '-x', '--noreport'] + _check_arguments(data),
        capture_output=True,
        text=True,
        shell=False,
    )
    output = result.stdout
    #error = result.stderr
    return output


def _check_arguments(data: InputData) -> list[str]:
    """Check the Input Data and map flags to tree command.
    """
    extras = []
    if data.directories_only:
        extras += '-d'
    if data.prune_dirs:
        extras += '--prune'
    if data.include_hidden:
        extras += '-a'
    if data.git_ignore:
        extras += '--gitignore'
    return extras
