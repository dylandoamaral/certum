from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule
from certum.rule.shared.is_empty import DictRuleEmpty


class DictRuleNotEmpty(DictRule):
    """The rule ensuring that a path is not empty.

    :param path: The path that should not be empty.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        self.path = path

    def check(self, dictionary: Dict[str, Any]) -> List[Error]:
        """Check if the path from the corresponding dictionary is not empty.

        Embedded rules:
            - :class:`certum.rule.shared.is_empty.DictRuleEmpty`

        :raises AssertionError: if the path is empty.
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
        message = f"The path {path} is empty."
        error = DictRuleEmpty(self.path).check(dictionary)
        if not error:
            errors.append(self.error(message))
        return errors
