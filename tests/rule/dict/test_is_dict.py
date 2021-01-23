import pytest

from certum import ensure, that


def test_is_dict_success():
    """Ensuring that x is a dict should return no exception."""
    obj = {"x": {}}
    validator = ensure(obj).respects(that("x").is_dict())
    validator.check()


def test_is_dict_failure():
    """Ensuring that x is a dict should return an assertion error."""
    obj = {"x": []}
    validator = ensure(obj).respects(that("x").is_dict())
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The path x is not a dict."
