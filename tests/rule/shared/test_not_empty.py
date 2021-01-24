import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_empty_success():
    """Ensuring that x is not empty."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").is_not_empty())
    validator.check()


@pytest.mark.parametrize(
    "empty",
    [None, {}, [], ""],
)
def test_empty_failure(empty):
    """Ensuring that x is empty."""
    obj = {"x": empty}
    validator = ensure(obj).respects(that("x").is_not_empty())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path x is empty.")
