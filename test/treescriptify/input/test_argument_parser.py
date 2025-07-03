""" Testing Module Methods
"""
import pytest

from treescriptify.input.argument_data import ArgumentData
from treescriptify.input.argument_parser import parse_args


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ([], ArgumentData()),
        (['-a'], ArgumentData(include_hidden=False)),
        (['-d'], ArgumentData(directories_only=True)),
        (['-ad'], ArgumentData(include_hidden=False, directories_only=True)),
        (['-ad', '--no-gitignore'], ArgumentData(include_hidden=False, directories_only=True, git_ignore=False)),
        (['--gitignore'], ArgumentData(git_ignore=False)),
        (['--prune'], ArgumentData(prune_dirs=True)),
        (['-p'], ArgumentData(prune_dirs=True)),
        (['-adp'], ArgumentData(include_hidden=False, directories_only=True, prune_dirs=True)),
        (['--depth', '1'], ArgumentData(depth=1)),
        (['--depth', '4'], ArgumentData(depth=4)),
        (['-n'], ArgumentData(number_labels=True)),
        (['--number-labels'], ArgumentData(number_labels=True)),
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
        (['--depth']), # Needs to have the integer argument
        (['--depth', '-3']), # Range check ensures positive integers
        (['--depth', 'abc']), # Cannot be string or other type
    ]
)
def test_parse_args_raises_exit(test_input):
	try:
		parse_args(test_input)
		assert False
	except SystemExit:
		assert True
