from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule
from certum.rule.shared.is_empty import JsonRuleEmpty


class JsonRuleKeyNotEmpty(JsonRule):
    """The rule ensuring that a path is not empty.

    :param path: The path that should not be empty.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is not empty.

        Embedded rules:
            - :class:`certum.rule.shared.is_empty.JsonRuleEmpty`

        :raises AssertionError: if the path is empty.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        path = " -> ".join(self.path)
        message = f"The path {path} is empty."
        errors = JsonRuleEmpty(self.path).check(json)
        if not errors:
            return [self.error(message)]
        return []
