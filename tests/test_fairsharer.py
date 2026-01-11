"""Tests for the fairsharer.my_module module.
"""
import pytest

from fairsharer.my_module import fair_sharer


def test_fair_sharer():
    result_1 = fair_sharer([0, 1000, 800, 0], 1)
    assert result_1 == [100.0, 800.0, 900.0, 0.0]

    result_2 = fair_sharer([0, 1000, 800, 0], 2)
    assert result_2 == [100.0, 890.0, 720.0, 90.0]

"""
def test_hello_with_error():
    with pytest.raises(ValueError) as excinfo:
        hello("nobody")
    assert "Cannot say hello to nobody" in str(excinfo.value)


@pytest.fixture
def some_name():
    return "Jane Smith"


def test_hello_with_fixture(some_name):
    assert hello(some_name) == "Hello Jane Smith!"
"""