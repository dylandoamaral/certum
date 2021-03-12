from typing import Any, Dict, List

from certum.error import Error
from certum.rule.generic.apply import DictRuleApply


class DictRuleUniqueElements(DictRuleApply):
    """The rule ensuring that a path has only unique elements.

    :param path: The path where the key should be present.
    :type path: List[str]
    """

    def __init__(self, path: List[str]):
        """Constructor method"""
        super().__init__(path, self._lambda)

    def _lambda(self, value: Any) -> List[str]:
        """
        Check if the value contains only unique elements.

        .. note::

            For `dict` instance, the rule is targeting the values.

        :param value: The value from the dictionary.
        :type value: Any
        :return: The list of error messages.
        :rtype: List[str]
        """
        try:
            length = len(value)
        except TypeError:
            # TODO Probably add verification in case of value who is not an
            # list or a dict.
            return []

        values = list(value.values()) if isinstance(value, dict) else value
        errors = []

        for i in range(0, length - 1):
            for j in range(1, length):
                if i != j:
                    first = values[i]
                    second = values[j]
                    message = f"The row {i} and {j} are the same."
                    if first == second:
                        errors.append(message)
        return errors
