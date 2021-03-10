from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule


class DictRuleEqual(DictRule):
    """The rule ensuring that a path has a particular value.

    :param path: The path where the key should be present.
    :type path: List[Any]
    :param value: The value of the path.
    :type value: Any
    """

    def __init__(self, path: List[Any], value: Any):
        """Constructor method"""
        self.path = path
        self.value = value

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary equal a value.

        :raises AssertionError: if the path doesn't equal the value.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        _value = self.target(dictionary)
        message = f"{self.value} is not equal to {_value}."
        if _value != self.value:
            errors.append(self.error(message))
        return errors
