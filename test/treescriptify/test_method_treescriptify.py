""" Testing the Treescriptify Method.
"""
import os

from treescriptify import treescriptify

from test.treescriptify.conftest import DEFAULT_INPUT, EXCLUDE_HIDDEN_INPUT, DIR_ONLY_INPUT, DIR_ONLY_HIDE_INPUT, \
    DIR_ONLY_PRUNE_INPUT


def test_treescriptify_default_nested_tree(mock_nested_tree):
    os.chdir(mock_nested_tree)
    assert treescriptify(DEFAULT_INPUT) == """src/
  main/
    SourceClass.java
"""


def test_treescriptify_ignore_hidden_nested_tree(mock_nested_tree):
    os.chdir(mock_nested_tree)
    assert treescriptify(EXCLUDE_HIDDEN_INPUT) == """src/
  main/
    SourceClass.java
"""


def test_treescriptify_dirs_only_nested_tree(mock_nested_tree):
    os.chdir(mock_nested_tree)
    assert treescriptify(DIR_ONLY_INPUT) == """src/
  main/
"""


def test_treescriptify_dirs_only_hide_nested_tree(mock_nested_tree):
    os.chdir(mock_nested_tree)
    assert treescriptify(DIR_ONLY_HIDE_INPUT) == """src/
  main/
"""


def test_treescriptify_dirs_only_prune_nested_tree(mock_nested_tree):
    os.chdir(mock_nested_tree)
    assert treescriptify(DIR_ONLY_PRUNE_INPUT) == """src/
  main/
"""
