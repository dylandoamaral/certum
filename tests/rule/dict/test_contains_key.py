import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_contains_key_success():
    """Ensuring that x is a dict with a key 'a' should return no exception."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").contains_key("a"))
    validator.check()


def test_contains_key_failure():
    """Ensuring that x is a dict with a key 'a' should return an assertion
    error."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").contains_key("b"))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The key b is missing.")
