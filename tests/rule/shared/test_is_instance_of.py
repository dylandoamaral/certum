import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_is_instance_of_success():
    """Ensuring that x is not empty."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").is_instance_of(int))
    validator.check()


def test_is_instance_of_failure():
    """Ensuring that x is empty."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").is_instance_of(str))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The key is not instance of str but int.")


def test_unknown_path():
    """Ensuring that the rule doesn't start if the path is unknown."""
    obj = {}
    validator = ensure(obj).respects(that("x").is_instance_of(str))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")
