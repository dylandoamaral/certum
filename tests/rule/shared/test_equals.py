import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_equals_success():
    """Ensuring that x is equal to 2."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").equals(2))
    validator.check()


def test_equals_failure():
    """Ensuring that x is equal to 2 throw an assertion error."""
    obj = {"x": 3}
    validator = ensure(obj).respects(that("x").equals(2))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The value is 3, expected 2.")
