import pytest

from certum import ensure, that, this
from certum.exception import CertumException
from tests.utils import assert_error


def test_foreach_dict_success():
    """Ensuring that foreach is applied correctly for a dict."""
    obj = {"x": {"a": 2, "b": 2, "c": 2}}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").foreach(rule))
    validator.check()


def test_foreach_dict_failure():
    """Ensuring that foreach is applied correctly with a failure for a dict."""
    obj = {"x": {"a": 2, "b": 2, "c": 3}}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").foreach(rule))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x -> c] => 2 is not equal to 3.")


def test_foreach_list_success():
    """Ensuring that foreach is applied correctly for a list."""
    obj = {"x": [2, 2, 2]}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").foreach(rule))
    validator.check()


def test_foreach_list_failure():
    """Ensuring that foreach is applied correctly with a failure for a dict."""
    obj = {"x": [2, 2, 3]}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").foreach(rule))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x -> 2] => 2 is not equal to 3.")


def test_foreach_list_path_success():
    """Ensuring that foreach is applied correctly for a list."""
    obj = {"x": [{"y": 2}, {"y": 2}, {"y": 2}]}
    rule = that("y").equals(2)
    validator = ensure(obj).respects(that("x").foreach(rule))
    validator.check()


def test_unknown_path():
    """Ensuring that the rule doesn't start if the path is unknown."""
    obj = {}
    rule = that("y").equals(2)
    validator = ensure(obj).respects(that("x").foreach(rule))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")
