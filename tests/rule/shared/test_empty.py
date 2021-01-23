import pytest

from certum import ensure, that


@pytest.mark.parametrize(
    "empty",
    [None, {}, [], ""],
)
def test_empty_success(empty):
    """Ensuring that x is empty."""
    obj = {"x": empty}
    validator = ensure(obj).respects(that("x").is_empty())
    validator.check()


def test_empty_failure():
    """Ensuring that x is not empty."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").is_empty())
    with pytest.raises(AssertionError) as error:
        validator.check()
    assert error.value.args[0] == "[x] => The path x is not empty."
