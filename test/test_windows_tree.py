"""Testing Windows tree Methods
"""
from pathlib import Path

import pytest

from treescriptify.input_data import InputData
from treescriptify.tree_node_data import TreeNodeData
from treescriptify.windows_tree import win_tree


DEFAULT_INPUT = InputData()
EXCLUDE_HIDDEN_INPUT = InputData(include_hidden=False)
DIR_ONLY_INPUT = InputData(directories_only=True)
DIR_ONLY_HIDE_INPUT = InputData(directories_only=True, include_hidden=False)
PRUNE_DIR_INPUT = InputData(prune_dirs=True)
DIR_ONLY_PRUNE_INPUT = InputData(directories_only=True, prune_dirs=True)
EXCLUDE_HIDDEN_WITH_DIR_ONLY_PRUNE = InputData(
    include_hidden=False, directories_only=True, prune_dirs=True
)


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


@pytest.fixture
def mock_basic_tree(tmp_path):
    src_dir = tmp_path / 'src'  
    src_dir.mkdir()
    (src_dir / 'data.txt').touch()
    return Path(str(tmp_path))


@pytest.fixture
def mock_nested_tree(tmp_path):
    src_dir = tmp_path / 'src'
    src_dir.mkdir()
    main_dir = src_dir / 'main'
    main_dir.mkdir()
    (main_dir / 'SourceClass.java').touch()
    return Path(str(tmp_path))


@pytest.fixture
def mock_hidden_tree(tmp_path):
    github_dir = tmp_path / '.github'
    github_dir.mkdir()
    (github_dir / 'dependabot.yml').touch()
    workflows_dir = github_dir / 'workflows'
    workflows_dir.mkdir()
    (workflows_dir / 'ci.yml').touch()
    (tmp_path / '.hidden.txt').touch()
    return Path(str(tmp_path))


@pytest.fixture
def mock_hidden_tree2(tmp_path):
    github_dir = tmp_path / '.github'
    github_dir.mkdir()
    (github_dir / 'dependabot.yml').touch()
    workflows_dir = github_dir / 'borkflows'
    workflows_dir.mkdir()
    (workflows_dir / 'ci.yml').touch()
    (tmp_path / '.hidden.txt').touch()
    return Path(str(tmp_path))


def test_win_tree_default_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in win_tree(DEFAULT_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, False, 'data.txt'),
    ]


def test_win_tree_default_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in win_tree(DEFAULT_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
        TreeNodeData(2, False, 'SourceClass.java'),
    ]


def test_win_tree_default_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in win_tree(DEFAULT_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(1, True, 'workflows'),
        TreeNodeData(2, False, 'ci.yml'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_win_tree_default_input_hidden_tree2_returns_data(mock_hidden_tree2):
    result = [x for x in win_tree(DEFAULT_INPUT, mock_hidden_tree2)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'borkflows'), # Sorting is alphabetical, not dir/file based
        TreeNodeData(2, False, 'ci.yml'),
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_win_tree_exclude_hidden_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in win_tree(EXCLUDE_HIDDEN_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, False, 'data.txt'),
    ]


def test_win_tree_exclude_hidden_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in win_tree(EXCLUDE_HIDDEN_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
        TreeNodeData(2, False, 'SourceClass.java'),
    ]

        
def test_win_tree_exclude_hidden_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in win_tree(EXCLUDE_HIDDEN_INPUT, mock_hidden_tree)]
    assert result == []


def test_win_tree_dir_only_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in win_tree(DIR_ONLY_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
    ]


def test_win_tree_dir_only_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in win_tree(DIR_ONLY_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
    ]

    
def test_win_tree_dir_only_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in iter(win_tree(DIR_ONLY_INPUT, mock_hidden_tree))]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'workflows'),
    ]


def test_win_tree_dir_only_hide_input_hidden_tree_returns_empty(mock_hidden_tree):
    assert 0 == len(list(win_tree(DIR_ONLY_HIDE_INPUT, mock_hidden_tree)))


def test_win_tree_prune_dir_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in win_tree(PRUNE_DIR_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, False, 'data.txt'),
    ]


def test_win_tree_prune_dir_input_nested_tree_returns_data(mock_nested_tree):    
    result = [x for x in win_tree(PRUNE_DIR_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
        TreeNodeData(2, False, 'SourceClass.java'),
    ]


def test_win_tree_prune_dir_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in win_tree(PRUNE_DIR_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, False, 'dependabot.yml'),
        TreeNodeData(1, True, 'workflows'),
        TreeNodeData(2, False, 'ci.yml'),
        TreeNodeData(0, False, '.hidden.txt'),
    ]


def test_win_tree_dir_only_prune_input_basic_tree_returns_data(mock_basic_tree):
    result = [x for x in win_tree(DIR_ONLY_PRUNE_INPUT, mock_basic_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
    ]


def test_win_tree_dir_only_prune_input_nested_tree_returns_data(mock_nested_tree):
    result = [x for x in win_tree(DIR_ONLY_PRUNE_INPUT, mock_nested_tree)]
    assert result == [
        TreeNodeData(0, True, 'src'),
        TreeNodeData(1, True, 'main'),
    ]


def test_win_tree_dir_only_prune_input_hidden_tree_returns_data(mock_hidden_tree):
    result = [x for x in win_tree(DIR_ONLY_PRUNE_INPUT, mock_hidden_tree)]
    assert result == [
        TreeNodeData(0, True, '.github'),
        TreeNodeData(1, True, 'workflows'),
    ]


def test_win_tree_exclude_hidden_dir_only_prune_input_hidden_tree_returns_empty(mock_hidden_tree):
    result = [x for x in win_tree(EXCLUDE_HIDDEN_WITH_DIR_ONLY_PRUNE, mock_hidden_tree)]
    assert result == []