"""Testing Module Methods
"""
import pytest

from treescriptify.input_data import InputData
from treescriptify.argument_parser import parse_args


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ([], InputData()),
        (['-a'], InputData(include_hidden=False)),
        (['-d'], InputData(directories_only=True)),
        (['--gitignore'], InputData(git_ignore=False)),
        (['--prune'], InputData(prune_dirs=True)),
    ]
)
def test_parse_args_returns_input(test_input, expected):
	assert parse_args(test_input) == expected


@pytest.mark.parametrize(
    'test_input',
    [
        (['']),
        ([' ']),
        (['r']),
        (['eeee']),
    ]
)
def test_parse_args_raises_exit(test_input):
	try:
		parse_args(test_input)
		assert False
	except SystemExit:
		assert True
