import pytest

from certum import ensure, that, this
from certum.exception import CertumException
from certum.strategy.printing.grouped import GroupedPrinting
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
            that("b", "c").is_instance_of(int),
            that("x", "a").equals(2),
            that("x", "b").equals(4),
        )
        .using(AlphabeticalSorting())
    )

    with pytest.raises(CertumException) as error:
        validator.check()

    errors = [
        "[b] => The value is instance of dict, expected list.",
        "[b -> c] => The value is instance of list, expected int.",
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
            that("name").equals("Hello"),
            that("entities").foreach(this.equals(1)),
            that("nested", "value").equals(4),
        )
        .using(GroupedPrinting(), AlphabeticalSorting())
    )

    with pytest.raises(CertumException) as error:
        validator.check()

    errors = [
        "entities -> 1   => The value is 3, expected 1.",
        "entities -> 2   => The value is 3, expected 1.",
        "name            => The value is 2, expected Hello.",
        "                   The value is instance of int, expected str.",
        "nested -> value => The value is 2, expected 4.",
    ]
    assert_error(error, "\n".join(errors))
