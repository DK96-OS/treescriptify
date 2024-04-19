"""Testing Module Methods
"""
import pytest
import subprocess

from treescriptify.input_data import InputData
from treescriptify.tree_runner import _check_arguments, get_tree_json


def get_cmd_result(*args, **kwargs):
	result = type('MyObject', (object,), {'stdout': '[{"type":"directory","name":".","contents":[{"type":"file","name":"test_script_writer.py"},{"type":"file","name":"test_tree_reader.py"},{"type":"file","name":"test_tree_runner.py"}]}]'})
	return result


def test_get_tree_json_():
	input_data = InputData()
	with pytest.MonkeyPatch().context() as c:
		c.setattr(subprocess, 'run', lambda *args, **kwargs: get_cmd_result(*args, **kwargs))
		result = get_tree_json(input_data)
		expected_files = [
			"test_script_writer.py",
			"test_tree_reader.py",
			"test_tree_runner.py",
		]
		for filename in expected_files:
			assert filename in result


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
