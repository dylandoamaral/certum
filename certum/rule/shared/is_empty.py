from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.apply import DictRuleApply


class DictRuleEmpty(DictRuleApply):
    """The rule ensuring that a path is empty.

    :param path: The path that should be empty.
    :type path: List[Any]
    """

    def __init__(self, path: List[Any]):
        """Constructor method"""
        super().__init__(path, self._lambda)

    def _lambda(self, value: Any) -> List[str]:
        """
        Check if the value is empty.

        .. note::

            A value is considered as empty if it is one of "", None, [], {}

        :param value: The value from the dictionary.
        :type value: Any
        :return: The list of error messages.
        :rtype: List[str]
        """
        empty_possibilities = ["", None, [], {}]
        if value not in empty_possibilities:
            return ["The target is not empty."]
        return []
