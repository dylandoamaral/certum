from typing import Any, Dict

import pytest

from certum.exception import CertumException
from certum.rule.generic.abstract import JsonRule


class JsonRuleTest(JsonRule):
    """The mocking rule."""

    def check(self, json: Dict[str, Any]):
        """Rule always valid no matter what.

        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        assert True


def test_target_one_depth():
    """Ensuring that you can target a value on a dict of depth 1."""
    obj = {"x": 1}
    rule = JsonRuleTest("x")
    assert rule.target(obj) == 1


def test_target_two_depths():
    """Ensuring that you can target a value on a dict of depth 2."""
    obj = {"x": {"y": 2}}
    rule = JsonRuleTest("x -> y")
    assert rule.target(obj) == 2


def test_target_one_depth_list():
    """Ensuring that you can target a value on a list of depth 1."""
    obj = [2]
    rule = JsonRuleTest("0")
    assert rule.target(obj) == 2


def test_target_two_depths_list():
    """Ensuring that you can target a value on a list of depth 2."""
    obj = [[3, 2]]
    rule = JsonRuleTest("0 -> 1")
    assert rule.target(obj) == 2


def test_target_three_depths_both():
    """Ensuring that you can target a value on a dict composed by both
    lists and dicts."""
    obj = {"a": [{"b": 2}]}
    rule = JsonRuleTest("a -> 0 -> b")
    assert rule.target(obj) == 2


def test_target_failure():
    """Ensuring that you can't target an uknown path."""
    obj = {"a": 2}
    rule = JsonRuleTest("a -> x")
    with pytest.raises(CertumException):
        rule.target(obj)
