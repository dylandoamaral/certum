import pytest

from certum import ensure, that


def test_contains_keys_success():
    """Ensuring that x is a dict with keys 'a' and 'b' should return no
    exception."""
    obj = {"x": {"a": 2, "b": 3}}
    validator = ensure(obj).respects(that("x").contains_keys(["a", "b"]))
    validator.check()


def test_contains_keys_failure_one_key():
    """Ensuring that x is a dict with keys 'a' and 'b' should return an assertion
    error saying that one key is missing."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").contains_keys(["a", "b"]))
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The key b is missing."


def test_contains_keys_failure_multiple_keys():
    """Ensuring that x is a dict with keys 'a' and 'b' should return an assertion
    error saying that the first key is missing."""
    obj = {"x": {}}
    validator = ensure(obj).respects(that("x").contains_keys(["a", "b"]))
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The key a is missing."
