import pytest

from certum import ensure, that, this
from certum.exception import CertumException
from certum.strategy.sorting.alphabetical import AlphabeticalSorting
from tests.utils import assert_error


def test_forsome_dict_success():
    """Ensuring that forsome is applied correctly for a dict."""
    obj = {"x": {"a": 2, "b": 2, "c": 3}}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").forsome(rule, keys=["a", "b"]))
    validator.check()


def test_forsome_dict_failure():
    """Ensuring that forsome is applied correctly with a failure for a dict."""
    obj = {"x": {"a": 2, "b": 2, "c": 3}}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").forsome(rule, keys=["a", "b", "c"]))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x -> c] => 2 is not equal to 3.")


def test_forsome_list_success():
    """Ensuring that forsome is applied correctly for a list."""
    obj = {"x": [2, 2, 3]}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").forsome(rule, keys=[0, 1]))
    validator.check()


def test_forsome_list_failure():
    """Ensuring that forsome is applied correctly with a failure for a dict."""
    obj = {"x": [2, 2, 3]}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").forsome(rule, keys=[0, 1, 2]))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x -> 2] => 2 is not equal to 3.")


def test_forsome_list_path_success():
    """Ensuring that forsome is applied correctly for a list."""
    obj = {"x": [{"y": 2}, {"y": 2}, {"y": 2}]}
    rule = that("y").equals(2)
    validator = ensure(obj).respects(that("x").forsome(rule, keys=[0, 1, 2]))
    validator.check()


def test_forsome_hybrid_success_and_failure():
    """Ensuring that forsome is applied correctly for a list."""
    obj = {"x": {"a": 2, "b": 3, "c": 3}}
    rule = this.equals(2)
    validator = (
        ensure(obj)
        .respects(that("x").forsome(rule, keys=["a", "b", "d"]))
        .using(AlphabeticalSorting())
    )
    with pytest.raises(CertumException) as error:
        validator.check()
    errors = ["[x -> b] => 2 is not equal to 3.", "[x -> d] => The path is missing."]
    assert_error(error, "\n".join(errors))


def test_unknown_path():
    """Ensuring that the rule doesn't start if the path is unknown."""
    obj = {}
    rule = that("y").equals(2)
    validator = ensure(obj).respects(that("x").forsome(rule, keys=[0]))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")


def test_no_keys_failure():
    """Ensuring that the rule need a 'keys' parameter to work."""
    obj = {}
    rule = that("y").equals(2)
    with pytest.raises(CertumException):
        ensure(obj).respects(that("x").forsome(rule))


def test_keys_no_list_failure():
    """Ensuring that the rule need a 'keys' parameter of type list to work."""
    obj = {}
    rule = that("y").equals(2)
    with pytest.raises(CertumException):
        ensure(obj).respects(that("x").forsome(rule, keys=2))


def test_type_failure():
    """Ensuring that forsome is not working if not a dict or a list."""
    obj = {"x": 2}
    rule = this.equals(2)
    validator = ensure(obj).respects(that("x").forsome(rule, keys=[0]))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path should be instance of dict or list.")
