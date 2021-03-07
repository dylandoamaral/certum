import pytest

from certum import ensure, that
from certum.exception import CertumException
from tests.utils import assert_error


def test_has_unique_elements_dict_success():
    """Ensuring that foreach is applied correctly for a dict."""
    obj = {"x": {"a": 2, "b": 3, "c": 4}}
    validator = ensure(obj).respects(that("x").has_unique_elements())
    validator.check()


def test_has_unique_elements_dict_failure():
    """Ensuring that foreach is applied correctly with a failure for a dict."""
    obj = {"x": {"a": 2, "b": 2, "c": 3}}
    validator = ensure(obj).respects(that("x").has_unique_elements())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The row 0 and 1 are the same.")


def test_has_unique_elements_list_success():
    """Ensuring that foreach is applied correctly for a list."""
    obj = {"x": [2, 3, 4]}
    validator = ensure(obj).respects(that("x").has_unique_elements())
    validator.check()


def test_has_unique_elements_list_failure():
    """Ensuring that foreach is applied correctly with a failure for a dict."""
    obj = {"x": [2, 2, 3]}
    validator = ensure(obj).respects(that("x").has_unique_elements())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The row 0 and 1 are the same.")


def test_has_unique_elements_other_success():
    """Ensuring that foreach is applied correctly for any other value."""
    obj = {"x": 2}
    validator = ensure(obj).respects(that("x").has_unique_elements())
    validator.check()


def test_unknown_path():
    """Ensuring that the rule doesn't start if the path is unknown."""
    obj = {}
    validator = ensure(obj).respects(that("x").has_unique_elements())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")
