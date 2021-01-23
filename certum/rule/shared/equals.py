from typing import Any, Dict

from certum.rule.generic.abstract import JsonRule


class JsonRuleEqual(JsonRule):
    """The rule ensuring that a path has a particular value.

    :param path: The path where the key should be present.
    :type path: str
    :param value: The value of the path.
    :type value: Any
    """

    def __init__(self, path: str, value: Any):
        """Constructor method"""
        self.path = path
        self.value = value

    def check(self, json: Dict[str, Any]):
        """Check if the path from the corresponding json equal a value.

        :raises AssertionError: if the path doesn't equal the value.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        """
        _value = self.target(json)
        message = f"{self.value} is not equal to {_value}."
        assert _value == self.value, self.error(message)
