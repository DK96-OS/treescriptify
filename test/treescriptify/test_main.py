""" Testing Main Module.
"""
import builtins
import os
import sys
from collections.abc import Callable

from treescriptify.__main__ import main


class PrintCollector:
    def __init__(self):
        self.collection: str = ''

    def get_output(self) -> str:
        return self.collection

    def append_print_output(self, output: str):
        self.collection = self.collection + output

    def assert_expected(self, expected: str):
        assert self.collection == expected


def setup_mock_print_collector() -> tuple[PrintCollector, Callable[[str], None]]:
    collector = PrintCollector()
    def _collection(result, **kwargs):
        collector.append_print_output(result)
        if (end_append := kwargs['end']) is not None:
            collector.append_print_output(end_append)
    return collector, _collection


def test_main_default_nested_tree(monkeypatch, mock_nested_tree):
    sys.argv = ['treescriptify']
    os.chdir(mock_nested_tree)
    expected = """src/
  main/
    SourceClass.java
"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_default_empty_dirs_tree_(monkeypatch, mock_empty_dirs_tree):
    sys.argv = ['treescriptify']
    os.chdir(mock_empty_dirs_tree)
    expected = """empty_dirs/
  dir1/
  dir2/
  dir3/
"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_a_empty_dirs_tree_(monkeypatch, mock_empty_dirs_tree):
    sys.argv = ['treescriptify', '-a']
    os.chdir(mock_empty_dirs_tree)
    expected = """empty_dirs/
  dir1/
  dir2/
  dir3/
"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_d_empty_dirs_tree_(monkeypatch, mock_empty_dirs_tree):
    sys.argv = ['treescriptify', '-d']
    os.chdir(mock_empty_dirs_tree)
    expected = """empty_dirs/
  dir1/
  dir2/
  dir3/
"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_p_empty_dirs_tree_(monkeypatch, mock_empty_dirs_tree):
    sys.argv = ['treescriptify', '-p']
    os.chdir(mock_empty_dirs_tree)
    expected = """empty_dirs/
"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_a_hidden_tree_(monkeypatch, mock_hidden_tree):
    sys.argv = ['treescriptify', '-a']
    os.chdir(mock_hidden_tree)
    expected = """"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_d_hidden_tree_(monkeypatch, mock_hidden_tree):
    sys.argv = ['treescriptify', '-d']
    os.chdir(mock_hidden_tree)
    expected = """.github/
  workflows/
"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_ad_hidden_tree(monkeypatch, mock_hidden_tree):
    sys.argv = ['treescriptify', '-ad']
    os.chdir(mock_hidden_tree)
    expected = """"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_a_hidden_tree2_(monkeypatch, mock_hidden_tree2):
    sys.argv = ['treescriptify', '-a']
    os.chdir(mock_hidden_tree2)
    expected = """"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_d_hidden_tree2_(monkeypatch, mock_hidden_tree2):
    sys.argv = ['treescriptify', '-d']
    os.chdir(mock_hidden_tree2)
    expected = """.github/
  borkflows/
"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)


def test_main_ad_hidden_tree2_(monkeypatch, mock_hidden_tree2):
    sys.argv = ['treescriptify', '-ad']
    os.chdir(mock_hidden_tree2)
    expected = """"""
    collector, mock_print = setup_mock_print_collector()
    monkeypatch.setattr(builtins, 'print', mock_print)
    main()
    collector.assert_expected(expected)

