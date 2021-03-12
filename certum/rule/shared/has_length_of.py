from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.apply import DictRuleApply


class DictRuleLength(DictRuleApply):
    """The rule ensuring that a path has a particular length.

    :param path: The path where the key should be present.
    :type path: List[Any]
    :param value: The length of the this of the path.
    :type value: int
    """

    def __init__(self, path: List[Any], length: int):
        """Constructor method"""
        super().__init__(path, self._lambda)
        self.length = length

    def _lambda(self, value: Any) -> List[str]:
        """
        Check if the length of an element inside the dictionary is equal to the expected
        length.

        :param value: The value from the dictionary.
        :type value: Any
        :return: The list of error messages.
        :rtype: List[str]
        """
        try:
            length = len(value)
        except TypeError:
            # TODO Probably add verification in case of value who is not
            # elligible with len function and return an assertion error.
            length = 1

        if length != self.length:
            return [f"The length is {length}, expected {self.length}."]
        return []
