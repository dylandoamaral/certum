import pytest

from certum import ensure, that, this, using
from certum.dsl import JsonRuleDsl
from certum.exception import CertumException
from certum.strategy.filtering.thunk import ThunkFiltering
from certum.validator import JsonValidator


def test_ensure():
    "The ensure function should create a default JsonValidator."
    validator = ensure({})
    assert isinstance(validator, JsonValidator)


def test_ensure_fail():
    "The ensure function should fail if the parameter is not a dict."
    with pytest.raises(CertumException):
        ensure("hello")


def test_that():
    "The that function should create a JsonRuleDsl that targets a path."
    element = that("a -> b")
    assert isinstance(element, JsonRuleDsl)
    assert element.path == ["a", "b"]


def test_this():
    "The that function should create a JsonRuleDsl that targets the root."
    element = this
    assert isinstance(element, JsonRuleDsl)
    assert element.path == []
    validator = ensure({"a": "b"}).respects(this.has_key_value("a", "b"))
    validator.check()


def test_using():
    "The using function should create an empty JsonValidator with selected strategies."
    validator = using(ThunkFiltering())
    assert isinstance(validator.filtering, ThunkFiltering)
    assert validator.json == None
