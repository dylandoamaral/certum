import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_is_not_empty_success():
    """Ensuring that x is not empty."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").is_not_empty())
    validator.check()


@pytest.mark.parametrize(
    "empty",
    [None, {}, [], ""],
)
def test_is_not_empty_failure(empty):
    """Ensuring that x is empty."""
    obj = {"x": empty}
    validator = ensure(obj).respects(that("x").is_not_empty())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path x is empty.")


def test_unknown_path():
    """Ensuring that the rule doesn't start if the path is unknown."""
    obj = {}
    validator = ensure(obj).respects(that("x").is_not_empty())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")
