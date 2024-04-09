"""Testing Module Methods
"""
import pytest

from input.input_data import InputData
from treescriptify.tree_runner import _check_arguments, get_tree_json


def test_get_tree_json_():
	input_data = InputData()
	#assert get_tree_json(input_data)
	pass


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (InputData(include_hidden=False, git_ignore=False), ''),
        (InputData(git_ignore=False), '-a'),
        (InputData(), '-a --gitignore'),
        (InputData(directories_only=True), '-d -a --gitignore'),
        (InputData(prune_dirs=True), '--prune -a --gitignore'),
        (InputData(directories_only=True, prune_dirs=True), '-d --prune -a --gitignore'),
    ]
)
def test_check_arguments(test_input, expected):
	assert _check_arguments(test_input) == expected
