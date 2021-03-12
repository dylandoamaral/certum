from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.abstract import DictRule
from certum.rule.shared.is_empty import DictRuleEmpty


class DictRuleNotEmpty(DictRuleEmpty):
    """The rule ensuring that a path is not empty.

    :param path: The path that should not be empty.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        super().__init__(path)

    def _lambda(self, value: Any) -> List[str]:
        """
        Check if the value is not empty.

        .. note::

            A value is considered as empty if it is one of "", None, [], {}

        :param value: The value from the dictionary.
        :type value: Any
        :return: The list of error messages.
        :rtype: List[str]
        """
        errors = super()._lambda(value)
        if errors:
            return []
        return ["The target is empty."]
