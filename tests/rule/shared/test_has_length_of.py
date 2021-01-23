import pytest

from certum import ensure, that


def test_has_length_of_list_success():
    """Ensuring that x is equal a list of size 2."""
    obj = {"x": [2, 3]}
    validator = ensure(obj).respects(that("x").has_length_of(2))
    validator.check()


def test_has_length_of_list_failure():
    """Ensuring that x is equal a list of size 2 throw an assertion error."""
    obj = {"x": [2, 3, 4]}
    validator = ensure(obj).respects(that("x").has_length_of(2))
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The length of x is 3, expected 2."


def test_has_length_of_dict_success():
    """Ensuring that x is equal a dict of size 2."""
    obj = {"x": {"x": 2, "y": 3}}
    validator = ensure(obj).respects(that("x").has_length_of(2))
    validator.check()


def test_has_length_of_dict_failure():
    """Ensuring that x is equal a dict of size 2."""
    obj = {"x": {"x": 2, "y": 3, "z": 4}}
    validator = ensure(obj).respects(that("x").has_length_of(2))
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The length of x is 3, expected 2."


def test_has_length_of_other_success():
    """Ensuring that x is equal 1 for other value."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").has_length_of(1))
    validator.check()
