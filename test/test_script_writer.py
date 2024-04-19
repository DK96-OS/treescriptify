"""Testing Module Methods
"""
import pytest

from treescriptify.script_writer import generate_script
from treescriptify.tree_node_data import TreeNodeData


def generator_single_dir_node(name: str, depth: int=0):
	yield TreeNodeData(depth, True, name)


def generator_single_file_node(name: str, depth: int=0):
	yield TreeNodeData(depth, False, name)


def generator_depth_1():
	yield TreeNodeData(0, True, 'module')
	yield TreeNodeData(1, False, 'file.txt')
	yield TreeNodeData(1, True, 'src')


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (generator_single_dir_node('.directory'), '.directory/'),
        (generator_single_dir_node('.directory', 1), '  .directory/'),
        (generator_single_file_node('file.txt'), 'file.txt'),
        (generator_single_file_node('file.txt', 1), '  file.txt'),
		(generator_depth_1(), 'module/\n  file.txt\n  src/')
    ]
)
def test_generate_script_returns_str(test_input, expected):
	script_gen = generate_script(test_input)
	assert "\n".join(script_gen) == expected
