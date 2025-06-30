"""
"""
from treescriptify.data.input_data import InputData
#from treescriptify.gitignore import load_gitignore_patterns
from treescriptify.input.argument_parser import parse_args


def validate_arguments(arguments: list[str]) -> InputData:
    """ Parse then Validate the given Arguments List, produce an InputData object.

**Parameters:**
 - arguments (list[str]): The list of arguments to parse.

**Returns:*
 InputData - The dataclass object containing the Program Input.
    """
    arg_data = parse_args(arguments)
    #ignore_patterns = load_gitignore_patterns() if arg_data.git_ignore else []
    return InputData(
        ignore_hidden=not arg_data.include_hidden,
        directories_only=arg_data.directories_only,
        prune_dirs=arg_data.prune_dirs,
        depth=arg_data.depth,
        #ignore_patterns=ignore_patterns if len(ignore_patterns) > 0 else None
    )
