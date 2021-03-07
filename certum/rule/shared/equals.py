from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule


class JsonRuleEqual(JsonRule):
    """The rule ensuring that a path has a particular value.

    :param path: The path where the key should be present.
    :type path: List[str]
    :param value: The value of the path.
    :type value: Any
    """

    def __init__(self, path: List[str], value: Any):
        """Constructor method"""
        self.path = path
        self.value = value

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json equal a value.

        :raises AssertionError: if the path doesn't equal the value.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(json)
        if errors:
            return errors
        _value = self.target(json)
        message = f"{self.value} is not equal to {_value}."
        if _value != self.value:
            errors.append(self.error(message))
        return errors
