from typing import Any, Dict

from certum.rule.generic.abstract import JsonRule
from certum.rule.shared.is_empty import JsonRuleEmpty


class JsonRuleKeyNotEmpty(JsonRule):
    """The rule ensuring that a path is not empty.

    :param path: The path that should not be empty.
    :type path: str
    """

    def __init__(self, path: str):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding json is not empty.

        Embedded rules:
            - :class:`certum.rule.shared.is_empty.JsonRuleEmpty`

        :raises AssertionError: if the path is empty.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        message = f"The path {self.path} is empty."
        try:
            JsonRuleEmpty(self.path).check(json)
        except AssertionError:
            return
        assert False, self.error(message)
