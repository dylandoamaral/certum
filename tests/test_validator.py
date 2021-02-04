import pytest

from certum import ensure, that
from certum.strategy.filtering.no import NoFiltering
from certum.strategy.filtering.first import FirstFiltering
from certum.strategy.printing.simple import SimplePrinting
from certum.strategy.printing.grouped import GroupedPrinting
from certum.strategy.sorting.alphanumerical import AlphanumericalSorting
from certum.strategy.sorting.no import NoSorting
from certum.exception import CertumException


def test_respects():
    """Respects should add more rule to the pool."""
    validator = ensure({})
    validator = validator.respects([that("x").equals(2), that("y").is_empty()])
    assert len(validator.rules) == 2
    validator = validator.respects([that("z").equals(4)])
    assert len(validator.rules) == 3


def test_using():
    """Using should setup correctly the strategies by chaining using."""
    validator = ensure({})
    assert isinstance(validator.sorting, NoSorting)
    assert isinstance(validator.filtering, NoFiltering)
    assert isinstance(validator.printing, SimplePrinting)
    validator = (
        validator.using(AlphanumericalSorting())
        .using(FirstFiltering())
        .using(GroupedPrinting())
    )
    assert isinstance(validator.sorting, AlphanumericalSorting)
    assert isinstance(validator.filtering, FirstFiltering)
    assert isinstance(validator.printing, GroupedPrinting)


def test_using_list():
    """Using should setup correctly the strategies with a list of strategies."""
    validator = ensure({})
    assert isinstance(validator.sorting, NoSorting)
    assert isinstance(validator.filtering, NoFiltering)
    assert isinstance(validator.printing, SimplePrinting)
    validator = validator.using(
        [AlphanumericalSorting(), FirstFiltering(), GroupedPrinting()]
    )
    assert isinstance(validator.sorting, AlphanumericalSorting)
    assert isinstance(validator.filtering, FirstFiltering)
    assert isinstance(validator.printing, GroupedPrinting)


def test_using_fail():
    """Using should return an error if an uknown strategy is provided."""
    with pytest.raises(CertumException):
        ensure({}).using(3)


def test_using_list_fail():
    """Using should return an error if an uknown strategy is provided inside a list."""
    with pytest.raises(CertumException):
        ensure({}).using([3])
