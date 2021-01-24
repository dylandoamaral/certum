import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_is_list_success():
    """Ensuring that x is a list should return no exception."""
    obj = {"x": []}
    validator = ensure(obj).respects(that("x").is_list())
    validator.check()


def test_is_list_failure():
    """Ensuring that x is a list should return an assertion error."""
    obj = {"x": {}}
    validator = ensure(obj).respects(that("x").is_list())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path x is not a list.")
