import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


@pytest.mark.parametrize(
    "empty",
    [None, {}, [], ""],
)
def test_is_empty_success(empty):
    """Ensuring that x is empty."""
    obj = {"x": empty}
    validator = ensure(obj).respects(that("x").is_empty())
    validator.check()


def test_is_empty_failure():
    """Ensuring that x is not empty."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").is_empty())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path x is not empty.")
