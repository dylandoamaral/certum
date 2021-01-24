import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_has_key_value_success():
    """Ensuring that x is a dict with a key 'a' should return no exception."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").has_key_value("a", 2))
    validator.check()


def test_has_key_value_failure():
    """Ensuring that x is a dict with a key 'a' should return an assertion
    error."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").has_key_value("a", "3"))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The key a is not equal to 3 but 2.")
