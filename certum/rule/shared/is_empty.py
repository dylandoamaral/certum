from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule


class JsonRuleEmpty(JsonRule):
    """The rule ensuring that a path is empty.

    :param path: The path that should be empty.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is empty.

        :raises AssertionError: if the path isn't empty.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(json)
        if errors:
            return errors
        empty_possibilities = ["", None, [], {}]
        value = self.target(json)
        path = " -> ".join(self.path)
        message = f"The path {path} is not empty."
        if value not in empty_possibilities:
            errors.append(self.error(message))
        return errors
