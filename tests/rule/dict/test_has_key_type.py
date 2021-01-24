import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


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
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The key a is not an instance of str but int.")
