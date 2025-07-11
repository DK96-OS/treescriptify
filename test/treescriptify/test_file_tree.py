""" Testing Windows tree Methods
"""
from treescriptify import generate_tree
from treescriptify.data.tree_node_data import TreeNodeData

from test.treescriptify.conftest import DEFAULT_INPUT, EXCLUDE_HIDDEN_INPUT, DIR_ONLY_INPUT, DIR_ONLY_HIDE_INPUT, \
    PRUNE_DIR_INPUT, DIR_ONLY_PRUNE_INPUT, EXCLUDE_HIDDEN_WITH_DIR_ONLY_PRUNE, DEPTH_1_INPUT, DEPTH_2_INPUT, \
    DEPTH_1_DIR_ONLY_INPUT, DEPTH_2_DIR_ONLY_INPUT, DEPTH_1_PRUNE_DIR_INPUT, DEPTH_2_PRUNE_DIR_INPUT


# BASIC_TREE
#   src/
#     data.txt

# NESTED_TREE
#   src/
#     main/
#       SourceClass.java

# HIDDEN_TREE
# on Windows:
#   .github/
#     dependabot.yml
#     workflows/
#       ci.yml
#   .hidden.txt
#
# on unix:
#   .github/
#     workflows/
#       ci.yml
#     dependabot.yml
#   .hidden.txt


def test_tree_default_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in generate_tree(DEFAULT_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, False, 'data.txt'),
    ]


def test_tree_default_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in generate_tree(DEFAULT_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
        TreeNodeData(2, False, 'SourceClass.java'),
    ]


def test_tree_default_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in generate_tree(DEFAULT_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(1, True, 'workflows'),
        TreeNodeData(2, False, 'ci.yml'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_tree_default_input_hidden_tree2_returns_data(mock_hidden_tree2):
    result = [x for x in generate_tree(DEFAULT_INPUT, mock_hidden_tree2)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'borkflows'), # Sorting is alphabetical, not dir/file based
        TreeNodeData(2, False, 'ci.yml'),
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_tree_exclude_hidden_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in generate_tree(EXCLUDE_HIDDEN_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, False, 'data.txt'),
    ]


def test_tree_exclude_hidden_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in generate_tree(EXCLUDE_HIDDEN_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
        TreeNodeData(2, False, 'SourceClass.java'),
    ]

        
def test_tree_exclude_hidden_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in generate_tree(EXCLUDE_HIDDEN_INPUT, mock_hidden_tree)]
    assert result == []


def test_tree_dir_only_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in generate_tree(DIR_ONLY_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
    ]


def test_tree_dir_only_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in generate_tree(DIR_ONLY_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
    ]

    
def test_tree_dir_only_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in iter(generate_tree(DIR_ONLY_INPUT, mock_hidden_tree))]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'workflows'),
    ]


def test_tree_dir_only_hide_input_hidden_tree_returns_empty(mock_hidden_tree):
    assert 0 == len(list(generate_tree(DIR_ONLY_HIDE_INPUT, mock_hidden_tree)))


def test_tree_prune_dir_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in generate_tree(PRUNE_DIR_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, False, 'data.txt'),
    ]


def test_tree_prune_dir_input_nested_tree_returns_data(mock_nested_tree):    
    result = [x for x in generate_tree(PRUNE_DIR_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
        TreeNodeData(2, False, 'SourceClass.java'),
    ]


def test_tree_prune_dir_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in generate_tree(PRUNE_DIR_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(1, True, 'workflows'),
        TreeNodeData(2, False, 'ci.yml'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_tree_dir_only_prune_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in generate_tree(DIR_ONLY_PRUNE_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
    ]


def test_tree_dir_only_prune_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in generate_tree(DIR_ONLY_PRUNE_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
    ]


def test_tree_dir_only_prune_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in generate_tree(DIR_ONLY_PRUNE_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'workflows'),
    ]


def test_tree_exclude_hidden_dir_only_prune_input_hidden_tree_returns_empty(mock_hidden_tree):
    result = [x for x in generate_tree(EXCLUDE_HIDDEN_WITH_DIR_ONLY_PRUNE, mock_hidden_tree)]
    assert result == []


def test_tree_depth_1_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in generate_tree(DEPTH_1_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
    ]


def test_tree_depth_1_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in generate_tree(DEPTH_1_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
    ]


def test_tree_depth_1_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in generate_tree(DEPTH_1_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_tree_depth_1_input_hidden_tree2_returns_data(mock_hidden_tree2):
    result = [x for x in generate_tree(DEPTH_1_INPUT, mock_hidden_tree2)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_tree_depth_2_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in generate_tree(DEPTH_2_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, False, 'data.txt'),
    ]


def test_tree_depth_2_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in generate_tree(DEPTH_2_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
    ]


def test_tree_depth_2_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in generate_tree(DEPTH_2_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(1, True, 'workflows'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_tree_depth_2_input_hidden_tree2_returns_data(mock_hidden_tree2):
    result = [x for x in generate_tree(DEPTH_2_INPUT, mock_hidden_tree2)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'borkflows'), # Sorting is alphabetical, not dir/file based
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_tree_depth_1_dir_only_input_empty_dirs_tree_returns_data(mock_empty_dirs_tree):
    result = [x for x in generate_tree(DEPTH_1_DIR_ONLY_INPUT, mock_empty_dirs_tree)]
    assert result == [
        TreeNodeData(0, True, 'empty_dirs'),
    ]


def test_tree_depth_2_dir_only_input_empty_dirs_tree_returns_data(mock_empty_dirs_tree):
    result = [x for x in generate_tree(DEPTH_2_DIR_ONLY_INPUT, mock_empty_dirs_tree)]
    assert result == [
        TreeNodeData(0, True, 'empty_dirs'),
        TreeNodeData(1, True, 'dir1'),
        TreeNodeData(1, True, 'dir2'),
        TreeNodeData(1, True, 'dir3'),
    ]


def test_tree_depth_1_prune_input_empty_dirs_tree_returns_data(mock_empty_dirs_tree):
    result = [x for x in generate_tree(DEPTH_1_PRUNE_DIR_INPUT, mock_empty_dirs_tree)]
    assert result == [
        TreeNodeData(0, True, 'empty_dirs'),
    ]


def test_tree_depth_2_prune_input_empty_dirs_tree_returns_data(mock_empty_dirs_tree):
    result = [x for x in generate_tree(DEPTH_2_PRUNE_DIR_INPUT, mock_empty_dirs_tree)]
    assert result == [
        TreeNodeData(0, True, 'empty_dirs'),
    ]


def test_tree_depth_1_dir_only_input_hidden_tree2_returns_data(mock_hidden_tree2):
    result = [x for x in generate_tree(DEPTH_1_DIR_ONLY_INPUT, mock_hidden_tree2)]
    assert result == [
        TreeNodeData(0, True, '.github'),
    ]


def test_tree_depth_2_dir_only_input_hidden_tree2_returns_data(mock_hidden_tree2):
    result = [x for x in generate_tree(DEPTH_2_DIR_ONLY_INPUT, mock_hidden_tree2)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'borkflows'),
    ]

