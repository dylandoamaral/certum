import pytest

from certum import ensure, that, this
from certum.exception import CertumException
from certum.strategy.printing.grouped import GroupedPrinting
from certum.strategy.sorting.alphabetical import AlphabeticalSorting
from certum.strategy.sorting.alphanumerical import AlphanumericalSorting
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


def test_two():
    """Ensure that certum accumulate multiple type of errors together + strategies."""
    my_obj = {"name": 2, "entities": [1, 3, 3], "nested": {"value": 2}}

    validator = (
        ensure(my_obj)
        .respects(
            that("name").is_instance_of(str),
            that("entities").foreach(this.equals(1)),
            that("nested -> value").equals(4),
        )
        .using(GroupedPrinting(), AlphanumericalSorting())
    )

    with pytest.raises(CertumException) as error:
        validator.check()

    errors = [
        "entities -> 1   => 1 is not equal to 3.",
        "entities -> 2   => 1 is not equal to 3.",
        "name            => The key is not instance of str but int.",
        "nested -> value => 4 is not equal to 2.",
    ]
    assert_error(error, "\n".join(errors))
