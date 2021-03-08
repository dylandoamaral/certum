import pytest

from certum import ensure, that
from certum.exception import CertumException
from certum.strategy.sorting.alphabetical import AlphabeticalSorting
from tests.utils import assert_error


def test_one():
    """Ensure that certum accumulate multiple type of errors together."""
    obj = {
        "a": 2,
        "b": {
            "c": [],
        },
        "d": "e",
    }

    validator = (
        ensure(obj)
        .respects(
            that("a").equals(2),
            that("b").is_instance_of(list),
            that("b -> c").is_instance_of(int),
            that("x -> a").equals(2),
            that("x -> b").equals(4),
        )
        .using(AlphabeticalSorting())
    )

    with pytest.raises(CertumException) as error:
        validator.check()

    errors = [
        "[b] => The key is not instance of list but dict.",
        "[b -> c] => The key is not instance of int but list.",
        "[x] => The path is missing.",
    ]
    assert_error(error, "\n".join(errors))
