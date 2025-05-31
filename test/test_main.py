""" Testing Main Module.
"""
from collections.abc import Callable


def assert_expected(expected) -> Callable[[str], None]:
    def _assertion(result):
        assert result == expected
    return _assertion


def test_main_ad(monkeypatch):
    from treescriptify.__main__ import main
    import sys
    from sys import orig_argv
    sys.argv = ['treescriptify', '-ad']
    import builtins
    expected = """test/
  __pycache__/
treescriptify/
  __pycache__/"""
    monkeypatch.setattr(builtins, 'print', assert_expected(expected))
    main()
    sys.argv = orig_argv