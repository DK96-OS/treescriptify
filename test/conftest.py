"""
"""
import tempfile

import pytest
from pathlib import Path


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
