from typing import Any, Dict

import pytest

from certum import ensure, that
from certum.exception import CertumException
from certum.rule.generic.abstract import JsonRule
from tests.utils import assert_error


def test_target_one_depth():
    """Ensuring that you can target a value on a dict of depth 1."""
    obj = {"x": 1}
    rule = JsonRule(["x"])
    assert rule.target(obj) == 1


def test_target_two_depths():
    """Ensuring that you can target a value on a dict of depth 2."""
    obj = {"x": {"y": 2}}
    rule = JsonRule(["x", "y"])
    assert rule.target(obj) == 2


def test_target_one_depth_list():
    """Ensuring that you can target a value on a list of depth 1."""
    obj = [2]
    rule = JsonRule(["0"])
    assert rule.target(obj) == 2


def test_target_two_depths_list():
    """Ensuring that you can target a value on a list of depth 2."""
    obj = [[3, 2]]
    rule = JsonRule(["0", "1"])
    assert rule.target(obj) == 2


def test_target_three_depths_both():
    """Ensuring that you can target a value on a dict composed by both
    lists and dicts."""
    obj = {"a": [{"b": 2}]}
    rule = JsonRule(["a", "0", "b"])
    assert rule.target(obj) == 2


def test_exists_failure():
    """Ensuring that exists should return an assertion error."""
    obj = {}
    validator = ensure(obj).respects(that("x").exists())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")


def test_exists_nested_failure():
    """Ensuring that exists error should return an assertion error."""
    obj = {}
    validator = ensure(obj).respects(that("x -> b").exists())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")


def test_unknown_path():
    """Ensuring that the rule doesn't start if the path is unknown."""
    obj = {}
    validator = ensure(obj).respects(that("x").exists())
    with pytest.raises(CertumException) as error:
        validator.check()
    assert_error(error, "[x] => The path is missing.")
