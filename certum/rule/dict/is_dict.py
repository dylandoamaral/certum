from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import JsonRule


class JsonRuleDict(JsonRule):
    """The rule ensuring that a path is a dict.

    :param path: The path that should be a dict.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, json: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding json is a dict or not.

        :param json: The Json to analyse.
        :type json: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(json)
        if errors:
            return errors
        path = " -> ".join(self.path)
        message = f"The path {path} is not a dict."
        if not isinstance(self.target(json), dict):
            errors.append(self.error(message))
        return errors
