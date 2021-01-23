import pytest

from certum import ensure, that


def test_is_list_success():
    """Ensuring that x is a list should return no exception."""
    obj = {"x": []}
    validator = ensure(obj).respects(that("x").is_list())
    validator.check()


def test_is_list_failure():
    """Ensuring that x is a list should return an assertion error."""
    obj = {"x": {}}
    validator = ensure(obj).respects(that("x").is_list())
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The path x is not a list."
