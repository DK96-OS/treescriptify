"""
"""
import pytest

from test.treescriptify.conftest import DEFAULT_INPUT, DEPTH_1_INPUT, DEPTH_2_INPUT


@pytest.mark.parametrize(
    'depth_value', [
        0, 1, 2, 5e10,
    ]
)
def test_is_depth_exceeded_default_always_returns_false(depth_value):
    assert not DEFAULT_INPUT.is_depth_exceeded(depth_value)


@pytest.mark.parametrize(
    'depth_value', [
        0,
    ]
)
def test_is_depth_exceeded_depth_1_returns_false(depth_value):
    assert not DEPTH_1_INPUT.is_depth_exceeded(depth_value)


@pytest.mark.parametrize(
    'depth_value', [
        1, 2, 3, 5e10,
    ]
)
def test_is_depth_exceeded_depth_1_returns_true(depth_value):
    assert DEPTH_1_INPUT.is_depth_exceeded(depth_value)


@pytest.mark.parametrize(
    'depth_value', [
        0, 1,
    ]
)
def test_is_depth_exceeded_depth_2_returns_false(depth_value):
    assert not DEPTH_2_INPUT.is_depth_exceeded(depth_value)


@pytest.mark.parametrize(
    'depth_value', [
        2, 3, 4, 5e10,
    ]
)
def test_is_depth_exceeded_depth_2_returns_true(depth_value):
    assert DEPTH_2_INPUT.is_depth_exceeded(depth_value)



