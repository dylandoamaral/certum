import pytest

from certum import ensure, that
from certum.exception import CertumException
from certum.strategy.sorting.alphabetical import AlphabeticalSorting
from tests.utils import assert_error


def test_contains_keys_success():
    """Ensuring that x is a dict with keys 'a' and 'b' should return no
    exception."""
    obj = {"x": {"a": 2, "b": 3}}
    validator = ensure(obj).respects(that("x").contains_keys(["a", "b"]))
    validator.check()


def test_contains_keys_failure_one_key():
    """Ensuring that x is a dict with keys 'a' and 'b' should return an assertion
    error saying that one key is missing."""
    obj = {"x": {"a": 2}}
    validator = ensure(obj).respects(that("x").contains_keys(["a", "b"]))
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The key b is missing.")


def test_contains_keys_failure_multiple_keys():
    """Ensuring that x is a dict with keys 'a' and 'b' should return an assertion
    error saying that the first key is missing."""
    obj = {"x": {}}
    validator = (
        ensure(obj)
        .respects(that("x").contains_keys(["a", "b"]))
        .using(AlphabeticalSorting())
    )
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The key a is missing.\n[x] => The key b is missing.")
