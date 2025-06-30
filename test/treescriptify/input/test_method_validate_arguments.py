""" Testing Input Package Method ValidateArguments.
"""
import os
from pathlib import Path

from treescriptify.data.input_data import InputData
from treescriptify.input import validate_arguments


def test_validate_arguments_empty_dir(tmp_path: Path):
    initial_dir = os.getcwd()
    os.chdir(tmp_path)
    #
    result: InputData = validate_arguments([])
    # Returns to initial directory
    os.chdir(initial_dir)
    #
    assert not result.ignore_hidden
    assert not result.directories_only
    assert not result.prune_dirs
    assert result.depth == 0


def test_validate_arguments_basic_tree(mock_basic_tree: Path):
    initial_dir = os.getcwd()
    os.chdir(mock_basic_tree)
    #
    result = validate_arguments([])
    # Returns to initial directory
    os.chdir(initial_dir)
    #
    assert not result.ignore_hidden
    assert not result.directories_only
    assert not result.prune_dirs
    assert result.depth == 0


def test_validate_arguments_nested_tree_depth1(mock_nested_tree: Path):
    initial_dir = os.getcwd()
    os.chdir(mock_nested_tree)
    #
    result = validate_arguments(['--depth', '1'])
    # Returns to initial directory
    os.chdir(initial_dir)
    #
    assert not result.ignore_hidden
    assert not result.directories_only
    assert not result.prune_dirs
    assert result.depth == 1


def test_validate_arguments_nested_tree_dirs_only(mock_nested_tree: Path):
    initial_dir = os.getcwd()
    os.chdir(mock_nested_tree)
    #
    result = validate_arguments(['-d'])
    # Returns to initial directory
    os.chdir(initial_dir)
    #
    assert not result.ignore_hidden
    assert result.directories_only
    assert not result.prune_dirs
    assert result.depth == 0


def test_validate_arguments_hidden_tree_hide(mock_hidden_tree: Path):
    initial_dir = os.getcwd()
    os.chdir(mock_hidden_tree)
    #
    result = validate_arguments(['--hide'])
    # Returns to initial directory
    os.chdir(initial_dir)
    #
    assert result.ignore_hidden
    assert not result.directories_only
    assert not result.prune_dirs
    assert result.depth == 0
