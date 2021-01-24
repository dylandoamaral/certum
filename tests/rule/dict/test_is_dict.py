import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_is_dict_success():
    """Ensuring that x is a dict should return no exception."""
    obj = {"x": {}}
    validator = ensure(obj).respects(that("x").is_dict())
    validator.check()


def test_is_dict_failure():
    """Ensuring that x is a dict should return an assertion error."""
    obj = {"x": []}
    validator = ensure(obj).respects(that("x").is_dict())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path x is not a dict.")
