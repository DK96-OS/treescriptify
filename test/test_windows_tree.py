"""Testing Windows tree Methods
"""
from pathlib import Path
import pytest

from treescriptify.input_data import InputData
from treescriptify.windows_tree import _gen_tree


DEFAULT_INPUT = InputData()
EXCLUDE_HIDDEN_INPUT = InputData(include_hidden=False)
DIR_ONLY_INPUT = InputData(directories_only=True)
PRUNE_DIR_INPUT = InputData(prune_dirs=True)
DIR_ONLY_PRUNE_INPUT = InputData(include_hidden=False, directories_only=True, prune_dirs=True)


BASIC_TREE = ['src', 'src/data.txt']
#   src/
#     data.txt

NESTED_DIR = ['src', 'src/data.txt', 'src/main', 'src/main/SourceClass.java']
#   src/
#     data.txt
#     main/
#       SourceClass.java

HIDDEN_DIRS = ['.github', '.github/dependabot.yml', '.github/workflows', '.github/workflows/ci.yml', '.hidden.txt', 'src', 'src/data.txt']
#   .github/
#     dependabot.yml
#     workflows/
#       ci.yml
#   .hidden.txt
#   src/
#     data.txt


def mock_iterdir(contents: list[str]):
    for c in contents:
        yield Path(c)


def test_gen_tree_default_input_basic_tree_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(BASIC_TREE))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DEFAULT_INPUT, './'))
        print('\n'.join(result))
        

def test_gen_tree_default_input_nested_dir_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(NESTED_DIR))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DEFAULT_INPUT, './'))
        print('\n'.join(result))

        
def test_gen_tree_default_input_hidden_dirs_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(HIDDEN_DIRS))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DEFAULT_INPUT, './'))
        print('\n'.join(result))

        
def test_gen_tree_exclude_hidden_input_basic_tree_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(BASIC_TREE))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(EXCLUDE_HIDDEN_INPUT, './'))
        print('\n'.join(result))
        

def test_gen_tree_exclude_hidden_input_nested_dir_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(NESTED_DIR))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(EXCLUDE_HIDDEN_INPUT, './'))
        print('\n'.join(result))

        
def test_gen_tree_exclude_hidden_input_hidden_dirs_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(HIDDEN_DIRS))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(EXCLUDE_HIDDEN_INPUT, './'))
        print('\n'.join(result))


def test_gen_tree_dir_only_input_basic_tree_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(BASIC_TREE))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DIR_ONLY_INPUT, './'))
        print('\n'.join(result))
        

def test_gen_tree_dir_only_input_nested_dir_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(NESTED_DIR))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DIR_ONLY_INPUT, './'))
        print('\n'.join(result))

        
def test_gen_tree_dir_only_input_hidden_dirs_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(HIDDEN_DIRS))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DIR_ONLY_INPUT, './'))
        print('\n'.join(result))


def test_gen_tree_prune_dir_input_basic_tree_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(BASIC_TREE))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(PRUNE_DIR_INPUT, './'))
        print('\n'.join(result))
        

def test_gen_tree_prune_dir_input_nested_dir_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(NESTED_DIR))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(PRUNE_DIR_INPUT, './'))
        print('\n'.join(result))

        
def test_gen_tree_prune_dir_input_hidden_dirs_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(HIDDEN_DIRS))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(PRUNE_DIR_INPUT, './'))
        print('\n'.join(result))


def test_gen_tree_dir_only_prune_input_basic_tree_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(BASIC_TREE))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DIR_ONLY_PRUNE_INPUT, './'))
        print('\n'.join(result))
        

def test_gen_tree_dir_only_prune_input_nested_dir_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(NESTED_DIR))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DIR_ONLY_PRUNE_INPUT, './'))
        print('\n'.join(result))

        
def test_gen_tree_dir_only_prune_input_hidden_dirs_returns_data():
    with pytest.MonkeyPatch().context() as mock:
        mock.setattr(Path, 'iterdir', lambda: mock_iterdir(HIDDEN_DIRS))
        mock.setattr(Path, 'exists', lambda: True)
        mock.setattr(Path, 'name', lambda: True)
        #
        mock.setattr(Path, 'is_dir', lambda: True)
        #
        result = list(_gen_tree(DIR_ONLY_PRUNE_INPUT, './'))
        print('\n'.join(result))

