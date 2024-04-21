"""Tree Runner
"""
import subprocess

from treescriptify.input_data import InputData


def get_tree_json(data: InputData) -> str:
    """Obtain the Tree Information as a JSON string.
    """
    result = subprocess.run(
        args='tree -Ji --noreport ' + _check_arguments(data),
        capture_output=True,
        text=True,
        shell=True,
        timeout=5
    )
    #error = result.stderr
    return result.stdout


def _check_arguments(data: InputData) -> str:
    """Check the Input Data and map flags to tree command.
    """
    extras = []
    if data.directories_only:
        extras.append('-d')
    if data.prune_dirs:
        extras += ['--prune']
    if data.include_hidden:
        extras += ['-a']
    if data.git_ignore:
        extras.append('--gitignore')
    return ' '.join(extras)
