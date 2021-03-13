import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_is_one_of_success():
    """Ensuring that x is equal to 2."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").is_one_of([1, 2, 3]))
    validator.check()


def test_is_one_of_failure():
    """Ensuring that x is equal to 2 throw an assertion error."""
    obj = {"x": 4}
    validator = ensure(obj).respects(that("x").is_one_of([1, 2, 3]))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The value is 4, expected one of 1, 2, 3.")
