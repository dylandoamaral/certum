from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule


class JsonRuleList(JsonRule):
    """The rule ensuring that a path is a list.

    :param path: The path that should be a list.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is a list or not.

        :raises AssertionError: if the path's value is not a list.
        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        path = " -> ".join(self.path)
        message = f"The path {path} is not a list."
        if not isinstance(self.target(json), list):
            return [self.error(message)]
        return []
