from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.apply import DictRuleApply


class DictRuleEqual(DictRuleApply):
    """The rule ensuring that a path has a particular value.

    :param path: The path where the key should be present.
    :type path: List[Any]
    :param value: The value of the path.
    :type value: Any
    """

    def __init__(self, path: List[Any], value: Any):
        """Constructor method"""
        super().__init__(path, self._lambda)
        self.value = value

    def _lambda(self, value: Any) -> List[str]:
        """
        Check if the value inside the dictionary is equal to the expected value.

        :param value: The value from the dictionary.
        :type value: Any
        :return: The list of error messages.
        :rtype: List[str]
        """
        if value != self.value:
            return [f"The value is {value}, expected {self.value}."]
        return []
