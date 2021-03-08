from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule


class DictRuleEmpty(DictRule):
    """The rule ensuring that a path is empty.

    :param path: The path that should be empty.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary is empty.

        :raises AssertionError: if the path isn't empty.
        :param dictionary: The Dict to analyse.
        :type dictionary: Dict[str, Any]
        :return: The list of errors catched by the rule, return empty list if
                 no errors.
        :rtype: List[Error]
        """
        errors = super().check(dictionary)
        if errors:
            return errors
        empty_possibilities = ["", None, [], {}]
        value = self.target(dictionary)
        path = " -> ".join(self.path)
        message = f"The path {path} is not empty."
        if value not in empty_possibilities:
            errors.append(self.error(message))
        return errors
