import pytest

from certum import ensure, that, this, using
from certum.dsl import DictRuleDsl
from certum.exception import CertumException
from certum.strategy.filtering.thunk import ThunkFiltering
from certum.validator import DictValidator


def test_ensure():
    "The ensure function should create a default DictValidator."
    validator = ensure({})
    assert isinstance(validator, DictValidator)


def test_ensure_fail():
    "The ensure function should fail if the parameter is not a dict."
    with pytest.raises(CertumException):
        ensure("hello")


def test_that():
    "The that function should create a DictRuleDsl that targets a path."
    element = that("a", "b")
    assert isinstance(element, DictRuleDsl)
    assert element.path == ["a", "b"]


def test_this():
    "The that function should create a DictRuleDsl that targets the root."
    element = this
    assert isinstance(element, DictRuleDsl)
    assert element.path == []
    validator = ensure({"a": "b"}).respects(this.is_instance_of(dict))
    validator.check()


def test_using():
    "The using function should create an empty DictValidator with selected strategies."
    validator = using(ThunkFiltering())
    assert isinstance(validator.filtering, ThunkFiltering)
    assert validator.dictionary is None
