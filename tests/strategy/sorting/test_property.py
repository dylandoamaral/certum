from random import shuffle

import pytest

from certum.strategy.sorting.alphabetical import AlphabeticalSorting
from certum.strategy.sorting.alphanumerical import AlphanumericalSorting
from tests.utils import generate_errors

startegies = [AlphabeticalSorting(), AlphanumericalSorting()]


@pytest.mark.parametrize("strategy", startegies)
def test_same_order(strategy):
    """A sorting strategy should always sort paths the same way even if the starting
    order is different (Except the NoSorting)."""

    for i in range(0, 50):
        errors = generate_errors(50, 5)
        shuffled = errors.copy()
        shuffle(shuffled)
        assert strategy.sort(errors) == strategy.sort(shuffled)


@pytest.mark.parametrize("strategy", startegies)
def test_same_number(strategy):
    """A sorting strategy should always conserve the number of errors."""

    for i in range(0, 50):
        errors = generate_errors(50, 5)
        assert len(strategy.sort(errors)) == len(errors)
