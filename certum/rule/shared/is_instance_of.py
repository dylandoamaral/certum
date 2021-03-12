from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.apply import DictRuleApply


class DictRuleInstanceOf(DictRuleApply):
    """The rule ensuring that a path is instance of a type type_.

    :param path: The path that should be of type type_.
    :type path: List[str]
    :param type_: The expected type.
    :type type_: type
    """

    def __init__(self, path: List[str], type_: type):
        """Constructor method"""
        super().__init__(path, self._lambda)
        self.type_ = type_

    def _lambda(self, value: Any) -> List[str]:
        """
        Check if the value inside the dictionary is instance of type_.

        :param value: The value from the dictionary.
        :type value: Any
        :return: The list of error messages.
        :rtype: List[str]
        """
        real_type = type(value).__name__
        expected_type = self.type_.__name__
        if real_type != expected_type:
            return [f"The value is instance of {real_type}, expected {expected_type}."]
        return []
