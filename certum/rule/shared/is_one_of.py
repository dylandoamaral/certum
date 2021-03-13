from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.apply import DictRuleApply


class DictRuleOneOf(DictRuleApply):
    """The rule ensuring that a path's value is one of a list of possible values.

    :param path: The path where the key should be present.
    :type path: List[Any]
    :param value: The list of possible values for the path.
    :type value: List[Any]
    """

    def __init__(self, path: List[Any], values: List[Any]):
        """Constructor method"""
        super().__init__(path, self._lambda)
        self.values = values

    def _lambda(self, value: Any) -> List[str]:
        """
        Check if the value inside the dictionary is equal to the expected value.

        :param value: The value from the dictionary.
        :type value: Any
        :return: The list of error messages.
        :rtype: List[str]
        """
        if value not in self.values:
            values = ", ".join([str(value) for value in self.values])
            return [f"The value is {value}, expected one of {values}."]
        return []
