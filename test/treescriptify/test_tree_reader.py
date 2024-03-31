"""Testing Module Methods
"""
import pytest

from treescriptify.tree_node_data import TreeNodeData
from treescriptify.tree_reader import generate_from_json


def wrap_root_dir(inner_dirs: str) -> str:
	return '{"type":"directory", "name":"src", "contents":[' + inner_dirs + ']}'


def get_src_dir() -> str:
	return '{"type":"directory", "name":"src", "contents":[]}'


def test_generate_from_json_empty_dir_returns_empty_list():
	tree_gen = generate_from_json(wrap_root_dir(''))
	assert list(tree_gen) == []


def test_generate_from_json_src_dir_returns_tree_node():
	tree_gen = generate_from_json(wrap_root_dir(get_src_dir()))
	assert list(tree_gen) == [TreeNodeData(0, True, 'src')]


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('{"type":"directory", "name":"src", "contents":[]}', [TreeNodeData(0, True, 'src')]),
    ]
)
def test_generate_from_json_(test_input, expected):
	tree_gen = generate_from_json(test_input)
	assert list(tree_gen) == expected
