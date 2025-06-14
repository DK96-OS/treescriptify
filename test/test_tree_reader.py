"""Testing Module Methods
"""
from itertools import repeat

import pytest

from treescriptify.tree_node_data import TreeNodeData
from treescriptify.tree_reader import generate_from_json


def wrap_root_dir(inner_dirs: str) -> str:
	return '[{"type":"directory", "name":".", "contents":[' + inner_dirs + ']}]'


def get_src_dir(contents: str = '') -> str:
	return '{"type":"directory", "name":"src", "contents":[' + contents + ']}'


def get_file(name: str) -> str:
	return '{"type":"file","name":"' + name + '"}'


def test_generate_from_json_empty_dir_returns_empty_list():
	tree_gen = generate_from_json(wrap_root_dir(''))
	assert list(tree_gen) == []


def test_generate_from_json_empty_str_raises_exit():
	with pytest.raises(SystemExit):
		list(generate_from_json(''))


def test_generate_from_json_non_json_str_raises_exit():
	with pytest.raises(SystemExit):
		list(generate_from_json('no'))


def test_generate_from_json_double_input_raises_exit():
	with pytest.raises(SystemExit):
		list(generate_from_json(str(repeat(get_src_dir(), 2))))


def test_generate_from_json_src_dir_returns_tree_node():
	tree_gen = generate_from_json(wrap_root_dir(get_src_dir()))
	assert list(tree_gen) == [TreeNodeData(0, True, 'src')]


def test_generate_from_json_src_dir_with_file_returns_2_nodes():
	tree_gen = generate_from_json(wrap_root_dir(get_src_dir(get_file('build.file'))))
	assert list(tree_gen) == [TreeNodeData(0, True, 'src'), TreeNodeData(1, False, 'build.file')]


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (wrap_root_dir(get_file('build.file')), [TreeNodeData(0, False, 'build.file')]),
        (wrap_root_dir(get_file('build.file') + ',\n\t\t' + get_file('req.txt')), [TreeNodeData(0, False, 'build.file'), TreeNodeData(0, False, 'req.txt')]),
    ]
)
def test_generate_from_json_(test_input, expected):
	tree_gen = generate_from_json(test_input)
	assert list(tree_gen) == expected