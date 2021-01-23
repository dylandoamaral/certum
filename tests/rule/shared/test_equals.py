import pytest

from certum import ensure, that


def test_equals_success():
    """Ensuring that x is equal to 2."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").equals(2))
    validator.check()


def test_is_list_failure():
    """Ensuring that x is equal to 2 throw an assertion error."""
    obj = {"x": 3}
    validator = ensure(obj).respects(that("x").equals(2))
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => 2 is not equal to 3."
