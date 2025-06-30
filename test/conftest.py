"""
"""
from pathlib import Path

import pytest


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
def mock_empty_dirs_tree(tmp_path):
    my_dirs = tmp_path / 'empty_dirs/'
    my_dirs.mkdir()
    for n in range(1, 4): # Create Numbered Empty Dirs
        (my_dirs / f'dir{n}').mkdir()
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


@pytest.fixture
def mock_gitignore_tree(tmp_path: Path) -> Path:
    gitignore_file = tmp_path / '.gitignore'
    gitignore_file.touch()
    gitignore_file.write_text("""# Basic Gitignore Patterns:
.ftb/
__**__.py
__pycache__/
""")
    (example_dir := tmp_path / 'example').mkdir()
    (example_dir / '__init__.py').touch()
    (example_dir / '__main__.py').touch()
    (example_dir / 'example_module.py').touch()
    (ftb_dir := tmp_path / '.ftb').mkdir()
    return Path(str(tmp_path))
