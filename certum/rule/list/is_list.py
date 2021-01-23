from typing import Any, Dict

from certum.rule.generic.abstract import JsonRule


class JsonRuleList(JsonRule):
    """The rule ensuring that a path is a list.

    :param path: The path that should be a list.
    :type path: str
    """

    def __init__(self, path: str):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding json is a list or not.

        :raises AssertionError: if the path's value is not a list.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        message = f"The path {self.path} is not a list."
        assert isinstance(self.target(json), list), self.error(message)
