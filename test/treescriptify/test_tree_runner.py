"""Testing Module Methods
"""
import pytest

from input.input_data import InputData
from treescriptify.tree_runner import get_tree_json


def test_get_tree_json_():
	input_data = InputData()
	#assert get_tree_json(input_data)
	pass


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('', ''),
    ]
)
def test_param(test_input, expected):
	#assert get_tree_json(test_input) == expected
	pass
