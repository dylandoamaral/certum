from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule


class DictRuleList(DictRule):
    """The rule ensuring that a path is a list.

    :param path: The path that should be a list.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary is a list or not.

        :raises AssertionError: if the path's value is not a list.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        path = " -> ".join(self.path)
        message = f"The path {path} is not a list."
        if not isinstance(self.target(dictionary), list):
            errors.append(self.error(message))
        return errors
