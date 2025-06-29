"""
"""
from pathlib import Path
from re import Pattern, compile
from typing import Generator


def load_gitignore_patterns(
    debug: bool = False,
) -> list[Pattern]:
    """ Load compiled Regex Patterns from the local Gitignore File.

**Parameters:**
 - debug (bool): Whether to print a statement when the Gitignore file is missing, or a non-ascii char is found in a pattern.
    """
    return [compile(x) for x in _generate_gitignore_patterns(debug)]


def extract_patterns(
    gitignore_file: str,
    pattern_length_limit: int = 80,
    debug: bool = True,
) -> Generator[str, None, None]:
    """ Extract the Pattern Lines from a Gitignore file content string.
 - Pattern Length Limit will ignore longer lines.

**Parameters:**
 - gitignore_file (str): The string contents of the Gitignore File.
 - pattern_length_limit (int): The Limit on Pattern lines, applied after stripping space characters.

**Yields:**
 str - The pattern lines from the Gitignore file.
    """
    for line in gitignore_file.splitlines():
        line = line.strip()
        if line.startswith('#'): # Comments
            continue
        if len(line) > pattern_length_limit:
            continue
        if not line.isascii():
            if debug:
                exit("Non-Ascii characters detected in gitignore pattern.")
            continue
        if _is_valid_pattern(line):
            yield line


def _generate_gitignore_patterns(
    debug: bool,
) -> Generator[str, None, None]:
    if not (file_path := Path('.gitignore')).exists():
        if debug:
            print("Note: Gitignore File does not exist.")
        return
    try:
        yield from extract_patterns(file_path.read_text(), debug)
    except OSError:
        exit("Failed to Read Gitignore File.")


def _is_valid_pattern(unvalidated_line: str):
    # Assume any ascii pattern is okay
    if not unvalidated_line.isascii():
        exit("Non-Ascii characters detected in gitignore pattern.")
    return True
