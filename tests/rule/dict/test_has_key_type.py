import pytest

from certum import ensure, that


def test_has_key_type_success():
    """Ensuring that x is a dict with a key 'a' should return no exception."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").has_key_type("a", int))
    validator.check()


def test_has_key_type_failure():
    """Ensuring that x is a dict with a key 'a' should return an assertion
    error."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").has_key_type("a", str))
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The key a is not an instance of str but int."
