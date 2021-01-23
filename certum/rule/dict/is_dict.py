from typing import Any, Dict

from certum.rule.generic.abstract import JsonRule


class JsonRuleDict(JsonRule):
    """The rule ensuring that a path is a dict.

    :param path: The path that should be a dict.
    :type path: str
    """

    def __init__(self, path: str):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding json is a dict or not.

        :raises AssertionError: if the path's value is not a dict.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        message = f"The path {self.path} is not a dict."
        assert isinstance(self.target(json), dict), self.error(message)
